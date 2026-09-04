import psycopg2
from psycopg2.errorcodes import UNIQUE_VIOLATION
from psycopg2.errors import UniqueViolation

from Python_Basics.Student_Control_System import data
from db import PgManager, validate_state, validate_fields_user, validate_fields_car, validate_fields_rentals
from flask import Flask
from flask import request, jsonify, Response
import datetime
import json

app = Flask(__name__)
pg_manager = PgManager(
    db_name = "postgres",
    host = "localhost",
    user = "postgres",
    password = "user"
)

user_states = [
    "activo", "inactivo", "suspendido"
]
car_states = [
    "disponible", "alquilado", "mantenimiento", "fuera_de_servicio"
]

rental_states = [
    "activo", "finalizado", "cancelado"
]

@app.route("/user/", methods=["GET"])
def get_user():
    try:
        users = pg_manager.execute_query("SELECT * FROM lyfter_car_rental.usuarios")
        name_filter = request.args.get("name")
        if name_filter:
            users = list(filter(lambda x: x[1] == name_filter, users))
            return jsonify(users), 200
        else:
            return jsonify(users), 200
    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route("/user/", methods=["POST"])
def post_user():
    try:
        validate_fields_user(request.json)
        data = request.get_json()
        users = pg_manager.execute_query("SELECT * FROM lyfter_car_rental.usuarios")
        max_int = pg_manager.execute_query("SELECT MAX(id) FROM lyfter_car_rental.usuarios")
        if data not in users:
            validate_state(user_states, data["state_account"])
            pg_manager.execute_query(
                f"insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account ) "
                f"values ('{(max_int[0][0]) + 1}','{data['first_name']}', '{data['last_name']}', '{data["email"]}', '{data['email']}', '{data['password']}', '{data['birthdate']}', '{data['state_account']}')")
            return jsonify("se guardó la información en la base de datos"), 200
        else:
            return jsonify("esa data ya existe en la base de datos"), 200
    except UniqueViolation:
        return jsonify({"error": "El email ya se encuentra registrado en la base de datos"})
    except ValueError as e:
        return jsonify({"error": str(e)}),400
    except TypeError as e:
        return jsonify({"error": str(e)}),400
    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route("/user/<id>", methods=["PUT"])
def update_user(id):
    user = pg_manager.execute_query("SELECT * FROM lyfter_car_rental.usuarios WHERE id = %s", (id,))
    data = request.get_json()
    try:
        validate_state(user_states, data["state_account"])
        validate_fields_user(request.json)
        pg_manager.execute_query(f"UPDATE lyfter_car_rental.usuarios "
                                 f"SET first_name = '{request.json.get('first_name')}',"
                                 f"last_name = '{request.json.get('last_name')}',"
                                 f"email = '{request.json.get('email')}',"
                                 f"username = '{request.json.get('username')}',"
                                 f"password = '{request.json.get('password')}',"
                                 f"birthdate = '{request.json.get('birthdate')}',"
                                 f"state_account = '{request.json.get('state_account')}'"
                                 f"WHERE id = {id}")
        return jsonify(f"se actualizó la data en la bd {user}"), 200
    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 500
    except TypeError as e:
        return jsonify({"error": str(e)}),400
    except ValueError as e:
        return jsonify({"error": str(e)}),400

@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        if pg_manager.execute_query("SELECT * FROM lyfter_car_rental.usuarios WHERE id = %s", (id,)):
            pg_manager.execute_query(f"DELETE FROM lyfter_car_rental.usuarios "
                                     f"WHERE id = {id}")
            return jsonify({"message":"se borró al usuario de la base de datos"}), 200
        else:
            return jsonify({"message":"no se puede borrar, no existe en la base de datos"}), 404
    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 500
    except TypeError as e:
        return jsonify({"error": str(e)}),400
    except ValueError as e:
        return jsonify({"error": str(e)}),400


@app.route("/car/", methods=["GET"])
def get_car():
    try:
        cars = pg_manager.execute_query("SELECT * FROM lyfter_car_rental.automoviles")
        model_filter = request.args.get("model")
        if model_filter:
            cars = list(filter(lambda x: x[1] == model_filter, cars))
            return jsonify(cars), 200
        else:
            return jsonify(cars)
    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route("/car/", methods=["POST"])
def post_car():
    try:
        validate_fields_car(request.json)
        data = request.get_json()
        cars = pg_manager.execute_query("SELECT * FROM lyfter_car_rental.automoviles;")
        max_int = pg_manager.execute_query("SELECT MAX(id) FROM lyfter_car_rental.automoviles;")
        query = (f"INSERT INTO lyfter_car_rental.automoviles(id,make, model, fabrication_year, state) "
                 f"values ( '{max_int[0][0]+1}' ,'{data['make']}', '{data['model']}', '{data['fabrication_year']}' ,'{data['state']}');")
        if data not in cars:
            validate_state(car_states, data["state"])
            pg_manager.execute_query(query)
            print("INSERT TERMINADO")
            return jsonify(f"se guardó la información en la base de datos: {max_int[0][0]+1} {data}"), 200
        else:
            return jsonify("esa data ya existe en la base de datos"), 200
    except UniqueViolation:
        return jsonify({"error": "El dato ya se encuentra registrado en la base de datos"})
    except ValueError as e:
        return jsonify({"error": str(e)}),400
    except TypeError as e:
        return jsonify({"error": str(e)}),400
    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route("/car/<id>", methods=["PUT"])
