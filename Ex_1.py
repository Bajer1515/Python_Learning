import requests
import re


# Import słownika
url = "https://raw.githubusercontent.com/sujithps/Dictionary/master/Oxford%20English%20Dictionary.txt?fbclid=IwAR37WSDQx62jLyMBgGbxKfan8kNkGHQ0eNyaFUunMy8kIWtcbnvoCVmAGEk"
r = requests.get(url)
text = r.text
#print(text)

# Rozbicie słownika na osobne linijki
t = text.split("\n")
print(len(t))
print(t[1:10])

# Usunięcie pustych linii
# 1) what is t? text? tribute? variable / method etc. names should be self-explanatory - in the best case you just look at the name and know all of required information. 't' doesn't provide that
# 2) it does work, but maybe think about list comprehension [line for line in t if line] 
#     2a) why is there if line? this means that we take only the strings that are True - when are they True? --> check https://stackoverflow.com/a/4531832
while '' in t:
    t.remove('')  

print(len(t))
print(t[1:10])

for i in t:
    t[i].split("  ")
# t = [element.split(' ') for element in t] # list comprehension - once again your solution was ok, but you can do it slightly more elegant way

#t2 = t.split("  ")

print(len(t2))
print(t2[1:10])

#t3 = t2.partition('  ')

#print(t3[1:3])


### Extraction of the first word. 
# Look for rsplit() function - as You may have seen words do not contain any spaces in them (even when they contain a dash). This means that you can split by ' '. 





