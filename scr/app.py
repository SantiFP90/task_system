# app.py
from flask import Flask, render_template
from routes.tasks import tasks_bp

app = Flask(__name__)

# Registrar blueprints
app.register_blueprint(tasks_bp)

# Ruta para la página de inicio
@app.route('/')
def index():
    # Ejemplo de lista de tareas (reemplaza con tu lógica real)
    tasks = [
        {'id': 1, 'text': 'Tarea 1'},
        {'id': 2, 'text': 'Tarea 2'},
        {'id': 3, 'text': 'Tarea 3'}
    ]
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
