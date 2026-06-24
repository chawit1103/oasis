from socialsense_core import RuntimeMode, SocialAction, SocialActor, SocialContent
from socialsense_core.simulation.context import SimulationContext
from socialsense_core.simulation.runner import run_simulation


def test_research_mode_supported_and_production_hooks_exist():
    research = SimulationContext.build("research", [SocialActor("a", "A")], [SocialContent("c", "C")], ["line"], [SocialAction("post", "a", "c")], runtime_mode="research")
    prod = SimulationContext.build("prod", [SocialActor("a", "A")], [SocialContent("c", "C")], ["line"], [SocialAction("post", "a", "c")], runtime_mode="production", governance_hooks={"policy": "downstream"})
    assert research.runtime_mode == RuntimeMode.RESEARCH
    result = run_simulation(prod)
    assert result.runtime_mode == RuntimeMode.PRODUCTION
    assert result.summary["governance_hooks_available"] is True
