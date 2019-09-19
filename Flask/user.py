import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("first", type=int, help="First number to add")
parser.add_argument("second", type= int, help="Second number to add")
args = parser.parse_args()

numbers = {
    'First': args.first,
    'Second': args.second
}

R = requests.post('http://127.0.0.1:5000/add', json=numbers)
print(R.json())

