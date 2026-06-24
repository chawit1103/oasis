from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from socialsense_core import SocialAction, SocialActor, SocialContent, ProvenanceLabel, RuntimeMode
from socialsense_core.simulation.context import SimulationContext
from socialsense_core.simulation.runner import run_simulation


def main():
    scenario = 'TikTok short-video discovery and creator affinity'
    platform_mix = ['tiktok']
    actions = [SocialAction('publish_video', "actor-1", "content-1", platform='tiktok'), SocialAction('watch_video', "actor-1", "content-1", platform='tiktok'), SocialAction('like_video', "actor-1", "content-1", platform='tiktok'), SocialAction('share_video', "actor-1", "content-1", platform='tiktok'), SocialAction('purchase_intent', "actor-1", "content-1", platform='tiktok')]
    context = SimulationContext.build(
        scenario=scenario,
        actors=[SocialActor("actor-1", "Synthetic Thai participant", traits={"country": "TH", "segment": "demo"})],
        content=[SocialContent("content-1", 'Synthetic short video message', author_id="source-1", topic="demo")],
        platform_mix=platform_mix,
        actions=actions,
        runtime_mode=RuntimeMode.RESEARCH,
        provenance_labels=(ProvenanceLabel.SYNTHETIC, ProvenanceLabel.MOCK),
    )
    result = run_simulation(context)
    print("input scenario:", result.scenario)
    print("platform mix:", result.summary["platform_mix"])
    print("actions simulated:", [event.action.action_type for event in result.event_log])
    print("event log:", [{"id": e.event_id, "action": e.action.action_type, "platform": e.action.platform} for e in result.event_log])
    print("result summary:", dict(result.summary))
    print("provenance labels:", [label.value for label in result.provenance_labels])
    print("runtime mode:", result.runtime_mode.value)


if __name__ == "__main__":
    main()
