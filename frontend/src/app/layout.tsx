import type { Metadata } from "next";
import { Inter } from "next/font/google";
import Script from "next/script";
import { NavHeader } from "@/components/NavHeader";
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
        <NavHeader />
        <main className="flex-1">{children}</main>
      </body>
    </html>
  );
}
