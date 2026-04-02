import pytest
from src.tasks import get_pending_tasks

def test_get_pending_tasks_order():
    tasks = [
        {"title": "A", "priority": "low", "completed": False},
        {"title": "B", "priority": "high", "completed": False},
    ]
    result = get_pending_tasks(tasks)
    assert result[0]["title"] == "B", "Tasks should be sorted with 'high' priority first"

if __name__ == "__main__":
    pytest.main()