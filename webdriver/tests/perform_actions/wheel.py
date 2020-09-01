import pytest

from tests.perform_actions.support.refine import filter_dict, get_events
from tests.support.asserts import assert_move_to_coordinates


def test_wheel_scroll(session, test_actions_page, wheel_chain):
    div_point = { "x": 82, "y": 187}

    wheel_chain \
        .scroll(div_point["x"], div_point["y"], 5, 10, origin="viewport") \
        .perform()
    events = get_events(session)
    assert len(events) > 0
    event_types = [e["type"] for e in events]
    assert "wheel" in event_types
    for e in events:
        if e["type"] == "wheel":
            assert e["deltaX"] >= 5
            assert e["deltaY"] >= 10
            assert e["deltaZ"] == 0
