"use client"

import { LineChart, Line, BarChart, Bar, ComposedChart, AreaChart, Area, Treemap, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, PieChart, Pie, Cell, ReferenceLine } from "recharts"
import Timeline from "@mui/lab/Timeline"
import TimelineItem from "@mui/lab/TimelineItem"
import TimelineSeparator from "@mui/lab/TimelineSeparator"
import TimelineConnector from "@mui/lab/TimelineConnector"
import TimelineContent from "@mui/lab/TimelineContent"
import TimelineOppositeContent from "@mui/lab/TimelineOppositeContent"
import TimelineDot from "@mui/lab/TimelineDot"
import HowToVoteIcon from "@mui/icons-material/HowToVote"
import GroupIcon from "@mui/icons-material/Group"
import WarningIcon from "@mui/icons-material/Warning"
import AccountBalanceIcon from "@mui/icons-material/AccountBalance"
import EventIcon from "@mui/icons-material/Event"
import Typography from "@mui/material/Typography"
import { Maximize2, Calendar, CheckCircle, Clock, AlertTriangle } from "lucide-react"

import {
  Card, CardContent, CardDescription, CardHeader, CardTitle, CardAction,
} from "@/components/ui/card"
import {
  ChartContainer, ChartTooltip, ChartTooltipContent, type ChartConfig,
} from "@/components/ui/chart"
import { cn } from "@/lib/utils"
import { ExpandableCard } from "@/components/ui/expandable-chart"

export {
  LineChart, Line, BarChart, Bar, ComposedChart, AreaChart, Area, Treemap,
  XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, PieChart, Pie, Cell, ReferenceLine,
  Timeline, TimelineItem, TimelineSeparator, TimelineConnector,
  TimelineContent, TimelineOppositeContent, TimelineDot,
  HowToVoteIcon, GroupIcon, WarningIcon, AccountBalanceIcon, EventIcon, Typography,
  Maximize2, Calendar, CheckCircle, Clock, AlertTriangle,
  Card, CardContent, CardDescription, CardHeader, CardTitle, CardAction,
  ChartContainer, ChartTooltip, ChartTooltipContent, cn, ExpandableCard,
}
export type { ChartConfig }

export function StatCard({ title, value, subtitle, icon }: {
  title: string; value: string; subtitle?: string; icon: React.ReactNode
}) {
  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between pb-2">
        <CardTitle className="text-sm font-medium">{title}</CardTitle>
        {icon}
      </CardHeader>
      <CardContent>
        <div className="text-3xl font-bold">{value}</div>
        {subtitle && <p className="text-xs text-muted-foreground mt-1">{subtitle}</p>}
      </CardContent>
    </Card>
  )
}

export const TIMELINE_EVENTS = [
  { date: "Jul 2025", event: "Oust Anwar rally — 18,000 protest subsidy cuts", type: "political" },
  { date: "Feb 2026", event: "US-Iran war begins — oil spikes to $120+", type: "economic" },
  { date: "Mar 2026", event: "Hormuz blockade — fuel subsidy costs hit RM3.2bn/month", type: "economic" },
  { date: "Apr 2026", event: "14 BN assemblymen in N9 withdraw support for MB", type: "political" },
  { date: "May 2026", event: "Rafizi Ramli quits PKR, forms BERSAMA", type: "political" },
  { date: "Jun 2026", event: "PAS ends cooperation with BERSATU", type: "political" },
  { date: "Jul 2026", event: "Johor state election (PH vs BN competing)", type: "election" },
  { date: "Aug 2026", event: "Negeri Sembilan state election", type: "election" },
  { date: "Jul-Sep 2027", event: "★ RECOMMENDED WINDOW for GE16", type: "prediction" },
  { date: "Feb 2028", event: "Constitutional deadline for GE16", type: "deadline" },
]

export const EVENT_ICONS: Record<string, { icon: typeof HowToVoteIcon; color: string }> = {
  election: { icon: HowToVoteIcon, color: "#e74c3c" },
  political: { icon: GroupIcon, color: "#d35400" },
  economic: { icon: AccountBalanceIcon, color: "#27ae60" },
  prediction: { icon: HowToVoteIcon, color: "#2ecc71" },
  deadline: { icon: WarningIcon, color: "#2c3e50" },
  other: { icon: EventIcon, color: "#7f8c8d" },
}

export const APPROVAL_DATA = [
  { date: "Aug 2018", pm: "Mahathir", approval: 71, govt: 67 },
  { date: "Mar 2019", pm: "Mahathir", approval: 46, govt: 39 },
  { date: "Sep 2020", pm: "Muhyiddin", approval: 69, govt: null as number | null },
  { date: "Feb 2023", pm: "Anwar", approval: 68, govt: 54 },
  { date: "Nov 2023", pm: "Anwar", approval: 50, govt: null as number | null },
  { date: "Dec 2024", pm: "Anwar", approval: 54, govt: 51 },
  { date: "Jun 2025", pm: "Anwar", approval: 55, govt: 56 },
]

