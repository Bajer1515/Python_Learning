import requests
import re


# Import słownika
url = "https://raw.githubusercontent.com/sujithps/Dictionary/master/Oxford%20English%20Dictionary.txt?fbclid=IwAR37WSDQx62jLyMBgGbxKfan8kNkGHQ0eNyaFUunMy8kIWtcbnvoCVmAGEk"
r = requests.get(url)
dictionary = r.text
#print(text)

# Rozbicie słownika na osobne linijki

print('First step - all lines')
Full_list = dictionary.split("\n") # TODO 2): read about Python naming conventions
print(Full_list[0])


# C reating list without empty positions

print('Second step - no empty lines') # TODO 4) stick to one convention - use either double quotes or single ones
no_empty_list = []
no_empty_list = [line for line in Full_list if line] # TODO 1): you don't have to initialize an empty array if you perform list comprehension
print(no_empty_list[0])


# Creating list of list with separated lines

print('Third step - list of lists with words')
Full_separated_list = [element.split(' ') for element in no_empty_list] # TODO 1): here's a proper way of list comprehension
print(Full_separated_list[0])


# Creating list with only passwords

print('Fourth step - list with only first word')
passwords = []
passwords = [item[0] for item in Full_separated_list]
print(passwords[0:10])


# Creating new file to write there passwords
file = open("Passwords.txt","a+") # TODO 3): why a+? 
for i in range(len(passwords)): # TODO 5): can you think of another way of writing this loop?
    file.write(passwords[i]+"\n")
# TODO 6): read about with open statemenet
