import pytest
from src.tasks import get_stats

def test_get_stats_with_empty_list():
    expected_output = {"total": 0, "completed": 0, "pending": 0, "completion_rate": 0.0}
    assert get_stats([]) == expected_output
