class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def display(self):
        status = "Completed" if self.completed else "Pending"
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Status: {status}")