class HashSet:
    def __init__(self, iterable=None, comparer=None):
        self.data = {}
        self.comparer = comparer if comparer else lambda x, y: x == y
        if iterable:
            for item in iterable:
                self.add(item)

    def add(self, item):
        if not self.contains(item):
            self.data[item] = None

    def clear(self):
        self.data.clear()

    def contains(self, item):
        for key in self.data:
            if self.comparer(key, item):
                return True
        return False

    def copy_to(self, array, array_index):
        for i, item in enumerate(self.data.keys()):
            array[array_index + i] = item

    def remove(self, item):
        for key in list(self.data.keys()):
            if self.comparer(key, item):
                del self.data[key]
                return True
        return False


class TaskManager:
    """
        TaskManager - это класс для управления задачами.

        Методы:
        - add_task(task): Добавляет новую задачу.
        - remove_task(task): Удаляет задачу.
        - print_all_tasks(): Выводит все задачи и их статус.
        - mark_task_as_completed(task): Отмечает задачу как выполненную.
        - rename_task(old_task, new_task): Переименовывает задачу.
        - clear_all_tasks(): Очищает все задачи.
    """

    def add_task(self, task):
        self.tasks.add(task)
        print(f"Задание '{task}' добавлено")

    def remove_task(self, task):
        if self.tasks.contains(task):
            self.tasks.remove(task)
            self.completed_tasks.remove(task)
            print(f"Задание '{task}' удалено")
        else:
            print(f"Задание '{task}' не найдено")

    def print_all_tasks(self):
        if len(self.tasks) == 0:
            print("Нет заданий")
        else:
            print("Задания:")
            for task in self.tasks:
                status = "выполнено" if self.completed_tasks.contains(task) else "в процессе"
                print(f"- {task} ({status})")

    def mark_task_as_completed(self, task):
        if self.tasks.contains(task):
            self.completed_tasks.add(task)
            print(f"Задание '{task}' отмечено как выполненное")
        else:
            print(f"Задание '{task}' не найдено")

    def rename_task(self, old_task, new_task):
        if self.tasks.contains(old_task):
            self.tasks.remove(old_task)
            self.tasks.add(new_task)
            if self.completed_tasks.contains(old_task):
                self.completed_tasks.remove(old_task)
                self.completed_tasks.add(new_task)
            print(f"Задание '{old_task}' переименовано в '{new_task}'")
        else:
            print(f"Задание '{old_task}' не найдено")

    def clear_all_tasks(self):
        self.tasks.clear()
        self.completed_tasks.clear()
        print("Теперь список пуст")


task_manager = TaskManager()
while True:
    print("\nМенеджер задач")
    print("1. Добавить задачу")
    print("2. Удалить задачу")
    print("3. Показать все задачи")
    print("4. Отметить задачу как выполненную")
    print("5. Переименовать задачу")
    print("6. Очистить все задачи")
    print("7. Выход")
    choice = input("Введите ваш выбор: ")

    if choice == '1':
        task = input("Введите имя задачи: ")
        task_manager.add_task(task)
    elif choice == '2':
        task = input("Введите имя задачи для удаления: ")
        task_manager.remove_task(task)
    elif choice == '3':
        task_manager.print_all_tasks()
    elif choice == '4':
        task = input("Введите имя задачи для отметки как выполненной: ")
        task_manager.mark_task_as_completed(task)
    elif choice == '5':
        old_task = input("Введите старое имя задачи: ")
        new_task = input("Введите новое имя задачи: ")
        task_manager.rename_task(old_task, new_task)
    elif choice == '6':
        task_manager.clear_all_tasks()
    elif choice == '7':
        print("Выход...")
        break
    else:
        print("Такой задачи нет, попробуйте еще раз")
