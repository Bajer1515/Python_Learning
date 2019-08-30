import os
import time
from .atm import ATM
from .utils import select_atm, select_option


def main():
    selected_atm = select_atm()
    atm = ATM.create_atm(selected_atm)
    logged, name = ATM.authorisate()
    while logged is True:
        choice = select_option()
        if choice == 0:
            os.system('cls||clear')
            logged = False
            ATM.logging_out(atm.id, atm.balance)
        elif choice == 1:
            os.system('cls||clear')
            amount = int(input('How much you want to put in? '))
            atm.put(amount, name)
            os.system('cls||clear')
        elif choice == 2:
            os.system('cls||clear')
            amount = int(input('How much you want to take out? '))
            atm.take(amount, name)
            time.sleep(5)
            os.system('cls||clear')
        else:
            os.system('cls||clear')
            atm.check_balance()
            time.sleep(5)
            os.system('cls||clear')


if __name__ == '__main__':
    main()
