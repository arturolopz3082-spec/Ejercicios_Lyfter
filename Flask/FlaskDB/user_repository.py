from psycopg2 import sql


class UserRepository:
    TABLE = "users"
    PUBLIC_COLUMNS = (
        "id",
        "first_name",
        "last_name",
        "email",
        "username",
        "birthdate",
        "state_account",
        "is_delinquent",
    )
    FILTERABLE_COLUMNS = set(PUBLIC_COLUMNS)

    def __init__(self, db):
        self.db = db

    def get_all(self, filters=None):
        filters = filters or {}
        unknown = set(filters) - self.FILTERABLE_COLUMNS
        if unknown:
            raise ValueError(f"Invalid user filters: {', '.join(sorted(unknown))}")

        query = sql.SQL("SELECT {} FROM lyfter_car_rental.users").format(
            sql.SQL(", ").join(map(sql.Identifier, self.PUBLIC_COLUMNS))
        )
        params = []

        if filters:
            clauses = []
            for column, value in filters.items():
                clauses.append(sql.SQL("{} = %s").format(sql.Identifier(column)))
                params.append(value)
            query += sql.SQL(" WHERE ") + sql.SQL(" AND ").join(clauses)

        query += sql.SQL(" ORDER BY id")
        return self.db.execute_query(query, tuple(params))

    def get_by_id(self, user_id):
        query = sql.SQL("SELECT {} FROM lyfter_car_rental.users WHERE id = %s").format(
            sql.SQL(", ").join(map(sql.Identifier, self.PUBLIC_COLUMNS))
        )
        result = self.db.execute_query(query, (user_id,))
        return result[0] if result else None

    def create(self, data):
        query = """
            INSERT INTO lyfter_car_rental.users
                (first_name, last_name, email, username, password, birthdate, state_account)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id, first_name, last_name, email, username, birthdate, state_account, is_delinquent
        """
        params = (
            data["first_name"],
            data["last_name"],
            data["email"],
            data["username"],
            data["password"],
            data["birthdate"],
            data["state_account"],
        )
        return self.db.execute_query(query, params)[0]

    def update(self, user_id, data):
        query = """
            UPDATE lyfter_car_rental.users
            SET first_name = %s,
                last_name = %s,
                email = %s,
                username = %s,
                password = %s,
                birthdate = %s,
                state_account = %s
            WHERE id = %s
            RETURNING id, first_name, last_name, email, username, birthdate, state_account, is_delinquent
        """
        params = (
            data["first_name"],
            data["last_name"],
            data["email"],
            data["username"],
            data["password"],
            data["birthdate"],
            data["state_account"],
            user_id,
        )
        result = self.db.execute_query(query, params)
        return result[0] if result else None

    def change_state(self, user_id, state):
        query = """
            UPDATE lyfter_car_rental.users
            SET state_account = %s
            WHERE id = %s
            RETURNING id, first_name, last_name, email, username, birthdate, state_account, is_delinquent
        """
        result = self.db.execute_query(query, (state, user_id))
        return result[0] if result else None

    def set_delinquent(self, user_id, is_delinquent=True):
        query = """
            UPDATE lyfter_car_rental.users
            SET is_delinquent = %s
            WHERE id = %s
            RETURNING id, first_name, last_name, email, username, birthdate, state_account, is_delinquent
        """
        result = self.db.execute_query(query, (is_delinquent, user_id))
        return result[0] if result else None

    def delete(self, user_id):
        query = "DELETE FROM lyfter_car_rental.users WHERE id = %s RETURNING id"
        result = self.db.execute_query(query, (user_id,))
        return bool(result)