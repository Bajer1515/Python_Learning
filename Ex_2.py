import argparse
import random
import string

# Przy pomocy argparse stworzyć program, który będzie przyjmował dwa argumenty
# * liczbę słów
# * literę,
# a następnie zwróci określoną liczbę losowych słów zaczynających się na daną literę.
# Słowa mają zostać pobrane z pliku zapisanego w ramach programu 1.


parser = argparse.ArgumentParser()
parser.add_argument("number", type=int, help="Number of randomly chosen words")
parser.add_argument("letter", help="A letter that starts words")
args = parser.parse_args()

print('Your chosen words:')
with open(f'Dictionaries/{args.letter}_words.txt', 'r') as f:
    list_of_words = f.readlines()
    for i in range(args.number):
        print(random.choice(list_of_words))
