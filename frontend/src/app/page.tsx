"use client";

import { useEffect, useRef } from "react";
import * as d3 from "d3";

const API = "";
const COLORS: Record<string, string> = {
  Election: "#e74c3c", Person: "#3498db", PoliticalParty: "#2ecc71",
  Article: "#f39c12", Company: "#9b59b6", Sentiment: "#1abc9c",
  Poll: "#e67e22", NewsOutlet: "#e91e63",
};

export default function GraphPage() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let W = window.innerWidth, H = window.innerHeight;
    canvas.width = W; canvas.height = H;

    let nodes: any[] = [];
    let edges: any[] = [];
    let view = { x: 0, y: 0, k: 1 };
    let selected: string | null = null;
    let highlighted = new Set<string>();
    let draggedNode: any = null;
    let dragOff = { x: 0, y: 0 };
    let pan = { active: false, sx: 0, sy: 0, vx: 0, vy: 0 };
    let sim: d3.Simulation<any, any>;

    fetch(`${API}/api/graph`)
      .then(r => r.json())
      .then(data => {
        if (!data.nodes?.length) return;
        const nodeMap: Record<string, any> = {};
        nodes = data.nodes.map((n: any) => {
          const N = { ...n, x: Math.random() * W, y: Math.random() * H, fx: null as number | null, fy: null as number | null };
          nodeMap[N.id] = N;
          return N;
        });
        edges = data.edges.map((e: any) => ({
          ...e, source: nodeMap[e.source] || e.source, target: nodeMap[e.target] || e.target,
        }));

        const linkForce = d3.forceLink(edges).id((n: any) => n.id).distance(50).strength(0.15);
        const chargeForce = d3.forceManyBody().strength(-30);

        sim = d3.forceSimulation(nodes)
          .force("link", linkForce)
          .force("charge", chargeForce)
          .force("center", d3.forceCenter(W / 2, H / 2))
          .force("collision", d3.forceCollide(5))
          .alphaDecay(0.015)
          .on("tick", render);

        function nodeBaseSize(n: any) {
          const sizes: Record<string, number> = { Person: 7, Election: 5, PoliticalParty: 5, Article: 4 };
          return sizes[n.group] || 4;
        }

        function selectNode(id: string) {
          selected = id;
          highlighted = new Set([id]);
          for (const e of edges) {
            const s = e.source.id || e.source;
            const t = e.target.id || e.target;
            if (s === id) highlighted.add(t);
            if (t === id) highlighted.add(s);
          }
          for (const n of nodes) {
            n.fx = highlighted.has(n.id) ? null : n.x;
            n.fy = highlighted.has(n.id) ? null : n.y;
          }
          chargeForce.strength(-200);
          linkForce.distance(150).strength(0.08);
          sim.alpha(0.6).alphaTarget(0.2).restart();
          render();
        }

        function clearSelection() {
          selected = null;
          highlighted = new Set();
          for (const n of nodes) { n.fx = null; n.fy = null; }
          chargeForce.strength(-30);
          linkForce.distance(50).strength(0.15);
          sim.alpha(0.3).alphaTarget(0).restart();
          render();
        }

        function render() {
          if (!ctx) return;
          ctx.clearRect(0, 0, W, H);
          ctx.save();
          ctx.translate(view.x, view.y);
          ctx.scale(view.k, view.k);
          const hasSelection = selected !== null;

          for (const e of edges) {
            const s = e.source, t = e.target;
            const sId = s.id || s, tId = t.id || t;
            const active = !hasSelection || (highlighted.has(sId) && highlighted.has(tId));
            if (hasSelection && !active) continue;
            ctx.strokeStyle = "rgba(150,150,150,0.6)";
            ctx.lineWidth = 0.8 / view.k;
            ctx.beginPath(); ctx.moveTo(s.x, s.y); ctx.lineTo(t.x, t.y); ctx.stroke();
            if (hasSelection && active) {
              const mx = (s.x + t.x) / 2, my = (s.y + t.y) / 2;
              ctx.font = `${Math.max(6, 9 / view.k)}px sans-serif`;
              ctx.textAlign = "center"; ctx.textBaseline = "bottom";
              ctx.fillStyle = "#555";
              ctx.fillText(e.label, mx, my - 2);
              ctx.textAlign = "start";
            }
          }

          for (const n of nodes) {
            const active = !hasSelection || highlighted.has(n.id);
            if (hasSelection && !active) continue;
            const isSelected = n.id === selected;
            const r = hasSelection
              ? (isSelected ? Math.max(7, 14 / view.k) : Math.max(5, 8 / view.k))
              : Math.max(nodeBaseSize(n), 4 / view.k);
            ctx.beginPath(); ctx.arc(n.x, n.y, r, 0, 2 * Math.PI);
            ctx.fillStyle = COLORS[n.group] || "#95a5a6";
            ctx.fill();
            ctx.strokeStyle = isSelected ? "#000" : "#fff";
            ctx.lineWidth = isSelected ? 2.5 / view.k : 1 / view.k;
            ctx.stroke();
          }

          if (view.k > 0.4) {
            const fs = Math.max(7, 11 / view.k);
            ctx.font = `${fs}px sans-serif`;
            ctx.textBaseline = "middle";
            for (const n of nodes) {
              const active = !hasSelection || highlighted.has(n.id);
              if (hasSelection && !active) continue;
              const r = hasSelection
                ? (n.id === selected ? Math.max(7, 14 / view.k) : Math.max(5, 8 / view.k))
                : Math.max(nodeBaseSize(n), 4 / view.k);
              ctx.fillStyle = "#333";
              ctx.fillText(n.label, n.x + r + 3 / view.k, n.y);
            }
          }
          ctx.restore();
        }

        function getNodeRadius(n: any) {
          if (selected) {
            if (n.id === selected) return Math.max(7, 14 / view.k);
            if (highlighted.has(n.id)) return Math.max(5, 8 / view.k);
            return 0;
          }
          return Math.max(nodeBaseSize(n), 4 / view.k);
        }

        function hitTest(mx: number, my: number) {
          const sx = (mx - view.x) / view.k, sy = (my - view.y) / view.k;
          for (const n of nodes) {
            const r = getNodeRadius(n) + 3;
            if (r > 0 && Math.hypot(n.x - sx, n.y - sy) < r) return n;
          }
          return null;
        }

        function screenToSim(mx: number, my: number) {
          return { x: (mx - view.x) / view.k, y: (my - view.y) / view.k };
        }

        canvas.addEventListener("mousedown", (e) => {
          const n = hitTest(e.clientX, e.clientY);
          if (n) {
            if (n.id === selected) clearSelection();
            else selectNode(n.id);
            draggedNode = n;
            const s = screenToSim(e.clientX, e.clientY);
            dragOff.x = n.x - s.x; dragOff.y = n.y - s.y;
            n.fx = n.x; n.fy = n.y;
            sim.alphaTarget(0.3).restart();
            render();
          } else {
            clearSelection();
            pan.active = true;
            pan.sx = e.clientX; pan.sy = e.clientY;
            pan.vx = view.x; pan.vy = view.y;
          }
        });

        window.addEventListener("mousemove", (e) => {
          if (draggedNode) {
            const s = screenToSim(e.clientX, e.clientY);
            draggedNode.fx = s.x + dragOff.x;
            draggedNode.fy = s.y + dragOff.y;
          } else if (pan.active) {
            view.x = pan.vx + (e.clientX - pan.sx);
            view.y = pan.vy + (e.clientY - pan.sy);
            render();
          }
        });

        window.addEventListener("mouseup", () => {
          if (draggedNode) { draggedNode.fx = null; draggedNode.fy = null; draggedNode = null; sim.alphaTarget(0); }
          pan.active = false;
        });

        canvas.addEventListener("wheel", (e) => {
          e.preventDefault();
          const k = e.deltaY > 0 ? 0.88 : 1 / 0.88;
          const nk = Math.max(0.08, Math.min(12, view.k * k));
          view.x += (e.clientX - view.x) * (1 - nk / view.k);
          view.y += (e.clientY - view.y) * (1 - nk / view.k);
          view.k = nk;
          render();
        }, { passive: false });

        const resize = () => {
          W = window.innerWidth; H = window.innerHeight;
          canvas.width = W; canvas.height = H;
          render();
        };
        window.addEventListener("resize", resize);
      });
  }, []);

  return <canvas ref={canvasRef} className="block w-full h-full" />;
}
