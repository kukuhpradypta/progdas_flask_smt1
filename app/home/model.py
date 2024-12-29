from abc import ABC, abstractmethod
from datetime import datetime

# Abstract class
class Task(ABC):
    def __init__(self, id, title, deadline, priority):
        self.id = id
        self.title = title
        self.deadline = deadline
        self.priority = priority

    @abstractmethod
    def display_task(self):
        pass

# Subclasses
class WorkTask(Task):
    def display_task(self):
        return f"[WORK] {self.title} | Deadline: {self.deadline} | Priority: {self.priority}"

class StudyTask(Task):
    def display_task(self):
        return f"[STUDY] {self.title} | Deadline: {self.deadline} | Priority: {self.priority}"

class RoutineTask(Task):
    def display_task(self):
        return f"[ROUTINE] {self.title} | Deadline: {self.deadline} | Priority: {self.priority}"

# Task Manager class
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.last_id = 0  # Untuk menyimpan ID terakhir

    def _generate_id(self):
        """Generate ID baru dengan increment dari ID terakhir."""
        self.last_id += 1
        return self.last_id

    def add_task(self, task):
        """Menambahkan task baru dengan ID auto-generate."""
        task.id = self._generate_id()  # Set ID untuk task baru
        self.tasks.append(task)

    def remove_task(self, task_id):
        """Menghapus task berdasarkan ID."""
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        if len(self.tasks) == initial_count:
            return False  # Task tidak ditemukan
        return True  # Task berhasil dihapus

    def get_all_tasks(self):
        """Mengembalikan semua tasks dalam bentuk list of dictionaries."""
        return [
            {
                "id": task.id,
                "category": task.__class__.__name__.replace("Task", ""),
                "title": task.title,
                "deadline": task.deadline,
                "priority": task.priority
            }
            for task in self.tasks
        ]

    def upcoming_tasks(self):
        """Mengembalikan tasks yang deadline-nya lebih dari waktu saat ini."""
        now = datetime.now()
        return [
            {
                "id": task.id,
                "category": task.__class__.__name__.replace("Task", ""), # untuk mendapatkan nama class lalu replace string Task dengan string kosong
                "title": task.title,
                "deadline": task.deadline,
                "priority": task.priority
            }
            for task in self.tasks if datetime.strptime(task.deadline, '%Y-%m-%d %H:%M') > now
        ]