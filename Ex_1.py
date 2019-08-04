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
while '' in t:
    t.remove('')

print(len(t))
print(t[1:10])

for i in t:
    t[i].split("  ")


#t2 = t.split("  ")

print(len(t2))
print(t2[1:10])

#t3 = t2.partition('  ')

#print(t3[1:3])

