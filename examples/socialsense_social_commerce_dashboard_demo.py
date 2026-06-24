from pathlib import Path
import pprint
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from socialsense_core.scenario_packs import run_scenario_pack


def main():
    pprint.pp(run_scenario_pack("social_commerce_response"))


if __name__ == "__main__":
    main()
