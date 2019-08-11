import requests
import re
import string

# Import słownika
url = "https://raw.githubusercontent.com/sujithps/Dictionary/master/Oxford%20English%20Dictionary.txt?fbclid=IwAR37WSDQx62jLyMBgGbxKfan8kNkGHQ0eNyaFUunMy8kIWtcbnvoCVmAGEk"
r = requests.get(url)
dictionary = r.text
#print(text)

# Rozbicie słownika na osobne linijki

print('First step - all lines')
full_list = dictionary.split("\n")
#print(full_list[0:10])

# C reating list without empty positions

print('Second step - no empty lines')
no_empty_list = [line for line in full_list if line]
#print(no_empty_list[0:10])

# Creating list of list with separated lines

print('Third step - list of lists with words')
full_separated_list = [element.split(' ') for element in no_empty_list]
#print(full_separated_list[0:10])

# Creating list with only passwords without empty lines

print('Fourth step - list with only first word')
passwords = [item[0] for item in full_separated_list if item[0].strip('\n')]
#print(passwords[2016])

# Creating new file to write there passwords

#with open('Passwords.txt','a+') as file:
#    for i in range(len(passwords)):
#        file.write(passwords[i]+"\n")

letters = string.ascii_uppercase

# Creating list of indexes
index = []
for l in letters:
    index.append(passwords.index(f'{l}'))

# Try to slice list in parts but I have no good idea how to do it
i = 0
n = 0
for l in letters:
    n = n + 1
    with open(f'{l}_words', 'w+') as f:
        if i < index[n]:
            f.write(passwords[i]+'\n'')
        elif


#for l in letters:
#    with open(f'{l}_words.txt', 'w+'):
#        for passwords.index(f'{l}') in range()





