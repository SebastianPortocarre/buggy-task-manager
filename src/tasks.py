VALID_PRIORITIES = ["low", "medium", "high"]

def get_pending_tasks(tasks: list) -> list:
    """Retorna solo las tareas no completadas, ordenadas por prioridad."""
    pending_tasks = [task for task in tasks if not task["completed"]]
    return sorted(pending_tasks, key=lambda x: VALID_PRIORITIES.index(x["priority"]), reverse=True)