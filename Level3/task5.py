import os

class Task:
    def __init__(self, task_id, title, description):
        self.id = task_id
        self.title = title
        self.description = description

    def __str__(self):
        return f"{self.id},{self.title},{self.description}"

    @classmethod
    def from_string(cls, task_string):
        task_id, title, description = task_string.strip().split(',')
        return cls(int(task_id), title, description)

class TaskManager:
    def __init__(self, filename='tasks.txt'):
        self.tasks = []
        self.next_id = 1
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    for line in file:
                        task = Task.from_string(line)
                        self.tasks.append(task)
                        if task.id >= self.next_id:
                            self.next_id = task.id + 1
            print("Tasks loaded successfully.")
        except Exception as e:
            print(f"Error loading tasks: {e}")

    def save_tasks(self):
        try:
            with open(self.filename, 'w') as file:
                for task in self.tasks:
                    file.write(str(task) + '\n')
            print("Tasks saved successfully.")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def create_task(self, title, description):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        print("Task created successfully.")

    def read_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def update_task(self, task_id, new_title, new_description):
        for task in self.tasks:
            if task.id == task_id:
                task.title = new_title
                task.description = new_description
                self.save_tasks()
                print("Task updated successfully.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("Task deleted successfully.")
                return
        print("Task not found.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.create_task(title, description)
        elif choice == '2':
            task_manager.read_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to update: "))
                new_title = input("Enter new task title: ")
                new_description = input("Enter new task description: ")
                task_manager.update_task(task_id, new_title, new_description)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
