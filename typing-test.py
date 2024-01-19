import time
from wonderwords import *
sentenceList = []
generatedSentence = ""

generator = RandomWord()

wordNum = int(input("How many words do you want?"))

def programOn():
    for i in range(0, wordNum):
        word = generator.word()
        sentenceList.append(word)
    print(sentenceList)


def Generate():
    global generatedSentence
    for i in sentenceList:
        generatedSentence  = generatedSentence + i + " " 

    print(generatedSentence)
        
programOn()
Generate()