"""Tests existentes del task manager."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.tasks import create_task, get_pending_tasks, complete_task, get_stats


def test_create_task_valid():
    result = create_task("Comprar leche", "high", "2024-12-31")
    assert result["success"] is True
    assert result["task"]["title"] == "Comprar leche"


def test_create_task_empty_title():
    result = create_task("", "high", "2024-12-31")
    assert result["success"] is False


def test_create_task_invalid_priority():
    result = create_task("Test", "urgent", "2024-12-31")
    assert result["success"] is False


def test_complete_task():
    tasks = [{"title": "Test", "priority": "high", "completed": False}]
    result = complete_task(tasks, "Test")
    assert result["success"] is True
    assert tasks[0]["completed"] is True


def test_complete_task_not_found():
    tasks = []
    result = complete_task(tasks, "No existe")
    assert result["success"] is False
