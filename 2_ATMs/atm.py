import json


class ATM:
    with open('Clients.json', 'r+') as json_file:
        users = json.load(json_file)
    with open('ATMs.json', 'r+') as file:
        atms = json.load(file)

    def __init__(self, balance, n):
        self.balance = balance
        self.id = n

    def put(self, amount, name):
        self.balance += amount
        ATM.users[name]['balance'] += amount
        # ATM.atms[f'ATM_{self.id}']['balance'] += amount

    def take(self, amount, name):
        if self.balance < amount or ATM.users[name]['balance'] < amount:
            print('There is no money.')
            return

        self.balance -= amount
        ATM.users[name]['balance'] -= amount
        # ATM.atms[f'ATM_{self.id}']['balance'] -= amount

    @classmethod
    def authorisate(cls):
        name = input('Your name: ')
        PIN = input('Your PIN: ')
        if name not in cls.users or PIN != cls.users[name]['PIN']:
            print('Sth is wrong')
            return False, None

        print('Login succesfully!')
        return True, name

    def check_balance(self):
        print(f'There is: {self.balance}')

    @classmethod
    def logging_out(cls, atm_no, balance):
        cls.atms[f'ATM_{atm_no}']['balance'] = balance
        with open('ATMs.json','w') as file:
            json.dump(cls.atms, file)
        with open('Clients.json', 'w') as file:
            json.dump(cls.users, file)
        exit()

    @classmethod
    def create_atm(cls, atm_no):
        atm_balance = cls.atms[f'ATM_{atm_no}']['balance']
        return cls(atm_balance, atm_no)
