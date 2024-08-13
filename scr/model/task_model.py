class Task:
    def __init__(self, id, text, completed=False):
        self.id = id
        self.text = text
        self.completed = completed

    def to_dict(self):
        return {'id': self.id, 'text': self.text, 'completed': self.completed}