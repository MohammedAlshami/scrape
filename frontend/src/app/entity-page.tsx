"use client";

import { useState, useEffect } from "react";
import Image from "next/image";
import { AspectRatio } from "@/components/ui/aspect-ratio";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import {
  Pagination,
  PaginationContent,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination";

const PAGE_SIZE = 12;

const COLORS = [
  "#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6",
  "#1abc9c", "#e67e22", "#e91e63", "#00bcd4", "#ff5722",
];

function getColor(name: string) {
  let hash = 0;
  for (let i = 0; i < name.length; i++) hash = name.charCodeAt(i) + ((hash << 5) - hash);
  return COLORS[Math.abs(hash) % COLORS.length];
}

function initials(name: string) {
  return name.split(" ").map(w => w[0]).join("").slice(0, 2).toUpperCase();
}

interface Relationship {
  rel: string;
  target: string;
  type: string;
}

interface Entity {
  name: string;
  relationships: Relationship[];
  [key: string]: any;
}

export default function EntityPage({ title, apiPath, subtitle, extraFields }: {
  title: string;
  apiPath: string;
  subtitle?: string;
  extraFields?: { key: string; label: string }[];
}) {
  const [items, setItems] = useState<Entity[]>([]);
  const [page, setPage] = useState(1);
  const [selected, setSelected] = useState<Entity | null>(null);

  useEffect(() => {
    fetch(apiPath)
      .then(r => r.json())
      .then(setItems);
  }, [apiPath]);

  const totalPages = Math.max(1, Math.ceil(items.length / PAGE_SIZE));
  const paged = items.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE);

  return (
    <div>
      <div className="max-w-7xl mx-auto px-4 pt-10">
        <div className="text-center mb-10">
          <h1 className="heading-lg mb-3">{title}</h1>
          <p className="text-muted-foreground text-lg">
            {subtitle || `${items.length} entities in the knowledge graph`}
          </p>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4">
        <div className="grid grid-cols-1 gap-8 md:grid-cols-2 md:gap-4 lg:grid-cols-4">
          {paged.map(item => (
            <button
              key={item.name}
              onClick={() => setSelected(item)}
              className="group block text-left w-full"
            >
              <div className="flex flex-col gap-4 rounded-xl transition-all duration-200">
                <AspectRatio ratio={4 / 3} className="overflow-hidden rounded-xl bg-muted flex items-center justify-center">
                  {item.logo_url || item.image_url ? (
                    item.logo_url ? (
                      <Image
                        src={item.logo_url}
                        alt={item.name}
                        width={100}
                        height={100}
                        className="object-contain w-16 h-16"
                      />
                    ) : (
                      <Image
                        src={item.image_url}
                        alt={item.name}
                        fill
                        className="object-cover"
                      />
                    )
                  ) : (
                    <div
                      className="w-16 h-16 rounded-full flex items-center justify-center text-white text-lg font-semibold"
                      style={{ backgroundColor: getColor(item.name) }}
                    >
                      {initials(item.name)}
                    </div>
                  )}
                </AspectRatio>
                <div className="flex flex-col gap-2">
                  <h3 className="text-base font-semibold tracking-tight group-hover:underline line-clamp-2">
                    {item.name}
                  </h3>
                  {extraFields?.map(f => (
                    <p key={f.key} className="text-muted-foreground text-sm min-h-[1.25rem]">
                      {item[f.key] || "\u00A0"}
                    </p>
                  ))}
                  <div className="flex flex-wrap gap-1.5 mt-1">
                    {item.relationships.slice(0, 3).map((rel, i) => (
                      <span
                        key={i}
                        className="text-[10px] px-2 py-0.5 rounded-full bg-secondary text-secondary-foreground"
                      >
                        {rel.rel.replace(/_/g, " ").toLowerCase()}
                      </span>
                    ))}
                    {item.relationships.length > 3 && (
                      <span className="text-[10px] text-muted-foreground">
                        +{item.relationships.length - 3}
                      </span>
                    )}
                    {item.relationships.length === 0 && (
                      <span className="text-[10px] text-muted-foreground">no relationships</span>
                    )}
                  </div>
                </div>
              </div>
            </button>
          ))}
        </div>
      </div>

      {totalPages > 1 && (
        <div className="py-8">
          <Pagination>
            <PaginationContent>
              <PaginationItem>
                <PaginationPrevious
                  href="#"
                  onClick={(e) => { e.preventDefault(); if (page > 1) setPage(p => p - 1); }}
                />
              </PaginationItem>
              {Array.from({ length: Math.min(totalPages, 10) }, (_, i) => i + 1).map(p => (
                <PaginationItem key={p}>
                  <PaginationLink
                    href="#"
                    isActive={p === page}
                    onClick={(e) => { e.preventDefault(); setPage(p); }}
                  >
                    {p}
                  </PaginationLink>
                </PaginationItem>
              ))}
              <PaginationItem>
                <PaginationNext
                  href="#"
                  onClick={(e) => { e.preventDefault(); if (page < totalPages) setPage(p => p + 1); }}
                />
              </PaginationItem>
            </PaginationContent>
          </Pagination>
        </div>
      )}

      <Dialog open={!!selected} onOpenChange={(open) => { if (!open) setSelected(null); }}>
        <DialogContent className="sm:max-w-lg max-h-[80vh] overflow-y-auto rounded-2xl scrollbar-hide p-0 gap-0">
          {selected && (
            <>
              {selected.logo_url ? (
                <div className="bg-muted flex items-center justify-center py-10 rounded-t-2xl">
                  <Image
                    src={selected.logo_url}
                    alt={selected.name}
                    width={80}
                    height={80}
                    className="object-contain w-20 h-20"
                  />
                </div>
              ) : selected.image_url ? (
                <div className="relative w-full h-48 rounded-t-2xl overflow-hidden">
                  <Image
                    src={selected.image_url}
                    alt={selected.name}
                    fill
                    className="object-cover"
                  />
                </div>
              ) : (
                <div className="bg-muted flex items-center justify-center py-10 rounded-t-2xl">
                  <div
                    className="w-20 h-20 rounded-full flex items-center justify-center text-white text-2xl font-semibold"
                    style={{ backgroundColor: getColor(selected.name) }}
                  >
                    {initials(selected.name)}
                  </div>
                </div>
              )}
              <div className="p-5 space-y-4">
                <DialogHeader>
                  <DialogTitle className="text-xl">{selected.name}</DialogTitle>
                  {extraFields?.map(f => selected[f.key] && (
                    <p key={f.key} className="text-sm text-muted-foreground">
                      {f.label}: {selected[f.key]}
                    </p>
                  ))}
                </DialogHeader>

                {selected.relationships.length > 0 && (
                  <div className="space-y-2 pt-2">
                    <p className="text-xs font-medium text-muted-foreground uppercase tracking-wider">
                      Relationships
                    </p>
                    <div className="space-y-2">
                      {selected.relationships.map((rel, i) => (
                        <div key={i} className="flex items-center gap-2 text-sm p-2 rounded-lg bg-muted/50">
                          <span className="text-muted-foreground capitalize text-xs min-w-[80px]">
                            {rel.rel.replace(/_/g, " ").toLowerCase()}
                          </span>
                          <span className="text-xs text-muted-foreground">→</span>
                          <span className="font-medium text-sm">{rel.target}</span>
                          <span className="text-[10px] px-1.5 py-0.5 rounded bg-muted text-muted-foreground ml-auto">
                            {rel.type}
                          </span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </>
          )}
        </DialogContent>
      </Dialog>
    </div>
  );
}
