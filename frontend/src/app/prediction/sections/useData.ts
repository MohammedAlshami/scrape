"use client"

import { useState, useEffect } from "react"

export function useCsv<T>(url: string): T[] {
  const [data, setData] = useState<T[]>([])
  useEffect(() => {
    fetch(url)
      .then(r => r.text())
      .then(text => {
        const lines = text.trim().split("\n")
        if (lines.length < 2) return
        const headers = lines[0].split(",").map(h => h.trim())
        const rows = lines.slice(1).map(line => {
          const vals = line.split(",").map(v => v.trim())
          const obj: any = {}
          headers.forEach((h, i) => { obj[h] = vals[i] || "" })
          return obj
        })
        setData(rows as T[])
      })
      .catch(() => {})
  }, [url])
  return data
}

export type EconomyRow = {
  year: string; pm: string; election: string; polling_date: string; campaign_days: string
  winner: string; turnout_pct: string; registered: string; gdp_real: string
  inflation_pct: string; opr_pct: string; unemployment_pct: string; klse_dec: string
}

export type FiscalRow = {
  year: string; deficit_pct: string; debt_pct: string; subsidy_bn: string
}

export type FuelRow = {
  date: string; ron95: string; ron97: string; diesel: string
}
