from socialsense_core import SocialAction, SocialActor, SocialContent
from socialsense_core.simulation.context import SimulationContext
from socialsense_core.simulation.runner import run_simulation


def test_simulation_runner_returns_deterministic_results():
    context = SimulationContext.build(
        scenario="deterministic",
        actors=[SocialActor("a1", "Actor")],
        content=[SocialContent("c1", "Message")],
        platform_mix=["line"],
        actions=[SocialAction("post", "a1", "c1"), SocialAction("share", "a1", "c1")],
    )
    r1 = run_simulation(context)
    r2 = run_simulation(context)
    assert [e.event_id for e in r1.event_log] == ["evt-0001", "evt-0002"]
    assert r1.summary == r2.summary
    assert r1.recommendation_signals == r2.recommendation_signals
