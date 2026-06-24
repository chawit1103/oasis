from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from socialsense_core.adapters.civicsense_adapter import demo_public_opinion_scenarios, simulate_public_opinion


def main():
    scenario = demo_public_opinion_scenarios()[0]
    result = simulate_public_opinion(
        message=scenario["message"],
        audience_profile=scenario["audience_profile"],
        platform_mix=scenario["platform_preset"],
        scenario_context=scenario["scenario_context"],
        runtime_mode="research",
    )
    print("input scenario:", scenario["title"], "—", result.scenario)
    print("platform mix:", result.summary["platform_mix"])
    print("actions simulated:", [e.action.action_type for e in result.event_log])
    print("event log:", [e.event_id for e in result.event_log])
    print("result summary:", dict(result.summary))
    print("headline metrics:", result.summary["headline_metrics"])
    print("dashboard series:", result.summary["series"])
    print("provenance labels:", [p.value for p in result.provenance_labels])
    print("runtime mode:", result.runtime_mode.value)


if __name__ == "__main__":
    main()
