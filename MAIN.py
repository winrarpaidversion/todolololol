from BD import create_table, add_task, remove_task, get_todo_list

def show_menu():
    print("1. Показать список задач")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Выйти")

def show_todo_list():
    tasks = get_todo_list()
    print("Список задач:")
    for task in tasks:
        print(f"{task[0]}. {task[1]}")

def add_task():
    task = input("Введите новую задачу: ")
    add_task(task)
    print(f"Задача '{task}' добавлена в список.")

def remove_task():
    task_id = int(input("Введите номер задачи для удаления: "))
    remove_task(task_id)
    print(f"Задача с номером {task_id} удалена из списка.")

def main():
    create_table()

    while True:
        show_menu()
        choice = int(input("Выберите от 1-4"))
        try:
            match choice:
                case 1:
                    show_todo_list()
                case 2:
                    add_task()        
                case 3:
                    remove_task()
                case 4:
                    print("bye bye")
                    
        except choice > 4:
            print("Неправильное число")


if __name__ == "__main__":
    main()
