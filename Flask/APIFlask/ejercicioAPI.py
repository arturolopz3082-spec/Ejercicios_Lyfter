from flask import Flask, request, jsonify
import json

app = Flask(__name__)

FILE_NAME = 'tasks.json'

VALID_STATUSES = [
    "TO DO",
    "IN PROGRESS",
    "COMPLETED"
]


def read_file():
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            return json.load(file)

    except FileNotFoundError:
        with open(FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump([], file, indent=4)
        return []

    except json.decoder.JSONDecodeError:
        return []


def write_file(task_list):
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(
            task_list,
            file,
            ensure_ascii=False,
            indent=4
        )


def validate_task(request_json, validate_id=False):
    if not isinstance(request_json, dict):
        raise ValueError("The JSON body must be a dictionary")

    required_fields = [
        'title',
        'description',
        'status'
    ]

    if validate_id:
        required_fields.append('id')

    for field in required_fields:
        if field not in request_json:
            raise ValueError(f"{field} missing from the body")

    title = request_json['title']
    description = request_json['description']
    status = request_json['status']

    if not isinstance(title, str) or not title.strip():
        raise ValueError(
            "Title cannot be empty"
        )

    if not isinstance(description, str) or not description.strip():
        raise ValueError(
            "Description cannot be empty"
        )

    if not isinstance(status, str):
        raise ValueError(
            "Status must be a string"
        )

    status = status.upper()

    if status not in VALID_STATUSES:
        raise ValueError(
            f"Invalid status. It must be one of these: {VALID_STATUSES}"
        )

    if validate_id:
        task_id = request_json['id']

        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError(
                "The id must be an integer greater than zero"
            )

    return True


def id_exists(task_list, task_id):
    return any(
        task['id'] == task_id
        for task in task_list
    )


@app.route("/tasks", methods=['GET'])
def get_tasks():
    tasks = read_file()

    status_filter = request.args.get("status")

    if status_filter:
        status_filter = status_filter.upper()

        tasks = list(
            filter(
                lambda task: task['status'] == status_filter,
                tasks
            )
        )

    return jsonify(tasks), 200


@app.route("/tasks", methods=['POST'])
def create_task():
    tasks = read_file()
    request_body = request.get_json(silent=True)

    try:
        validate_task(
            request_body,
            validate_id=True
        )

        task_id = request_body['id']

        if id_exists(tasks, task_id):
            return jsonify({
                "error": "This id has already been registered"
            }), 400

        new_task = {
            "id": task_id,
            "title": request_body['title'],
            "description": request_body['description'],
            "status": request_body['status'].upper()
        }

        tasks.append(new_task)
        write_file(tasks)

        return jsonify(new_task), 201

    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 400


@app.route("/tasks/<int:task_id>", methods=['PUT'])
def update_task(task_id):
    tasks = read_file()
    request_body = request.get_json(silent=True)

    if not id_exists(tasks, task_id):
        return jsonify({
            "error": "The task id does not exist"
        }), 404

    try:
        validate_task(request_body)

        updated_task = {
            "title": request_body['title'],
            "description": request_body['description'],
            "status": request_body['status'].upper()
        }

        for task in tasks:
            if task['id'] == task_id:
                task.update(updated_task)

                write_file(tasks)

                return jsonify(task), 200

    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 400


@app.route("/tasks/<int:task_id>", methods=['DELETE'])
def delete_task(task_id):
    tasks = read_file()

    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)

            write_file(tasks)

            return jsonify({
                "message": "Task deleted successfully"
            }), 200

    return jsonify({
        "error": "The task id does not exist"
    }), 404


if __name__ == '__main__':
    app.run(
        host='localhost',
        debug=True
    )