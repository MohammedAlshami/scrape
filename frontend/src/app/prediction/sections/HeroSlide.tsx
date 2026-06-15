"use client"

export default function HeroSlide() {
  return (
    <section className="h-screen w-full flex flex-col items-center justify-center text-center px-4 snap-start">
      <h1 className="text-3xl md:text-5xl lg:text-6xl font-semibold tracking-tight mb-4">GE16 Election Timing Prediction</h1>
      <p className="text-muted-foreground text-sm md:text-lg max-w-2xl mx-auto leading-relaxed">
        Data-driven analysis of when Malaysia&apos;s 16th General Election will be called.
        Based on 310 data files across economic indicators, political history, polls, and timing factors.
      </p>
    </section>
  )
}
