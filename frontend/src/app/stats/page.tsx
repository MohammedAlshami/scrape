"use client"

import { useState, useEffect } from "react"
import { TrendingUp } from "lucide-react"
import { CartesianGrid, LabelList, Line, LineChart, XAxis, YAxis } from "recharts"

import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import {
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
  type ChartConfig,
} from "@/components/ui/chart"
import { cn } from "@/lib/utils"

interface InflationData {
  year: number
  inflation: number
}

interface Term {
  id: string
  label: string
  years: number[]
  period: string
}

const ALL_TERM = { id: "all", label: "All", period: "1999 \u2013 present" }

export default function StatsPage() {
  const [terms, setTerms] = useState<Term[]>([])
  const [activeTerm, setActiveTerm] = useState<string>("all")
  const [allData, setAllData] = useState<InflationData[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch("/data/inflation.json")
      .then((r) => r.json())
      .then((res) => {
        setTerms(res.terms)
        setAllData(res.data)
        setLoading(false)
      })
  }, [])

  const data = activeTerm === "all"
    ? allData
    : allData.filter((d) => terms.find((t) => t.id === activeTerm)?.years.includes(d.year)) ?? []

  const currentTerm = activeTerm === "all" ? ALL_TERM : terms.find((t) => t.id === activeTerm)

  const chartConfig = {
    inflation: {
      label: "Inflation",
      color: "var(--chart-1)",
    },
  } satisfies ChartConfig

  const avgInflation =
    data.length > 0
      ? (data.reduce((sum, d) => sum + d.inflation, 0) / data.length).toFixed(1)
      : "—"

  const trend = data.length >= 2
    ? data[data.length - 1].inflation - data[0].inflation
    : 0

  return (
    <div className="max-w-5xl mx-auto px-4 pt-10 pb-20">
      <div className="text-center mb-12">
        <h1 className="heading-lg mb-3">Economic Stats</h1>
        <p className="text-muted-foreground text-lg">
          Malaysia inflation rate by election term &mdash; data from DOSM
        </p>
      </div>

      <div className="flex flex-wrap justify-center gap-2 mb-10">
        <button
          onClick={() => setActiveTerm("all")}
          className={cn(
            "px-4 py-2 rounded-full text-sm font-medium transition-colors",
            activeTerm === "all"
              ? "bg-foreground text-background"
              : "bg-secondary text-secondary-foreground hover:bg-secondary/80"
          )}
        >
          All
          <span className="ml-1.5 text-xs opacity-60">1999 &ndash; present</span>
        </button>
        {terms.map((term) => (
          <button
            key={term.id}
            onClick={() => setActiveTerm(term.id)}
            className={cn(
              "px-4 py-2 rounded-full text-sm font-medium transition-colors",
              activeTerm === term.id
                ? "bg-foreground text-background"
                : "bg-secondary text-secondary-foreground hover:bg-secondary/80"
            )}
          >
            {term.label}
            <span className="ml-1.5 text-xs opacity-60">{term.period}</span>
          </button>
        ))}
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Inflation Rate</CardTitle>
          <CardDescription>
            Annual CPI inflation &mdash; {currentTerm?.label} ({currentTerm?.period})
          </CardDescription>
        </CardHeader>
        <CardContent>
          {loading ? (
            <div className="flex items-center justify-center h-64 text-muted-foreground">
              Loading...
            </div>
          ) : (
            <ChartContainer config={chartConfig}>
              <LineChart
                accessibilityLayer
                data={data}
                margin={{ top: 20, left: 12, right: 12 }}
              >
                <CartesianGrid vertical={false} />
                <XAxis
                  dataKey="year"
                  tickLine={false}
                  axisLine={false}
                  tickMargin={8}
                  tickFormatter={(value) => String(value)}
                />
                <YAxis
                  tickLine={false}
                  axisLine={false}
                  tickMargin={8}
                  tickFormatter={(value) => `${value}%`}
                />
                <ChartTooltip
                  cursor={false}
                  content={<ChartTooltipContent indicator="line" />}
                />
                <Line
                  dataKey="inflation"
                  type="natural"
                  stroke="var(--color-inflation)"
                  strokeWidth={2}
                  dot={{ fill: "var(--color-inflation)" }}
                  activeDot={{ r: 6 }}
                >
                  <LabelList
                    position="top"
                    offset={12}
                    className="fill-foreground"
                    fontSize={12}
                    formatter={(value) => `${value}%`}
                  />
                </Line>
              </LineChart>
            </ChartContainer>
          )}
        </CardContent>
        <CardFooter className="flex-col items-start gap-2 text-sm">
          <div className="flex gap-2 leading-none font-medium">
            {trend >= 0 ? (
              <>
                Inflation trending up by {Math.abs(trend).toFixed(1)}pp over term
                <TrendingUp className="h-4 w-4" />
              </>
            ) : (
              <>
                Inflation trending down by {Math.abs(trend).toFixed(1)}pp over term
                <TrendingUp className="h-4 w-4 rotate-180" />
              </>
            )}
          </div>
          <div className="leading-none text-muted-foreground">
            Average {avgInflation}% &mdash; Source: DOSM Consumer Price Index
          </div>
        </CardFooter>
      </Card>
    </div>
  )
}
