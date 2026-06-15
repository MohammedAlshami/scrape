"use client"

import * as React from "react"
import { Maximize2 } from "lucide-react"
import {
  Dialog,
  DialogContent,
} from "@/components/ui/dialog"
import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
  CardAction,
} from "@/components/ui/card"

export function ExpandableCard({
  title,
  description,
  children,
  className,
}: {
  title: string
  description?: string
  children: React.ReactNode
  className?: string
}) {
  const [open, setOpen] = React.useState(false)

  return (
    <>
      <Card className={className}>
        <CardHeader>
          <div className="flex items-center justify-between w-full">
            <div>
              <CardTitle>{title}</CardTitle>
              {description && <CardDescription>{description}</CardDescription>}
            </div>
            <CardAction>
              <Button variant="ghost" size="icon" className="h-7 w-7 shrink-0" onClick={() => setOpen(true)}>
                <Maximize2 className="h-3.5 w-3.5" />
              </Button>
            </CardAction>
          </div>
        </CardHeader>
        <CardContent>{children}</CardContent>
      </Card>

      <Dialog open={open} onOpenChange={setOpen}>
        <DialogContent className="!max-w-[95vw] !w-[95vw] !h-[90vh] chart-dialog [&_[data-slot=chart]]:!aspect-auto [&_[data-slot=chart]]:!flex-1 [&_[data-slot=chart]]:!h-full [&_.recharts-responsive-container]:!h-full">
          <div className="w-full h-full pt-6 flex flex-col">
            <h3 className="text-lg font-medium mb-4 shrink-0">{title}</h3>
            <div className="flex-1 min-h-0 w-full">
              <div className="w-full h-full">
                {children}
              </div>
            </div>
          </div>
        </DialogContent>
      </Dialog>
    </>
  )
}
