from psycopg2 import sql


class CarRepository:
    FILTERABLE_COLUMNS = {"id", "make", "model", "fabrication_year", "state"}

    def __init__(self, db):
        self.db = db

    def get_all(self, filters=None):
        filters = filters or {}
        unknown = set(filters) - self.FILTERABLE_COLUMNS
        if unknown:
            raise ValueError(f"Invalid car filters: {', '.join(sorted(unknown))}")

        query = sql.SQL(
            "SELECT id, make, model, fabrication_year, state FROM lyfter_car_rental.cars"
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

    def get_by_id(self, car_id):
        query = """
            SELECT id, make, model, fabrication_year, state
            FROM lyfter_car_rental.cars
            WHERE id = %s
        """
        result = self.db.execute_query(query, (car_id,))
        return result[0] if result else None

    def create(self, data):
        query = """
            INSERT INTO lyfter_car_rental.cars (make, model, fabrication_year, state)
            VALUES (%s, %s, %s, %s)
            RETURNING id, make, model, fabrication_year, state
        """
        params = (data["make"], data["model"], data["fabrication_year"], data["state"])
        return self.db.execute_query(query, params)[0]

    def update(self, car_id, data):
        query = """
            UPDATE lyfter_car_rental.cars
            SET make = %s,
                model = %s,
                fabrication_year = %s,
                state = %s
            WHERE id = %s
            RETURNING id, make, model, fabrication_year, state
        """
        params = (
            data["make"],
            data["model"],
            data["fabrication_year"],
            data["state"],
            car_id,
        )
        result = self.db.execute_query(query, params)
        return result[0] if result else None

    def change_state(self, car_id, state):
        query = """
            UPDATE lyfter_car_rental.cars
            SET state = %s
            WHERE id = %s
            RETURNING id, make, model, fabrication_year, state
        """
        result = self.db.execute_query(query, (state, car_id))
        return result[0] if result else None

    def delete(self, car_id):
        query = "DELETE FROM lyfter_car_rental.cars WHERE id = %s RETURNING id"
        result = self.db.execute_query(query, (car_id,))
        return bool(result)