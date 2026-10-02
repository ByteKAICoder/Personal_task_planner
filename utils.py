def load_tasks():
    """Загружает задачи из файла"""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Сохраняет задачи в файл"""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Показывает список задач"""
    if not tasks:
        print("Список задач пуст!")
        return
    print("\nСПИСОК ЗАДАЧ:")
    print("-" * 30)
    for i, task in enumerate(tasks, 1):
        if task.startswith("[X] "):
            status = "✓"
            task_text = task[4:]
        else:
            status = " "
            task_text = task
        print(f"{i}. [{status}] {task_text}")
