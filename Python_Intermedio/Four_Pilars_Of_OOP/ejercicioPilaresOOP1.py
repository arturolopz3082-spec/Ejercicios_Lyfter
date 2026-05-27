
class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Fondos Insuficientes")
            return
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def send_money_to_account(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)


class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print(f"no se puede retirar {amount} de dinero porque no puede "
                  f"ser menor a {self.min_balance}")
            return
        self.balance -= amount


def main():
    arthur_savings = SavingsAccount(100, 100)
    print(f"Savings Balance: {arthur_savings.balance}")
    print(f"Savings min balance: {arthur_savings.min_balance}")
    arthur_savings.deposit(300)
    print(f"Savings Balance: {arthur_savings.balance}")
    arthur_savings.withdraw(350)
    print(f"Savings Balance: {arthur_savings.balance}")


if __name__ == '__main__':
    main()