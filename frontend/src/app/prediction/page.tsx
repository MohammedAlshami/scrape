"use client"

import HeroSlide from "./sections/HeroSlide"
import TocSlide from "./sections/TocSlide"
import HistoryTableSlide from "./sections/HistoryTableSlide"
import HistoryChartSlide from "./sections/HistoryChartSlide"
import ConstitutionalSlide from "./sections/ConstitutionalSlide"
import { ApprovalChartSlide, ParliamentSlide } from "./sections/DashboardSlide"
import GDPTrendSlide from "./sections/GDPTrendSlide"
import InflationTrendSlide from "./sections/InflationTrendSlide"
import CostOfLivingSlide from "./sections/CostOfLivingSlide"
import FuelPricesSlide from "./sections/FuelPricesSlide"
import { DebtDeficitSlide, SubsidyBurdenSlide } from "./sections/FiscalStressSlide"
import MajorPolicySlide from "./sections/MajorPolicySlide"
import PolicyShockSlide from "./sections/PolicyShockSlide"
import SalaryPressureSlide from "./sections/SalaryPressureSlide"
import CostReliefSlide from "./sections/CostReliefSlide"
import CoalitionStabilitySlide from "./sections/CoalitionStabilitySlide"
import LeadershipChallengeSlide from "./sections/LeadershipChallengeSlide"
import CabinetReshuffleSlide from "./sections/CabinetReshuffleSlide"
import ByElectionTrendSlide from "./sections/ByElectionTrendSlide"
import StateAlignmentSlide from "./sections/StateAlignmentSlide"
import PollAggregationSlide from "./sections/PollAggregationSlide"
import FloodsSlide from "./sections/FloodsSlide"
import ParliamentSessionsSlide from "./sections/ParliamentSessionsSlide"
import UnemploymentSlide from "./sections/UnemploymentSlide"
import { OPRSlide } from "./sections/MarketSlides"
import KlseSlide from "./sections/KlseSlide"
import RinggitSlide from "./sections/RinggitSlide"
import BrentSlide from "./sections/BrentSlide"
import ScenarioASlide from "./sections/ScenarioASlide"
import ScenarioBSlide from "./sections/ScenarioBSlide"
import ScenarioCSlide from "./sections/ScenarioCSlide"
import ScenarioDSlide from "./sections/ScenarioDSlide"
import ScenarioESlide from "./sections/ScenarioESlide"

export default function PredictionPage() {
  return (
    <div className="h-screen w-full overflow-y-scroll snap-y snap-mandatory">
      <HeroSlide />
      <TocSlide />
      <div id="slide-2"><HistoryTableSlide /></div>
      <div id="slide-3"><HistoryChartSlide /></div>
      <div id="slide-4"><ParliamentSlide /></div>
      <div id="slide-5"><ConstitutionalSlide /></div>
      <div id="slide-6"><ApprovalChartSlide /></div>
      <div id="slide-7"><GDPTrendSlide /></div>
      <div id="slide-8"><InflationTrendSlide /></div>
      <div id="slide-9"><CostOfLivingSlide /></div>
      <div id="slide-10"><FuelPricesSlide /></div>
      <div id="slide-11"><DebtDeficitSlide /></div>
      <div id="slide-12"><SubsidyBurdenSlide /></div>
      <MajorPolicySlide />
      <PolicyShockSlide />
      <SalaryPressureSlide />
      <CostReliefSlide />
      <CoalitionStabilitySlide />
      <LeadershipChallengeSlide />
      <CabinetReshuffleSlide />
      <ByElectionTrendSlide />
      <StateAlignmentSlide />
      <PollAggregationSlide />
      <FloodsSlide />
      <ParliamentSessionsSlide />
      <UnemploymentSlide />
      <OPRSlide />
      <KlseSlide />
      <RinggitSlide />
      <BrentSlide />
      <ScenarioASlide />
      <ScenarioBSlide />
      <ScenarioCSlide />
      <ScenarioDSlide />
      <ScenarioESlide />
    </div>
  )
}
