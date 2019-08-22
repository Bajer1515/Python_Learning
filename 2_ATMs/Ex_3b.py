import json

#class Operations:
    #def __init__(self):

    #def authorisation():
     #   name = str(input('Your name: '))
      #  PIN = str(input('Your PIN: '))

    #def payment():

    #def withdrawal():

    #def balance():

with open('Clients', 'r') as file:
    loaded_json = json.loads(file)

print(loaded_json)


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
