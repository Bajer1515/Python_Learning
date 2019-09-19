import requests

first = int(input('First number to add: '))
second = int(input('Second number to add: '))

numbers = {
    'First': first,
    'Second': second
}

R = requests.post('http://127.0.0.1:5000/add', json=numbers)
print(R.json())

