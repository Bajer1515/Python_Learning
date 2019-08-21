#Projekt sieci bankomatów

#- każdy bankomat to obiekt
#- bankomat ma swój aktualny balans - ilość pieniędzy znajdujących się w nim
#- bankomat pozwala na wyciąganie i wkładanie pieniędzy - jeśli spełnione są warunki
#(jest kasa w bankomacie, ktoś ma tyle na koncie)
#- ma istnieć plik konfiguracyjny typu JSON który będzie zawierać następującą strukturę

#imie_nazwisko:
#	pin:
#	aktualny_stan_konta:

#- aby wybrać pieniądze z konta powinniśmy wpisać PIN, zły PIN wyświetla komunikat,
#dobry pozwala przejść dalej


import json

#ATM - cash machine (pl. bankomat)

data = {
    'ATMs':[
        {'name': 'ATM_1', 'balance': 10000},
        {'name': 'ATM_2', 'balance': 20000},
        {'name': 'ATM_3', 'balance': 30000},
        {'name': 'ATM_4', 'balance': 40000},
        {'name': 'ATM_5', 'balance': 50000}
    ]
}
with open('ATMs','w') as file:
    json.dump(data, file)


users = {
    'Clients':[
        {'name': 'Adam Bajerowicz', 'PIN': '0001', 'balance': 15000},
        {'name': 'Lukasz Klekowski', 'PIN': '0002', 'balance': 20000},
        {'name': 'Piotr Kawa', 'PIN': '0003', 'balance': 25000}
    ]
}

with open('Clients', 'w') as file:
    json.dump(users, file)
