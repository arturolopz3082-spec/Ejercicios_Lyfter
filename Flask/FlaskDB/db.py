import psycopg2
from flask import jsonify

class PgManager:
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = self.create_connection(db_name, user, password, host, port)
        if self.connection:
            self.cursor = self.connection.cursor()
            print("Connection created succesfully")

    def create_connection(self, db_name, user, password, host, port):
        try:
            connection = psycopg2.connect(
                dbname=db_name,
                user=user,
                password=password,
                host=host,
                port=port,
            )
            return connection
        except Exception as error:
            print("Error connecting to the database:", error)
            return None

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")

    def execute_query(self, query, *args):
        try:
            self.cursor.execute(query, args)
            result = None
            if self.cursor.description is not None:
                result = self.cursor.fetchall()
            self.connection.commit()
        except psycopg2.Error as error:
            print("ERROR SQL:", error)
            self.connection.rollback()
            raise error

        return result

def validate_state( valid_states ,state):
    if state not in valid_states:
        raise ValueError(f"estado inválido debería ser uno de: {valid_states}")


def validate_fields_user(request_json, validate_id=False):
    if not isinstance(request_json, dict):
        raise TypeError("request_json debe ser un dicionario")

    required_fields = [
        'first_name',
        'last_name',
        'email',
        'username',
        'password',
        'birthdate',
        'state_account'
    ]

    if validate_id:
        required_fields.append('id')

    '''for field in required_fields:
        if field not in request_json:
            raise ValueError(f"Field {field} is required")'''

    first_name = request_json.get('first_name')
    last_name = request_json.get('last_name')
    email = request_json.get('email')
    username = request_json.get('username')
    password = request_json.get('password')
    birthdate = request_json.get('birthdate')
    state_account = request_json.get('state_account')

    if not isinstance(first_name, str) or not first_name.strip():
        raise TypeError("first_name no debe estar vacío")

    if not isinstance(last_name, str) or not last_name.strip():
        raise ValueError("last_name no debe estar vacío")

    if not isinstance(email, str) or not email.strip():
        raise ValueError("email no debe estar vacío")

    if not isinstance(username, str) or not username.strip():
        raise ValueError("username no debe estar vacio")

    if not isinstance(password, str) or not password.strip():
        raise ValueError("password no debe estar vacio")

    if not isinstance(birthdate, str) or not birthdate.strip():
        raise ValueError("birthdate no debe estar vacio")

    if not isinstance(state_account, str) or not state_account.strip():
        raise ValueError("state_account no debe estar vacio")

    if validate_id:
        id = int(request_json['id'])
        if not isinstance(id, int) or id < 0:
            raise ValueError("id debe ser un entero o mayor a cero")

    return True

def validate_fields_car(request_json, validate_id=False):
    if not isinstance(request_json, dict):
        raise ValueError("request_json debe ser un dicionario")

    required_fields = [
        "make",
        "model",
        "fabrication_year",
        "state"
    ]

    if validate_id:
        required_fields.append('id')

    for field in required_fields:
        if field not in request_json:
            raise ValueError(f"Field {field} is required")

    make = request_json.get('make')
    model = request_json.get('model')
    fabrication_year = request_json.get('fabrication_year')
    state = request_json.get('state')

    if not isinstance(make, str) or not make.strip():
        raise TypeError("make no debe estar vacio")

    if not isinstance(model, str) or not model.strip():
        raise TypeError("model no debe estar vacio")

    if not isinstance(fabrication_year, str) or not fabrication_year.strip():
        raise TypeError("fabrication_year no debe estar vacio")

    if not isinstance(state, str) or not state.strip():
        raise TypeError("state no debe estar vacio")

    if validate_id:
        id = int(request_json['id'])
        if not isinstance(id, int) or id < 0:
            raise ValueError("id debe ser un entero o mayor a cero")

def validate_fields_rentals(request_json, validate_id=False):
    if not isinstance(request_json, dict):
        raise TypeError("request_json debe ser un dicionario")
    required_fields = [
        "user_id",
        "car_id",
        "rental_date",
        "rental_state"
    ]
    if validate_id:
        required_fields.append('id')

    for field in required_fields:
        if field not in request_json:
            raise ValueError(f"Field {field} is required")
    user_id = request_json.get('user_id')
    car_id = request_json.get('car_id')
    rental_state = request_json.get('rental_state')

    if not isinstance(user_id, str) or not user_id.strip():
        raise TypeError("user_id no debe estar vacio")

    if not isinstance(car_id, str) or not car_id.strip():
        raise TypeError("car_id no debe estar vacio")

    if not isinstance(rental_state, str) or not rental_state.strip():
        raise TypeError("rental_state no debe estar vacio")

    if validate_id:
        id = int(request_json['id'])
        if not isinstance(id, int) or id < 0:
            raise ValueError("id debe ser un entero o mayor a cero")

    return True

