from pathlib import Path
import pprint
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# External projects should import from the stable public package surface only.
import socialsense_core as ssc


def main():
    print("SocialSense Core version:", ssc.__version__)
    print("Available scenario packs:", ssc.list_scenario_packs())
    contract = ssc.run_scenario_pack("civic_policy_message")
    pprint.pp(
        {
            "summary": contract["summary"],
            "platform_breakdown": contract["platform_breakdown"],
            "runtime_mode": contract["runtime_mode"],
            "provenance_labels": contract["provenance_labels"],
        }
    )


if __name__ == "__main__":
    main()
