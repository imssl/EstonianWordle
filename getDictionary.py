from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Estonian_wordlist")
soup = BeautifulSoup(response.content, 'lxml')
data = soup.findAll("li")

for line in data:
    word = line.text
    word = word.split()[0]
    upperCase = word[0].isupper()

    if len(word) == 5 and not upperCase:
        f = open("EstonianDictionary.txt", "a")
        f.write(word + "\n")
        f.close()

