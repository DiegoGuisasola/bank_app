# Parent class: User
# Child class: Bank
# Stores user info and allows withdrawal, deposit and check balance

class User:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_info(self):
        print('Personal information')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance:float = 0

    def deposit(self,amount:float):
        self.balance += amount
        print(f'Deposit succesfully. New balance: ${self.balance}')

    def withdraw(self,amount:float):
        if self.balance < amount:
            print(f'Insufficient funds. You have ${self.balance}')
        else:
            self.balance -= amount
            print(f'Withdrawal succesfully. New balance: ${self.balance}')

    def view_balance(self):
        # self.show_info()
        print(f'Your balance is: ${self.balance}')