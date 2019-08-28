import json
import os
import time

class Data:

    def __init__(self):
        with open('ATMs.json','r+') as file:
            self.ATMs = json.load(file)
        with open('Clients.json','r+') as json_file:
            self.users = json.load(json_file)


# Choice of ATM
def make_choice():
    print('You can use ATM no. 1, 2, 3, 4 or 5. Which one do You like?\n'
          "To leave type 9\n")
    n = int(input('I\'d like to choose ATM number: '))
    if n == 9:
        exit()
    while n not in [1,2,3,4,5,9]:
        n = int(input('Wrong! Select correct ATM! Your ATM number: '))
        if n == 9:
            exit()
    return n

# Logging in
def authorisate():
    print('****   Login   ****')
    name = str(input('Your name: '))
    password = str(input('Your PIN: '))
    if name in users:
        if password == users[f'{name}']['PIN']:
            os.system('cls||clear')
            print('Login succesfully!')
    else:
        os.system('cls||clear')
        print('You did something wrong!')
        time.sleep(5)
        exit()
    return name

def take_out(n, name): #outcome/withdrawal
    amount = int(input('How much money do you need? \n'))
    if ATMs[f'ATM_{n}']['balance'] < amount:
        print('There is not enought money in this ATM!')
    elif users[f'{name}']['balance'] < amount:
        print('You have not enought money!')
    else:
        ATMs[f'ATM_{n}']['balance'] = ATMs[f'ATM_{n}']['balance'] - amount
        users[f'{name}']['balance'] = users[f'{name}']['balance'] - amount
    #print('There is in ATM:', ATMs[f'ATM_{n}']['balance'])
    #print('There is on your account:',users[f'{name}']['balance'])

def put_in(n, name): #income
    amount = int(input('How much money you want to put in? \n'))
    ATMs[f'ATM_{n}']['balance'] = ATMs[f'ATM_{n}']['balance'] + amount
    users[f'{name}']['balance'] = users[f'{name}']['balance'] + amount
    #print('There is in ATM:', ATMs[f'ATM_{n}']['balance'])
    #print('There is on your account:',users[f'{name}']['balance'])


def check_balance(n, name):
    print('You have:', users[f'{name}']['balance'], 'zl')


def main():
    data = Data()
    ATMs = data.ATMs
    users = data.users
    n = make_choice()
    name = authorisate()
    logged = 1
    while logged == 1:
        do = int(input('What you want to do?\n'
                      'Make a payment - press 1\n'
                      'Make a withdrawal - press 2\n'
                      'Check your account balance - press 3\n'
                      'Press 0 to log out\n'))
        while do not in [0,1,2,3]:
            do = int(input('There is no option like that. Try one more time!\n'
                          'What you want to do?\n'
                          'Make a payment - press 1\n'
                          'Make a withdrawal - press 2\n'
                          'Check your account balance - press 3\n'
                          'Press 0 to log out\n'))
        if do == 0:
            os.system('cls||clear')
            logged = do
        elif do == 1:
            os.system('cls||clear')
            put_in(n,name)
            os.system('cls||clear')
        elif do == 2:
            os.system('cls||clear')
            take_out(n,name)
            time.sleep(5)
            os.system('cls||clear')
        else:
            os.system('cls||clear')
            check_balance(n,name)
            time.sleep(5)
            os.system('cls||clear')


if __name__ == '__main__':
    main()
