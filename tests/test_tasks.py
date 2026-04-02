"""Tests existentes del task manager."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.tasks import create_task, get_pending_tasks


def test_create_task_valid():
    result = create_task("Comprar leche", "high", "2024-12-31")
    assert result["success"] is True
    assert result["task"]["title"] == "Comprar leche"


def test_create_task_empty_title():
    result = create_task("", "high", "2024-12-31")
    assert result["success"] is False


def test_create_task_invalid_priority():
    result = create_task("Comprar leche", "very high", "2024-12-31")
    assert result["success"] is False


def test_create_task_invalid_date_format():
    result = create_task("Comprar leche", "high", "31-12-2024")
    assert result["success"] is False

