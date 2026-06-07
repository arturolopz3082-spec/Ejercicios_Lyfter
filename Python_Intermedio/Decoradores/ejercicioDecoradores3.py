from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1

        return years


def validate_adult(func):
    def wrapper(*args, **kwargs):
        all_params = list(args) + list(kwargs.values())

        for param in all_params:
            if isinstance(param, User):
                if param.age < 18:
                    raise ValueError(f"Menor de edad: {param.age}")

        return func(*args, **kwargs)

    return wrapper


@validate_adult
def access(user):
    return f"Edad: {user.age}"

user_ok = User(date(2000, 5, 10))
print(access(user_ok))

user_bad = User(date(2010, 1, 1))
print(access(user_bad))