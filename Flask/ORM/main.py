from sqlalchemy import inspect

from database import (
    engine,
    SessionLocal,
    create_tables
)

import models

from managers import (
    UserManager,
    CarManager,
    AddressManager
)


def validate_tables():

    inspector = inspect(engine)

    tables = inspector.get_table_names()

    required_tables = {
        "users",
        "cars",
        "addresses"
    }

    if required_tables.issubset(set(tables)):
        print("All tables already exist.")

    else:
        print("Some tables are missing.")
        print("Creating tables...")

        create_tables()

        print("Tables created successfully.")


def main():

    validate_tables()

    session = SessionLocal()

    try:

        user_manager = UserManager(session)
        car_manager = CarManager(session)
        address_manager = AddressManager(session)

        # Crear usuario
        user = user_manager.create_user(
            name="Arturo Lopez",
            email="arturo@email.com"
        )

        print("\nUser created:")
        print(user)

        # Crear automóvil sin usuario
        car = car_manager.create_car(
            brand="Nissan",
            model="Kicks",
            year=2026
        )

        print("\nCar created:")
        print(car)

        # Crear dirección
        address = address_manager.create_address(
            street="Av. Reforma 100",
            city="Ciudad de Mexico",
            state="CDMX",
            user_id=user.id
        )

        print("\nAddress created:")
        print(address)

        # Asociar automóvil
        car_manager.assign_car_to_user(
            car_id=car.id,
            user_id=user.id
        )

        print("\nCar assigned to user.")

        # Consultar usuarios
        print("\nUSERS")

        users = user_manager.get_all_users()

        for current_user in users:
            print(current_user)

        # Consultar automóviles
        print("\nCARS")

        cars = car_manager.get_all_cars()

        for current_car in cars:
            print(current_car)

        # Consultar direcciones
        print("\nADDRESSES")

        addresses = address_manager.get_all_addresses()

        for current_address in addresses:
            print(current_address)

    except Exception as error:

        session.rollback()

        print(
            f"An error occurred: {error}"
        )

    finally:

        session.close()


if __name__ == "__main__":
    main()