# Choice of ATM
def select_atm():
    print('You can use ATM no. 1, 2, 3, 4 or 5. Which one do You like?\n'
          "To leave type 9\n")
    selected_atm = int(input('I\'d like to choose ATM number: '))
    if selected_atm == 9:
        exit()
    while selected_atm not in [1, 2, 3, 4, 5, 9]:
        selected_atm = int(input('Wrong! Select correct ATM! Your ATM number: '))
        if selected_atm == 9:
            exit()
    return selected_atm


def select_option():
    choice = int(input('What you want to do?\n'
                       'Make a payment - press 1\n'
                       'Make a withdrawal - press 2\n'
                       'Check your account balance - press 3\n'
                       'Press 0 to log out\n'))
    while choice not in [0, 1, 2, 3]:
        choice = int(input('There is no option like that. Try one more time!\n'
                           'What you want to do?\n'
                           'Make a payment - press 1\n'
                           'Make a withdrawal - press 2\n'
                           'Check your account balance - press 3\n'
                           'Press 0 to log out\n'))
    return choice
