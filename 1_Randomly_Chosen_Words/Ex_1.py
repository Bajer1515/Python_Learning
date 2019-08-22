import requests
import re
import string
import os

# Import of dictionary
url = "https://raw.githubusercontent.com/sujithps/Dictionary/master/Oxford%20English%20Dictionary.txt?fbclid=IwAR37WSDQx62jLyMBgGbxKfan8kNkGHQ0eNyaFUunMy8kIWtcbnvoCVmAGEk"
r = requests.get(url)
dictionary = r.text


# Cut the dictionary to separated lines

print('First step - all lines')
full_list = dictionary.split("\n")


# C reating list without empty positions

print('Second step - no empty lines')
no_empty_list = [line for line in full_list if line]


# Creating list of list with separated lines

print('Third step - list of lists with words')
full_separated_list = [element.split(' ') for element in no_empty_list]


# Creating list with only passwords without empty lines

print('Fourth step - list with only first word')
words = [item[0] for item in full_separated_list if item[0].strip('\n')]


letters = string.ascii_uppercase

# Creating list of indexes
indexes = []
for l in letters:
    indexes.append(words.index(f'{l}'))
print(indexes)

# Creating A-Y files automatically + manually Z file

let = letters[0:-1]

i = 0
for l in let:
    new_words = words[indexes[i]:indexes[i+1]]
    i = i + 1
    with open(os.path.join('Dictionaries',f'{l}_words.txt'), 'w+') as f:
        for word in new_words:
            f.write(word+'\n')


with open(os.path.join('Dictionarie','Z_words.txt'), 'w+') as fZ:
    Z_words = words[indexes[-1]:len(words)]
    for word in Z_words:
        fZ.write(word+'\n')