def put_car(id):
    car = pg_manager.execute_query(f"SELECT * FROM lyfter_car_rental.automoviles WHERE id = {id}")
    data = request.get_json()
    try:
        validate_state(car_states, data["state"])
        validate_fields_car(request.json)
        pg_manager.execute_query(f"UPDATE lyfter_car_rental.automoviles "
                                 f"SET make = '{request.json.get('make')}',"
                                 f"model = '{request.json.get('model')}',"
                                 f"fabrication_year = {request.json.get('fabrication_year')}, "
                                 f"state = '{request.json.get('state')}'"
                                 f"WHERE id = {id};")
        return jsonify(f"se actualizó la data en la bd {car}"), 200
    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 500
    except TypeError as e:
        return jsonify({"error": str(e)}),400
    except ValueError as e:
        return jsonify({"error": str(e)}),400

@app.route("/car/<id>", methods=["DELETE"])
def delete_car(id):
    try:
        if pg_manager.execute_query(f"SELECT * FROM lyfter_car_rental.automoviles WHERE id = {id}"):
            pg_manager.execute_query(f"DELETE FROM lyfter_car_rental.automoviles "
                                     f"WHERE id = {id}")
            return jsonify({"message":"se borró el carro de la base de datos"}), 200
        else:
            return jsonify({"error": "no existe en la base de datos"}), 404
    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 500
    except TypeError as e:
        return jsonify({"error": str(e)}),400
    except ValueError as e:
        return jsonify({"error": str(e)}),400


@app.route("/rental/", methods=["GET"])
def get_rental():
    try:
        rentals = pg_manager.execute_query(
            "SELECT * FROM lyfter_car_rental.alquiler"
        )
        state_filter = request.args.get("state")
        if state_filter:
            rentals = list(filter(lambda x: x[1] == state_filter, rentals))
            return jsonify(rentals), 200
        else:
            return jsonify(rentals), 200
    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route("/rental/", methods=["POST"])
def post_rental():
    try:
        validate_fields_rentals(request.json)
        validate_state(rental_states, request.json["rental_state"])
        data = request.get_json()
        rentals = pg_manager.execute_query("SELECT * FROM lyfter_car_rental.alquiler;")
        max_int = pg_manager.execute_query("SELECT MAX(id) FROM lyfter_car_rental.alquiler;")
        query = (f"INSERT INTO lyfter_car_rental.alquiler "
                 f"values ('{max_int[0][0] + 1}' ,'{data['user_id']}','{data['car_id']}',"
                 f"'{data['rental_date']}', '{data['rental_state']}');")
        if data not in rentals:
            pg_manager.execute_query(query)
            print("INSERT TERMINADO")
            return jsonify("se ingresó en la base de datos"), 200
        else:
            return jsonify({"error": " existe en la base de datos"}), 404
    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 500
    except TypeError as e:
        return jsonify({"error": str(e)}),400
    except ValueError as e:
        return jsonify({"error": str(e)}),400

@app.route("/rental/<id>", methods=["PUT"])
def update_car(id):
    rental = pg_manager.execute_query(f"SELECT * FROM lyfter_car_rental.alquiler WHERE id = {id};")
    data = request.get_json()
    try:
        validate_state(rental_states, data["rental_state"])
        validate_fields_rentals(request.json)
        pg_manager.execute_query(f"UPDATE lyfter_car_rental.alquiler SET "
                                 f"user_id = '{request.json.get('user_id')}',"
                                 f"car_id = '{request.json.get('car_id')}',"
                                 f"rental_date = '{request.json.get('rental_date')}',"
                                 f"rental_state = '{request.json.get('rental_state')}'"
                                 f"WHERE id = '{id}';")
        return jsonify({f"data": "se actualizó la información en la base de datos"}),200
    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 500
    except TypeError as e:
        return jsonify({"error": str(e)}),400
    except ValueError as e:
        return jsonify({"error": str(e)}),400

@app.route("/rental/<id>", methods=["DELETE"])
def delete_rental(id):
    rental = pg_manager.execute_query(f"SELECT * FROM lyfter_car_rental.alquiler;")
    data = request.get_json()
    try:
        validate_state(rental_states, data["rental_state"])
        validate_fields_rentals(request.json)
        if rental:
            pg_manager.execute_query(f"DELETE FROM lyfter_car_rental.alquiler where id = {id};")
            return jsonify({"data": "se elimina de la base de datos"}), 200
        else:
            return jsonify({"error": "no existe en la base de datos"}), 404
    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 500
    except TypeError as e:
        return jsonify({"error": str(e)}),400
    except ValueError as e:
        return jsonify({"error": str(e)}),400


if __name__ == '__main__':
    app.run(host='localhost',debug=True)



