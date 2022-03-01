from bs4 import BeautifulSoup
import requests
from random import randint

wordNum=randint(1,292)
ATTEMPTS = 6
WORD_LENGTH = 5

#f = open("EstonianDictionary.txt")
#lines = f.readlines()
#Word = lines[wordNum]
#f.close()

Word = "selga"

while ATTEMPTS != 0 :
    val = input("Enter a 5 letter word:")
    if len(val) == 5 and val.isalpha():
        val = val.lower()
        vallink = val
        vallink = vallink.replace("ä","%E4")
        vallink = vallink.replace("õ","%F5")
        vallink = vallink.replace("ö","%F6")
        response = requests.get(url="https://aare.pri.ee/dictionary.html?query="
                                    +vallink+
                                    "&lang=ee&meth=exact&switch=en&otsi=search")
        soup = BeautifulSoup(response.content, 'lxml')
        data = soup.findAll("td")
        flag1 = False
        flag2 = False

        for line in data :
            sentence = line.text
            if "No results." in sentence:
                flag1 = True
            if "Did you mean" in sentence:
                flag2 = True

        if flag1 == True or flag2 == True:
            print("Please enter a valid Estonian word. Allowed attempt left:", ATTEMPTS)
        elif val == Word :
            print("Congratulations, you've guessed the word!")
            break
        elif flag1 == False and flag2 == False:
            ATTEMPTS = ATTEMPTS - 1
            if ATTEMPTS > 0:
                print("Wrong answer. Allowed attempt left:", ATTEMPTS)

                val = set(list(val))
                splitWord = list(Word)

                for i in val:
                    if i in splitWord:
                        print(i,"exists in the word.")

            elif ATTEMPTS == 0:
                print("No attempts left. Game Over.")
                print("The word was:", Word)
                break
        else:
            print("Unknown error")

    else:
        print("Enter a word with 5 letters!")