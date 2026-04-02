from datetime import datetime

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

    # Cambio de formato de fecha al correcto '%Y-%m-%d'
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
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
    pending_tasks = [task for task in tasks if not task["completed"]]
    return sorted(pending_tasks, key=lambda x: VALID_PRIORITIES.index(x["priority"]))
