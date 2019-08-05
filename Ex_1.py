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

# Change third step with second step.
#C reating list without empty positions
print('Third step - no empty lines')
no_empty_list = []
no_empty_list = [line for line in Full_list if line]
print(no_empty_list[0])


# Creating list of list with separated lines
print('Second step - list of lists with words')
Full_separated_list = [element.split(' ') for element in no_empty_list]
print(Full_separated_list[1])





