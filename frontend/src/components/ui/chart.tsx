"use client"

import * as React from "react"
import * as RechartsPrimitive from "recharts"

import { cn } from "@/lib/utils"

const ChartContext = React.createContext<{ config: ChartConfig } | null>(null)

function useChart() {
  const context = React.useContext(ChartContext)
  if (!context) throw new Error("Chart components must be used within a ChartContainer")
  return context
}

export type ChartConfig = Record<
  string,
  { label: string; color?: string }
>

function ChartContainer({
  config,
  children,
  className,
  ...props
}: React.ComponentProps<"div"> & { config: ChartConfig; children: React.ReactNode }) {
  const id = React.useId()
  return (
    <ChartContext.Provider value={{ config }}>
      <div
        id={id}
        data-slot="chart"
        className={cn(
          "flex aspect-video justify-center text-xs [&_.recharts-cartesian-axis-tick_text]:fill-muted-foreground [&_.recharts-cartesian-grid_line[stroke='#ccc']]:stroke-border/50 [&_.recharts-curve.recharts-tooltip-cursor]:stroke-border [&_.recharts-dot[stroke='#fff']]:stroke-transparent [&_.recharts-layer]:outline-hidden [&_.recharts-polar-grid_[stroke='#ccc']]:stroke-border [&_.recharts-radial-bar-background-sector]:fill-muted [&_.recharts-rectangle.recharts-tooltip-cursor]:fill-muted [&_.recharts-reference-line_[stroke='#ccc']]:stroke-border [&_.recharts-sector[stroke='#fff']]:stroke-transparent [&_.recharts-sector]:outline-hidden [&_.recharts-surface]:outline-hidden",
          className
        )}
        {...props}
      >
        <ChartStyle id={id} config={config} />
        <RechartsPrimitive.ResponsiveContainer>
          {children}
        </RechartsPrimitive.ResponsiveContainer>
      </div>
    </ChartContext.Provider>
  )
}

function ChartStyle({ id, config }: { id: string; config: ChartConfig }) {
  return (
    <style
      dangerouslySetInnerHTML={{
        __html: `
          #${id} {
            ${Object.entries(config)
              .filter(([, v]) => v.color)
              .map(([k, v]) => `--color-${k}: ${v.color};`)
              .join("\n")}
          }
        `,
      }}
    />
  )
}

const ChartTooltip = RechartsPrimitive.Tooltip

function ChartTooltipContent({
  className,
  indicator = "dot",
  ...props
}: React.ComponentProps<"div"> & { indicator?: "line" | "dot" }) {
  const { config } = useChart()
  const { active, payload } = props as any

  if (!active || !payload?.length) return null

  return (
    <div
      className={cn(
        "rounded-xl border bg-card px-3 py-2 text-sm shadow-sm",
        className
      )}
    >
      <div className="grid gap-1.5">
        {payload.map((item: any) => {
          const cfg = config[item.dataKey as string]
          return (
            <div key={item.dataKey} className="flex items-center gap-2">
              {indicator === "dot" && (
                <span
                  className="size-2 rounded-full"
                  style={{ backgroundColor: item.color }}
                />
              )}
              {indicator === "line" && (
                <span
                  className="w-4 h-0.5"
                  style={{ backgroundColor: item.color }}
                />
              )}
              <span className="text-muted-foreground">{cfg?.label || item.name}</span>
              <span className="font-medium tabular-nums">{item.value.toFixed(1)}%</span>
            </div>
          )
        })}
      </div>
    </div>
  )
}

export { ChartContainer, ChartTooltip, ChartTooltipContent }
