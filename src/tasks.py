VALID_PRIORITIES = ["low", "medium", "high"]

def get_pending_tasks(tasks: list) -> list:
    """Retorna solo las tareas no completadas, ordenadas por prioridad."""
    pending_tasks = [task for task in tasks if not task["completed"]]
    return sorted(pending_tasks, key=lambda x: VALID_PRIORITIES.index(x["priority"]), reverse=True)

def get_stats(tasks: list) -> dict:
    """Calcula estadísticas de la lista de tareas proporcionada."""
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed
    completion_rate = (completed / total) if total > 0 else 0.0
    return {"total": total, "completed": completed, "pending": pending, "completion_rate": completion_rate}