from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from socialsense_core.adapters.civicsense_adapter import simulate_public_opinion


def main():
    result = simulate_public_opinion(
        message="Synthetic policy explainer",
        audience_profile={"name": "Synthetic Thai urban audience"},
        platform_mix=["line", "facebook", "tiktok"],
        scenario_context="demo only; no live platform data",
        runtime_mode="research",
    )
    print("input scenario:", result.scenario)
    print("platform mix:", result.summary["platform_mix"])
    print("actions simulated:", [e.action.action_type for e in result.event_log])
    print("event log:", [e.event_id for e in result.event_log])
    print("result summary:", dict(result.summary))
    print("provenance labels:", [p.value for p in result.provenance_labels])
    print("runtime mode:", result.runtime_mode.value)


if __name__ == "__main__":
    main()
