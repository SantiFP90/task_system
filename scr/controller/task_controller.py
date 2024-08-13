from flask import request, jsonify
from model.task_model import Task

tasks = [
    Task(1, 'Tarea 1'),
    Task(2, 'Tarea 2', completed=True),
    Task(3, 'Tarea 3')
]

def get_tasks():
    return jsonify([task.to_dict() for task in tasks])

def add_task():
    data = request.json
    text = data.get('text')
    if text:
        task = Task(len(tasks) + 1, text)
        tasks.append(task)
        return jsonify(task.to_dict())
    else:
        return jsonify({'error': 'Invalid task text'}), 400

def update_task(id):
    data = request.json
    completed = data.get('completed')
    if 0 < id <= len(tasks):
        tasks[id - 1].completed = completed
        return jsonify(tasks[id - 1].to_dict())
    else:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    
def delete_task(id):
    if 0 < id <= len(tasks):
        deleted_task = tasks.pop(id - 1)
        return jsonify(deleted_task.to_dict())
    else:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    
def update_task_text(id):
    print("soy el id", id)
    data = request.json
    text = data.get('text')
    print(text)
    if 0 < id <= len(tasks):
        tasks[id - 1].text = text  # Actualiza el texto de la tarea
        return jsonify(tasks[id - 1].to_dict())
    else:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    
#PRUEBAS UNITARIAS
def sum(a,b):
    return a+b
def division(a,b):
    return a/b
class Calculator:
    def add(self, a, b):
        return a + b