export const ECONOMY_DATA = [
  { year: "2019", gdp: 4.4, inflation: 0.7, unemployment: 3.3, opr: 3.0, klse: 1588 },
  { year: "2020", gdp: -5.6, inflation: -1.1, unemployment: 4.5, opr: 1.75, klse: 1627 },
  { year: "2021", gdp: 3.3, inflation: 2.5, unemployment: 4.6, opr: 1.75, klse: 1567 },
  { year: "2022", gdp: 8.7, inflation: 3.4, unemployment: 3.8, opr: 2.75, klse: 1495 },
  { year: "2023", gdp: 3.6, inflation: 2.5, unemployment: 3.4, opr: 3.0, klse: 1454 },
  { year: "2024", gdp: 5.1, inflation: 1.8, unemployment: 3.1, opr: 3.0, klse: 1625 },
  { year: "2025", gdp: 5.2, inflation: 1.2, unemployment: 3.0, opr: 2.75, klse: 1610 },
  { year: "2026e", gdp: 5.0, inflation: 2.0, unemployment: 2.9, opr: 2.75, klse: 1620 },
]

export const GDP_CONFIG = {
  gdp: { label: "GDP Growth %", color: "var(--chart-1)" },
  inflation: { label: "Inflation %", color: "var(--chart-2)" },
} satisfies ChartConfig

export const GE_DATA = [
  { ge: "GE1", year: 1959, dissolution: "27 Jun 1959", polling: "19 Aug 1959", campaignDays: 35, turnout: 73.3, seats: 104, winner: "Alliance", pm: "Tunku" },
  { ge: "GE2", year: 1964, dissolution: "2 Mar 1964", polling: "25 Apr 1964", campaignDays: 35, turnout: 80.0, seats: 159, winner: "Alliance", pm: "Tunku" },
  { ge: "GE3", year: 1969, dissolution: "20 Mar 1969", polling: "10 May 1969", campaignDays: 35, turnout: 73.6, seats: 144, winner: "Alliance", pm: "Tunku" },
  { ge: "GE4", year: 1974, dissolution: "31 Jul 1974", polling: "24 Aug 1974", campaignDays: 16, turnout: 75.0, seats: 154, winner: "BN", pm: "Razak" },
  { ge: "GE5", year: 1978, dissolution: "12 Jun 1978", polling: "8 Jul 1978", campaignDays: 17, turnout: 75.3, seats: 154, winner: "BN", pm: "Hussein" },
  { ge: "GE6", year: 1982, dissolution: "29 Mar 1982", polling: "22 Apr 1982", campaignDays: 15, turnout: 74.4, seats: 154, winner: "BN", pm: "Mahathir" },
  { ge: "GE7", year: 1986, dissolution: "19 Jul 1986", polling: "3 Aug 1986", campaignDays: 9, turnout: 70.0, seats: 177, winner: "BN", pm: "Mahathir" },
  { ge: "GE8", year: 1990, dissolution: "4 Oct 1990", polling: "21 Oct 1990", campaignDays: 9, turnout: 72.0, seats: 180, winner: "BN", pm: "Mahathir" },
  { ge: "GE9", year: 1995, dissolution: "6 Apr 1995", polling: "25 Apr 1995", campaignDays: 9, turnout: 68.0, seats: 192, winner: "BN", pm: "Mahathir" },
  { ge: "GE10", year: 1999, dissolution: "~10 Nov 1999", polling: "29 Nov 1999", campaignDays: 9, turnout: 71.2, seats: 193, winner: "BN", pm: "Mahathir" },
  { ge: "GE11", year: 2004, dissolution: "4 Mar 2004", polling: "21 Mar 2004", campaignDays: 8, turnout: 73.0, seats: 219, winner: "BN", pm: "Abdullah" },
  { ge: "GE12", year: 2008, dissolution: "13 Feb 2008", polling: "8 Mar 2008", campaignDays: 13, turnout: 75.4, seats: 222, winner: "BN", pm: "Abdullah" },
  { ge: "GE13", year: 2013, dissolution: "3 Apr 2013", polling: "5 May 2013", campaignDays: 15, turnout: 84.6, seats: 222, winner: "BN", pm: "Najib" },
  { ge: "GE14", year: 2018, dissolution: "7 Apr 2018", polling: "9 May 2018", campaignDays: 11, turnout: 82.3, seats: 222, winner: "PH", pm: "Najib" },
  { ge: "GE15", year: 2022, dissolution: "10 Oct 2022", polling: "19 Nov 2022", campaignDays: 14, turnout: 74.1, seats: 222, winner: "PH", pm: "Ismail Sabri" },
]

export const SEATS_DATA = [
  { name: "PH", seats: 77, fill: "#ED1C24" },
  { name: "PN", seats: 62, fill: "#031e61" },
  { name: "BN", seats: 30, fill: "#000080" },
  { name: "GPS", seats: 23, fill: "#FF6666" },
  { name: "GRS", seats: 5, fill: "#4682b4" },
  { name: "WARISAN", seats: 3, fill: "#A4E5FC" },
  { name: "Others", seats: 22, fill: "#888888" },
]
