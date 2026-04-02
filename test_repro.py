import pytest

# Suponiendo que existe una función get_stats en algún módulo Python
from src.tasks import get_stats  # Esta importación es hipotética

def test_get_stats_no_tasks():
    """get_stats debería manejar el caso de una lista vacía"""
    expected = {"total": 0, "completed": 0, "pending": 0, "completion_rate": 0.0}
    assert get_stats([]) == expected, "Debería resultar en estadísticas vacías"

if __name__ == "__main__":
    pytest.main(["-v", "--tb=short", "test_repro.py"])