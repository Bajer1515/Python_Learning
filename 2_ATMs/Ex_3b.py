import json

#class Operations:
    #def __init__(self):

#To tak na próbę zanim nauczę się wczytywać z pliku i do niego zapisywać od razu
ATMs = {
    'ATM_1':
        {'name': 'ATM_1', 'balance': 10000},
    'ATM_2':
        {'name': 'ATM_2', 'balance': 20000},
    'ATM_3':
        {'name': 'ATM_3', 'balance': 30000},
    'ATM_4':
        {'name': 'ATM_4', 'balance': 40000},
    'ATM_5':
        {'name': 'ATM_5', 'balance': 50000}
}
users = {
    'Adam_Bajerowicz':{
        'PIN': '0001', 'balance': 15000},
    'Lukasz_Klekowski':{
        'PIN': '0002', 'balance': 20000},
    'Piotr_Kawa':{
        'PIN': '0003', 'balance': 25000}
}

def choice():
    print('You can use ATM no. 1, 2, 3, 4 or 5. Which one do You like?')
    n = int(input('I\'d like to choose ATM number: '))
    while n not in [1,2,3,4,5]:
        n = int(input('Wrong! Select correct ATM! Your ATM number: '))


def authorisation():
    print('****   Login   ****')
    name = str(input('Your name: '))
    password = str(input('Your PIN: '))
    if password == users[f'{name}']['PIN']:
        print('Login succesfully!')
    else:
        print('Invalid login or password')

#    def payment(): #Wypłata

#    def withdrawal(): #Wpłata

#    def balance(): #Sprawdzenie salda konta

#    def change_PIN(): #Zmiana PINu

#with open('Clients', 'r') as file:
#    loaded_json = json.loads(file)

#print(loaded_json)

choice()
authorisation()



#1. Wczytanie listy bankomatów.
#2. Wybór bankomatu.
#3. Autoryzacja:
#    - pobranie listy klientów
#    - porównanie PINu do imienie i nazwiska użytkownika
#    - jeżeli jest to przechodzimy dalej, jak nie to błąd
#4. Wybór opcji.
#5. Wpłata:
#    - podać kwotę wpłaty,
#    - kwota jest dodana do konta i jednocześnie do bilansu bankomatu,
#    - możliwość wyboru innej opcji.
#6. Wypłata:
#    - podać kwotę wypłaty,
#    - sprawdzić czy ma tyle na koncie,
#    - sprawdzić czy bankomat ma tyle w sobie,
#    - jeżeli się zgadza to od konta odejmujemy kwotę i od bilansu bankomatu.
#7. Zmiana PINu:
#    - zassaj plik z klientami,
#    - podaj stary PIN,
#    - podaj nowy PIN,
#    - zapisać do JSONa zmieniony PIN.
#8. Sprawdzenie stanu konta:
#    - zassaj listę użytkowników,
#    - podaj stan konta
#9. WYlogowanie:
#    - usunięcie zmiennej z użytkownikiem,
#    - zapisanie zmian w pliku 'ATMs'
