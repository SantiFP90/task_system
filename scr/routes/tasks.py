from flask import Blueprint, jsonify, request
from controller.task_controller import get_tasks, add_task, update_task, update_task_text, delete_task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks_route():
    return get_tasks()

@tasks_bp.route('/tasks', methods=['POST'])
def add_task_route():
    return add_task()

@tasks_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task_route(id):
    return update_task(id)

@tasks_bp.route('/tasksText/<int:id>', methods=['PUT'])  # Nueva ruta para actualizar el texto de la tarea
def update_task_text_route(id):
    return update_task_text(id)

@tasks_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task_route(id):
    return delete_task(id)
