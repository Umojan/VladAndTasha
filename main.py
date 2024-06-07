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

    def __init__(self):
        self.tasks = HashSet()
        self.completed_tasks = HashSet()

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
