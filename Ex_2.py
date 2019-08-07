import argparse
import random

# Przy pomocy argparse stworzyć program, który będzie przyjmował dwa argumenty
# * liczbę słów
# * literę,
# a następnie zwróci określoną liczbę losowych słów zaczynających się na daną literę.
# Słowa mają zostać pobrane z pliku zapisanego w ramach programu 1.


#parser = argparse.ArgumentParser()
#parser.add_argument("number", type = int, help = "Number of randomly chosen words")
#parser.add_argument("letter", help = "A letter that starts words")
#args = parser.parse_args()

# We are opening file as f
f = open("Passwords.txt", "r+")
# Save data from file into list
list = f.readlines()
# Close file
f.close()
# Previously there was 'word\n'. We are removing this part '\n'
words = [w.rstrip('\n') for w in list]
#print(words[0:100])

