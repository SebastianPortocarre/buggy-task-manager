"""
Task Manager — módulo principal
"""
from datetime import datetime


# Prioridades válidas
VALID_PRIORITIES = ["low", "medium", "high"]


def create_task(title: str, priority: str, due_date: str) -> dict:
    """
    Crea una nueva tarea.

    Args:
        title: Título de la tarea (no puede estar vacío)
        priority: "low", "medium" o "high"
        due_date: Fecha en formato "YYYY-MM-DD"

    Returns:
        {"success": True, "task": {...}} o {"success": False, "error": "..."}
    """
    if not title or not title.strip():
        return {"success": False, "error": "El título no puede estar vacío"}

    if priority not in VALID_PRIORITIES:
        return {"success": False, "error": f"Prioridad inválida: {priority}"}

    # BUG 1: La fecha se valida con el formato incorrecto.
    # Se usa "%d-%m-%Y" pero el contrato dice "YYYY-MM-DD" ("%Y-%m-%d").
    # Ej: "2024-12-31" es válido según el contrato pero lanza ValueError aquí.
    try:
        datetime.strptime(due_date, "%d-%m-%Y")
    except ValueError:
        return {"success": False, "error": "Formato de fecha inválido. Usa YYYY-MM-DD"}

    return {
        "success": True,
        "task": {
            "title": title.strip(),
            "priority": priority,
            "due_date": due_date,
            "completed": False,
            "created_at": datetime.now().isoformat()
        }
    }


def get_pending_tasks(tasks: list) -> list:
    """Retorna solo las tareas no completadas, ordenadas por prioridad."""
    priority_order = {"high": 0, "medium": 1, "low": 2}

    pending = [t for t in tasks if not t["completed"]]

    # BUG 2: sorted() con reverse=True ordena de mayor a menor número,
    # pero priority_order mapea high=0, medium=1, low=2.
    # Con reverse=True, "low" (2) queda primero y "high" (0) queda último.
    # Debería ser reverse=False para que high (0) quede primero.
    return sorted(pending, key=lambda t: priority_order[t["priority"]], reverse=True)


def complete_task(tasks: list, title: str) -> dict:
    """Marca una tarea como completada por su título."""
    for task in tasks:
        if task["title"] == title:
            task["completed"] = True
            return {"success": True}

    return {"success": False, "error": f"Tarea '{title}' no encontrada"}


def get_stats(tasks: list) -> dict:
    """Retorna estadísticas de las tareas."""
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed

    # BUG 3: División por cero cuando no hay tareas.
    # Si total == 0, esta línea lanza ZeroDivisionError.
    completion_rate = completed / total * 100

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "completion_rate": round(completion_rate, 1)
    }
