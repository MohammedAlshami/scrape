import type { Metadata } from "next";
import { Inter } from "next/font/google";
import Script from "next/script";
import Link from "next/link";
import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuList,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu";
import "./globals.css";

const inter = Inter({
  variable: "--font-sans",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Election Prediction",
  description: "Malaysian Election Knowledge Graph & News",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" className={`${inter.variable} h-full antialiased`}>
      <body className="min-h-full flex flex-col">
        {process.env.NODE_ENV === "development" && (
          <Script
            src="//unpkg.com/react-grab/dist/index.global.js"
            crossOrigin="anonymous"
            strategy="beforeInteractive"
          />
        )}
        <header className="bg-background/95 backdrop-blur sticky top-0 z-50">
          <div className="max-w-7xl mx-auto flex justify-center h-12">
            <NavigationMenu>
              <NavigationMenuList>
                <NavigationMenuItem>
                  <Link href="/" className={navigationMenuTriggerStyle()}>Graph</Link>
                </NavigationMenuItem>
                <NavigationMenuItem>
                  <Link href="/news" className={navigationMenuTriggerStyle()}>News</Link>
                </NavigationMenuItem>
                <NavigationMenuItem>
                  <Link href="/people" className={navigationMenuTriggerStyle()}>People</Link>
                </NavigationMenuItem>
                <NavigationMenuItem>
                  <Link href="/parties" className={navigationMenuTriggerStyle()}>Parties</Link>
                </NavigationMenuItem>
                <NavigationMenuItem>
                  <Link href="/companies" className={navigationMenuTriggerStyle()}>Companies</Link>
                </NavigationMenuItem>
                <NavigationMenuItem>
                  <Link href="/elections" className={navigationMenuTriggerStyle()}>Elections</Link>
                </NavigationMenuItem>
                <NavigationMenuItem>
                  <Link href="/timeline" className={navigationMenuTriggerStyle()}>Timeline</Link>
                </NavigationMenuItem>
                <NavigationMenuItem>
                  <Link href="/stats" className={navigationMenuTriggerStyle()}>Stats</Link>
                </NavigationMenuItem>
              </NavigationMenuList>
            </NavigationMenu>
          </div>
        </header>
        <main className="flex-1">{children}</main>
      </body>
    </html>
  );
}
