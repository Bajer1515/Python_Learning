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

# We are opening file as f
#f = open("Passwords.txt", "r+")
# Save data from file into list
#list = f.readlines()
# Close file

#f.close()

# Previously there was 'word\n'. We are removing this part '\n'

#words = [element.rstrip('\n') for element in list if element.rstrip('\n')]
#print(words)

#letters = string.ascii_uppercase

#for l in letters:
#    with open(f'{l}_words.txt', 'w+') as f:
#        for w in words:
#            if l == w[0]:
#                f.write(w+'\n')

print('Your chosen words:')
with open(f'{args.letter}_words.txt', 'r') as f:
    list_of_words = f.readlines()
    for i in range(args.number):
        print(random.choice(list_of_words))
