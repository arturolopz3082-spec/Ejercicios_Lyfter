import psycopg2
from psycopg2.extras import RealDictCursor


class PgManager:
    def __init__(self, db_name, user, password, host, port=5432):
        self.connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        print("Connection created successfully")

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            result = None

            if self.cursor.description is not None:
                result = [dict(row) for row in self.cursor.fetchall()]

            self.connection.commit()
            return result

        except psycopg2.Error:
            self.connection.rollback()
            raise

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")


def validate_state(valid_states, state):
    if state not in valid_states:
        raise ValueError(f"Invalid state. Expected one of: {valid_states}")


def require_json_object(data):
    if not isinstance(data, dict):
        raise TypeError("The request body must be a JSON object")


def validate_fields_user(data):
    require_json_object(data)

    required_fields = [
        "first_name",
        "last_name",
        "email",
        "username",
        "password",
        "birthdate",
        "state_account",
    ]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Field '{field}' is required")

    for field in ["first_name", "last_name", "email", "username", "password", "birthdate", "state_account"]:
        if not isinstance(data[field], str) or not data[field].strip():
            raise ValueError(f"Field '{field}' cannot be empty")


def validate_fields_car(data):
    require_json_object(data)

    required_fields = ["make", "model", "fabrication_year", "state"]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Field '{field}' is required")

    if not isinstance(data["make"], str) or not data["make"].strip():
        raise ValueError("Field 'make' cannot be empty")
    if not isinstance(data["model"], str) or not data["model"].strip():
        raise ValueError("Field 'model' cannot be empty")
    if not isinstance(data["fabrication_year"], int):
        raise TypeError("Field 'fabrication_year' must be an integer")
    if not isinstance(data["state"], str) or not data["state"].strip():
        raise ValueError("Field 'state' cannot be empty")


def validate_fields_rental(data):
    require_json_object(data)

    required_fields = ["user_id", "car_id"]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Field '{field}' is required")

    if not isinstance(data["user_id"], int):
        raise TypeError("Field 'user_id' must be an integer")
    if not isinstance(data["car_id"], int):
        raise TypeError("Field 'car_id' must be an integer")