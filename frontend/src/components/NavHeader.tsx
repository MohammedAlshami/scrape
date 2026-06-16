"use client"

import { usePathname } from "next/navigation"
import Link from "next/link"
import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuList,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu"

export function NavHeader() {
  const pathname = usePathname()
  if (pathname === "/prediction") return null
  return (
    <header className="bg-background/95 backdrop-blur sticky top-0 z-50">
      <div className="max-w-7xl mx-auto flex justify-center h-12">
        <NavigationMenu>
          <NavigationMenuList>
            {[
              ["/", "Graph"],
              ["/news", "News"],
              ["/people", "People"],
              ["/parties", "Parties"],
              ["/companies", "Companies"],
              ["/elections", "Elections"],
              ["/timeline", "Timeline"],
              ["/stats", "Stats"],
              ["/prediction", "Prediction"],
            ].map(([href, label]) => (
              <NavigationMenuItem key={href}>
                <Link href={href} className={navigationMenuTriggerStyle()}>{label}</Link>
              </NavigationMenuItem>
            ))}
          </NavigationMenuList>
        </NavigationMenu>
      </div>
    </header>
  )
}
