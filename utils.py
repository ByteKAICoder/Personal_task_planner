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
