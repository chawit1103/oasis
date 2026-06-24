from socialsense_core.actions.types import SocialAction
from socialsense_core.events.event_log import EventLog
from socialsense_core.events.types import SocialEvent


def test_event_log_records_actions():
    log = EventLog()
    log.append(SocialEvent("evt-1", SocialAction("post", "a1", "c1")))
    assert len(log) == 1
    assert log.to_summary() == {"post": 1}
    assert log.by_action("post")[0].event_id == "evt-1"
