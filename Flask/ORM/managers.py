from sqlalchemy.orm import Session

from models import User, Car, Address


class UserManager:

    def __init__(self, session: Session):
        self.session = session

    def create_user(self, name, email):
        user = User(
            name=name,
            email=email
        )

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return user

    def update_user(self, user_id, name=None, email=None):

        user = self.session.get(User, user_id)

        if user is None:
            raise ValueError("User not found")

        if name is not None:
            user.name = name

        if email is not None:
            user.email = email

        self.session.commit()
        self.session.refresh(user)

        return user

    def delete_user(self, user_id):

        user = self.session.get(User, user_id)

        if user is None:
            raise ValueError("User not found")

        self.session.delete(user)
        self.session.commit()

        return True

    def get_all_users(self):

        return self.session.query(User).all()


class CarManager:

    def __init__(self, session: Session):
        self.session = session

    def create_car(
        self,
        brand,
        model,
        year,
        user_id=None
    ):

        car = Car(
            brand=brand,
            model=model,
            year=year,
            user_id=user_id
        )

        self.session.add(car)
        self.session.commit()
        self.session.refresh(car)

        return car

    def update_car(
        self,
        car_id,
        brand=None,
        model=None,
        year=None
    ):

        car = self.session.get(Car, car_id)

        if car is None:
            raise ValueError("Car not found")

        if brand is not None:
            car.brand = brand

        if model is not None:
            car.model = model

        if year is not None:
            car.year = year

        self.session.commit()
        self.session.refresh(car)

        return car

    def delete_car(self, car_id):

        car = self.session.get(Car, car_id)

        if car is None:
            raise ValueError("Car not found")

        self.session.delete(car)
        self.session.commit()

        return True

    def assign_car_to_user(
        self,
        car_id,
        user_id
    ):

        car = self.session.get(Car, car_id)

        if car is None:
            raise ValueError("Car not found")

        user = self.session.get(User, user_id)

        if user is None:
            raise ValueError("User not found")

        car.user = user

        self.session.commit()
        self.session.refresh(car)

        return car

    def get_all_cars(self):

        return self.session.query(Car).all()


class AddressManager:

    def __init__(self, session: Session):
        self.session = session

    def create_address(
        self,
        street,
        city,
        state,
        user_id
    ):

        user = self.session.get(User, user_id)

        if user is None:
            raise ValueError(
                "A valid user is required"
            )

        address = Address(
            street=street,
            city=city,
            state=state,
            user_id=user_id
        )

        self.session.add(address)
        self.session.commit()
        self.session.refresh(address)

        return address

    def update_address(
        self,
        address_id,
        street=None,
        city=None,
        state=None
    ):

        address = self.session.get(
            Address,
            address_id
        )

        if address is None:
            raise ValueError(
                "Address not found"
            )

        if street is not None:
            address.street = street

        if city is not None:
            address.city = city

        if state is not None:
            address.state = state

        self.session.commit()
        self.session.refresh(address)

        return address

    def delete_address(self, address_id):

        address = self.session.get(
            Address,
            address_id
        )

        if address is None:
            raise ValueError(
                "Address not found"
            )

        self.session.delete(address)
        self.session.commit()

        return True

    def get_all_addresses(self):

        return self.session.query(Address).all()