from utils import load_tasks, save_tasks, show_tasks

def main():
    print('Добро пожаловать в  ваш персональный планировщик задач!')

    FILE_NAME = "tasks.txt"
    tasks = load_tasks()
  
    while True:
        print("\nГлавное меню:")
        print("1 — Показать все задачи")
        print("2 — Добавить задачу")
        print("3 — Отметить задачу выполненной")
        print("4 — Удалить задачу")
        print("5 — Выйти")
    
        choice = input("Выберите пункт меню: ")
        match choice:
            case "1":
                  if not tasks:
                      print("Список задач пуст!")
                  else:
                      show_tasks(tasks)
            case "2":
                """Добавляет новую задачу"""
                task = input("Введите новую задачу: ")
                if task.strip():
                    tasks.append(task.strip())
                    save_tasks(tasks)
                    print("Задача добавлена!")
                else:
                    print("Задача не может быть пустой!")
            case "3":
                """Отмечает задачу выполненной"""
                if not tasks:
                    print("Список задач пуст!")
                else:
                    show_tasks(tasks)
                    try:
                        task_num = int(input("\nВведите номер задачи для отметки: "))
                        if 1 <= task_num <= len(tasks):
                            if not tasks[task_num-1].startswith("[X] "):
                                tasks[task_num-1] = "[X] " + tasks[task_num-1]
                                save_tasks(tasks)
                                print("Задача отмечена выполненной!")
                            else:
                                print("Эта задача уже выполнена!")
                        else:
                            print("Неверный номер задачи!")
                    except ValueError:
                        print("Введите число!")
            case "4":
                """Удаляет задачу"""
                if not tasks:
                    print("Список задач пуст!")
                else:
                    show_tasks(tasks)
                    try:
                        task_num = int(input("\nВведите номер задачи для удаления: "))
                        if 1 <= task_num <= len(tasks):
                            deleted_task = tasks.pop(task_num-1)
                            save_tasks(tasks)
                            print(f"Задача '{deleted_task.replace('[X] ', '')}' удалена!")
                        else:
                            print("Неверный номер задачи!")
                    except ValueError:
                        print("Введите число!")
            case "5":
                print("До свидания! Ваши задачи сохранены.")
                break
            case _:
                print("Ошибка ввода. Попробуйте снова")
