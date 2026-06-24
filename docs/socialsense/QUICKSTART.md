# Quickstart

```bash
cd /Users/chawit/Projects/oasis-socialsense-research
python3 -m pytest tests/socialsense -q
python3 examples/socialsense_thai_platform_mix_demo.py
```

Minimal usage:

```python
from socialsense_core import SocialAction, SocialActor, SocialContent, RuntimeMode
from socialsense_core.simulation.context import SimulationContext
from socialsense_core.simulation.runner import run_simulation

context = SimulationContext.build(
    scenario="Synthetic LINE/Facebook campaign",
    actors=[SocialActor("a1", "Synthetic audience")],
    content=[SocialContent("c1", "Synthetic message")],
    platform_mix=["line", "facebook"],
    actions=[SocialAction("post", "a1", "c1"), SocialAction("share", "a1", "c1")],
    runtime_mode=RuntimeMode.RESEARCH,
)
result = run_simulation(context)
print(result.summary)
```
