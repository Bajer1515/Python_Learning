import requests
import re


# Import słownika
url = "https://raw.githubusercontent.com/sujithps/Dictionary/master/Oxford%20English%20Dictionary.txt?fbclid=IwAR37WSDQx62jLyMBgGbxKfan8kNkGHQ0eNyaFUunMy8kIWtcbnvoCVmAGEk"
r = requests.get(url)
dictionary = r.text
#print(text)

# Rozbicie słownika na osobne linijki

print('First step - all lines')
Full_list = dictionary.split("\n")
print(Full_list[0])


# C reating list without empty positions

print('Second step - no empty lines')
no_empty_list = []
no_empty_list = [line for line in Full_list if line]
print(no_empty_list[0])


# Creating list of list with separated lines

print('Third step - list of lists with words')
Full_separated_list = [element.split(' ') for element in no_empty_list]
print(Full_separated_list[0])


# Creating list with only passwords

print('Fourth step - list with only first word')
passwords = []
passwords = [item[0] for item in Full_separated_list]
print(passwords[0:10])


# Creating new file to write there passwords
file = open("Passwords.txt","a+")
for i in range(len(passwords)):
    file.write(passwords[i]+"\n")