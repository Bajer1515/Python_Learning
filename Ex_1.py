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
print(Full_list[4])

# Rozbicie każdej lini na listy pojedynczych słów
print('Second step - list of lists with words')
Full_separated_list = [element.split(' ') for element in Full_list]
print(Full_separated_list[4])

#Creating list without empty positions
print('Third step - no empty lines')
no_empty = []
no_empty = [line for line in Full_separated_list if line == True]
print(no_empty)





# Usunięcie pustych linii
#while '' in t:
#    t.remove('')

#print(len(t))
#print(t[1:10])



#t2 = t.split("  ")

#print(len(t2))
#print(t2[1:10])

#t3 = t2.partition('  ')

#print(t3[1:3])

