from controller.task_controller import sum, add_task, division, Calculator
from flask import Flask, jsonify
import pytest

def test_sum():
    assert sum(2,2) == 4

def test_division():
    assert division(10,5) == 2

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(5, 0)

# Cuando se ejecuta division(5, 0) dentro del contexto de pytest.raises(ZeroDivisionError), se espera que la función division() lance una excepción ZeroDivisionError debido a la división por cero.
# Si la función division() no maneja correctamente esta excepción, la prueba fallará, ya que pytest.raises(ZeroDivisionError) espera que se produzca esta excepción, y si no ocurre, se considera un fallo.

class TestCalculator:
    def test_add(self):
        calculator = Calculator()
        assert calculator.add(2, 3) == 5

# PROBANDO EL CONTROLLADOR DE LA APLICACIÓN
# Define una prueba para agregar una tarea válida
def test_add_task_valid():
    app = Flask(__name__)

    with app.test_request_context(json={'text': 'Nueva tarea'}):
        response = add_task()
        assert response.status_code == 200
        assert 'id' in response.json
        assert response.json['text'] == 'Nueva tarea'


