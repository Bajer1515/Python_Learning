import json

#class Operations:
    #def __init__(self):

#To tak na próbę zanim nauczę się wczytywać z pliku i do niego zapisywać od razu
data = {
    'ATMs':[
        {'name': 'ATM_1', 'balance': 10000},
        {'name': 'ATM_2', 'balance': 20000},
        {'name': 'ATM_3', 'balance': 30000},
        {'name': 'ATM_4', 'balance': 40000},
        {'name': 'ATM_5', 'balance': 50000}
    ]
}
users = {
    'Clients':[
        {'name': 'Adam Bajerowicz', 'PIN': '0001', 'balance': 15000},
        {'name': 'Lukasz Klekowski', 'PIN': '0002', 'balance': 20000},
        {'name': 'Piotr Kawa', 'PIN': '0003', 'balance': 25000}
    ]
}
x = users['Clients']
print(x)

def choice():
    print('You can use ATM no. 1, 2, 3, 4 or 5. Which one do You like?')
    n = int(input('I\'d like to choose ATM number: '))
    if (n < 1 & n > 5):
        n = int(input('Wrong! Select correct ATM!'))


def authorisation():
    print('****   Login   ****')
    name = str(input('Your name: '))
    PIN = str(input('Your PIN: '))


#    def payment():

#    def withdrawal():

#    def balance():

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
