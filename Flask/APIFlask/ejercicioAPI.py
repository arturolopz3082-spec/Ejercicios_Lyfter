from asyncio import tasks

from flask import Flask
from flask import request, jsonify, Response
import json

app = Flask(__name__)

FILE_NAME = 'tasks.json'

VALID_STATUSES = [
    "POR HACER",
    "EN PROGRESO",
    "COMPLETADA"
]

def read_file():
    try:
        with open(FILE_NAME, 'r', encoding='utf8') as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        tasks = { }
        with open(FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump([], file, indent=4)
            return []
    except json.decoder.JSONDecodeError:
        print("El archivo no tiene formato JSON")

def write_file(list_of_tasks):
    try:
        with open(FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump(list_of_tasks, file, ensure_ascii=False ,indent=4)
    except FileNotFoundError:
        print("El archivo no existe")
    except json.decoder.JSONDecodeError:
        print("El archivo no tiene formato JSON")


def validate_tasks(request_json):
    required_fields = ['Identificador', 'Titulo', 'Descripcion', 'Estado']

    if not isinstance(request_json, dict):
        raise ValueError("El json debe ser un diccionario")
    for field in required_fields:
        if field not in request_json:
            raise ValueError(f"{field} missing from the body")

    #obtener valores
    identifier = request_json['Identificador']
    title = request_json['Titulo']
    description = request_json['Descripcion']
    state = request_json['Estado'].upper()

    if not isinstance(identifier, int) or identifier <= 0:
        raise ValueError(
            "El identificador debe ser un número mayor a cero"
        )

    if not isinstance(title, str) or not title.strip():
        raise ValueError(
            "El titulo no puede estar vacío"
        )

    if not isinstance(description, str) or not description.strip():
        raise ValueError(
            "La descripción no puede estar vacía"
        )

    if state not in VALID_STATUSES:
        raise ValueError(
            f"Estado inválido. Debe ser algunos estados: {VALID_STATUSES}"
        )
    return identifier

def identifier_exist(task_list, identifier):
    return any(
        task['Identificador'] == identifier
        for task in task_list
    )
@app.route("/getTasks", methods=['GET'])
def get_tasks():
    filtered_states = read_file()
    state_filter = request.args.get("Estado")
    if state_filter:
        filtered_states = list(
            filter(lambda task: task["Estado"] == state_filter, filtered_states)
        )
    return jsonify(filtered_states), 200

@app.route("/createTask", methods=['POST'])
def create_task():
    tasks = read_file()
    request_body = request.json
    identifier = request_body['Identificador']
    try:
        if identifier_exist(tasks, identifier):
            return jsonify("Error este identificador ya fue registrado"), 400
        else:
            if validate_tasks(request_body):
                tasks.append(
                    {
                        "Identificador": request_body['Identificador'],
                        "Titulo": request_body['Titulo'],
                        "Descripcion": request_body['Descripcion'],
                        "Estado": request_body['Estado'].upper(),
                    }
                )
                write_file(tasks)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    return jsonify(f"Esto es lo registrado",request_body), 200

@app.route("/updateTask", methods=['PUT'])
def update_task():
    tasks = read_file()
    request_body = request.json
    identifier = request_body['Identificador']
    new_task = {
        "Identificador": request_body['Identificador'],
        "Titulo": request_body['Titulo'],
        "Descripcion": request_body['Descripcion'],
        "Estado": request_body['Estado'].upper(),
    }
    try:
        if identifier_exist(tasks, identifier):
            for task in tasks:
                if task['Identificador'] == identifier:
                    if validate_tasks(request_body):
                        task.update(new_task)
                        write_file(tasks)
                        return jsonify("El identificador ya fue actualizado"), 200
        else:
            return jsonify("Error este identificador no ha sido registrado"), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route("/deleteTask", methods=['DELETE'])
def delete_task():
    tasks = read_file()
    request_body = request.json
    identifier = request_body['Identificador']
    task_to_delete = {
        "Identificador": request_body['Identificador'],
        "Titulo": request_body['Titulo'],
        "Descripcion": request_body['Descripcion'],
        "Estado": request_body['Estado'].upper(),
    }
    try:
        if identifier_exist(tasks, identifier):
            if validate_tasks(request_body):
                tasks.remove(task_to_delete)
                write_file(tasks)
                return jsonify("Esta tarea ya fue borrada"), 200
        else:
            return jsonify("El identificador no existe"), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(host='localhost',debug=True)
