from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Mapping

from socialsense_core.adapters.civicsense_adapter import (
    simulate_crisis_response,
    simulate_policy_message_diffusion,
)
from socialsense_core.adapters.dashboard_contract import to_dashboard_contract
from socialsense_core.adapters.threec_marketing_adapter import (
    simulate_brand_sentiment,
    simulate_campaign_response,
    simulate_social_commerce_response,
)
from socialsense_core.simulation.result import SimulationResult


@dataclass(frozen=True)
class ScenarioPack:
    key: str
    title: str
    consumer: str
    platform_preset: str
    runtime_mode: str
    synthetic: bool
    message: str
    audience_profile: Mapping[str, str]
    scenario_context: str
    runner: Callable[["ScenarioPack"], SimulationResult]
    product_context: str | None = None

    def run(self) -> SimulationResult:
        return self.runner(self)


def _run_civic_policy(pack: ScenarioPack) -> SimulationResult:
    return simulate_policy_message_diffusion(
        pack.message,
        pack.audience_profile,
        platform_mix=pack.platform_preset,
        scenario_context=pack.scenario_context,
        runtime_mode=pack.runtime_mode,
    )


def _run_civic_crisis(pack: ScenarioPack) -> SimulationResult:
    return simulate_crisis_response(
        pack.message,
        pack.audience_profile,
        platform_mix=pack.platform_preset,
        scenario_context=pack.scenario_context,
        runtime_mode=pack.runtime_mode,
    )


def _run_marketing_campaign(pack: ScenarioPack) -> SimulationResult:
    return simulate_campaign_response(
        pack.message,
        pack.product_context or "synthetic product",
        pack.audience_profile,
        platform_mix=pack.platform_preset,
        runtime_mode=pack.runtime_mode,
    )


def _run_brand_sentiment(pack: ScenarioPack) -> SimulationResult:
    return simulate_brand_sentiment(
        pack.message,
        pack.audience_profile,
        platform_mix=pack.platform_preset,
        runtime_mode=pack.runtime_mode,
    )


def _run_social_commerce(pack: ScenarioPack) -> SimulationResult:
    return simulate_social_commerce_response(
        pack.message,
        pack.product_context or "synthetic offer",
        pack.audience_profile,
        platform_mix=pack.platform_preset,
        runtime_mode=pack.runtime_mode,
    )


SCENARIO_PACKS: dict[str, ScenarioPack] = {
    "civic_policy_message": ScenarioPack(
        key="civic_policy_message",
        title="Thai civic policy message diffusion",
        consumer="CivicSense",
        platform_preset="civic_default_thailand",
        runtime_mode="research",
        synthetic=True,
        message="Synthetic public-policy explainer with local context, trade-offs, and participation window.",
        audience_profile={"name": "Synthetic Thai civic audience", "country": "TH", "segment": "mixed public service users"},
        scenario_context="policy message diffusion dashboard contract demo",
        runner=_run_civic_policy,
    ),
    "civic_crisis_response": ScenarioPack(
        key="civic_crisis_response",
        title="Thai civic crisis response tabletop",
        consumer="CivicSense",
        platform_preset="crisis_default_thailand",
        runtime_mode="research",
        synthetic=True,
        message="Synthetic crisis update with official response, rumor correction, and community forwarding behavior.",
        audience_profile={"name": "Synthetic Thai crisis audience", "country": "TH", "segment": "family and workplace groups"},
        scenario_context="crisis response dashboard contract demo",
        runner=_run_civic_crisis,
    ),
    "threec_marketing_campaign": ScenarioPack(
        key="threec_marketing_campaign",
        title="Thai 3C marketing campaign response",
        consumer="3C Marketing Simulator",
        platform_preset="marketing_default_thailand",
        runtime_mode="research",
        synthetic=True,
        message="Synthetic creator-led campaign with short video discovery, social proof, and conversion intent.",
        product_context="mock consumer product bundle; synthetic SKU only",
        audience_profile={"name": "Synthetic Thai shoppers", "country": "TH", "segment": "value-seeking households"},
        scenario_context="marketing campaign dashboard contract demo",
        runner=_run_marketing_campaign,
    ),
    "threec_brand_sentiment": ScenarioPack(
        key="threec_brand_sentiment",
        title="Thai 3C brand sentiment tracking",
        consumer="3C Marketing Simulator",
        platform_preset="marketing_default_thailand",
        runtime_mode="research",
        synthetic=True,
        message="Synthetic brand message designed to test comment, creator, and trust response signals.",
        product_context="mock brand narrative; synthetic data only",
        audience_profile={"name": "Synthetic Thai brand audience", "country": "TH", "segment": "category-aware buyers"},
        scenario_context="brand sentiment dashboard contract demo",
        runner=_run_brand_sentiment,
    ),
    "social_commerce_response": ScenarioPack(
        key="social_commerce_response",
        title="Thai social commerce response",
        consumer="3C Marketing Simulator",
        platform_preset="commerce_default_thailand",
        runtime_mode="research",
        synthetic=True,
        message="Synthetic social-commerce offer with review prompt, platform sharing, and purchase-intent response.",
        product_context="mock commerce offer; no real inventory or payment flow",
        audience_profile={"name": "Synthetic Thai social-commerce shoppers", "country": "TH", "segment": "mobile-first deal seekers"},
        scenario_context="social commerce dashboard contract demo",
        runner=_run_social_commerce,
    ),
}


def list_scenario_packs() -> tuple[str, ...]:
    return tuple(sorted(SCENARIO_PACKS))


def get_scenario_pack(key: str) -> ScenarioPack:
    return SCENARIO_PACKS[key]


def run_scenario_pack(key: str) -> dict:
    pack = get_scenario_pack(key)
    result = pack.run()
    return to_dashboard_contract(result, scenario_key=pack.key, consumer=pack.consumer)
