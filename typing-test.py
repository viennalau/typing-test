import time
from wonderwords import *
sentenceList = []
generatedSentence = ""
wordsCompleted = 0
generator = RandomWord()
incorrectChars = 0
correctChars = 0
wordTotal = 0
accuracy = 0
timeElapsed = 0
wpm = 0

def programOn():
    wordTotal = int(input("\nHow many words do you want? "))
    generate(wordTotal)
    actualTest()
    
def generate(wordTotal):
    global generatedSentence
    for i in range(0, wordTotal):
        word = generator.word(word_min_length=3, word_max_length=6)
        sentenceList.append(word)
    for i in sentenceList:
        if i == sentenceList[-1]:
            generatedSentence = generatedSentence + i
        else:
            generatedSentence = generatedSentence + i + " "
    
def actualTest():
    global userSentence
    global generatedSentence
    global timeElapsed
    print('-------------------------------------------------------------------------')
    print(generatedSentence)
    print('-------------------------------------------------------------------------')
    testOn = True
    while testOn == True:
        startTime = time.time()
        userSentence = input("Type the sentence above: ")
        print('-------------------------------------------------------------------------')
        endTime = time.time()
        timeElapsed = round((endTime - startTime), 2)
        testOn = False
        
    accuracyCheck(userSentence)
    wordCheck()
    wpmCheck(wordsCompleted, timeElapsed)
    statistics()

def accuracyCheck(userSentence):
    global correctChars
    global incorrectChars
    global accuracy
    userSplice = userSentence.split()

    if wordsCompleted == wordTotal:
        for wordNum in range(0, len(sentenceList)):
            if len(sentenceList[wordNum]) == len(userSplice[wordNum]):
                if sentenceList[wordNum] == userSplice[wordNum]:
                    correctChars = correctChars + len(userSplice[wordNum])
                else:
                    for char in range(0, len(userSplice[wordNum])):
                        if sentenceList[wordNum][char] == userSplice[wordNum][char]:
                            correctChars += 1
                        else:
                            incorrectChars += 1 
            else:
                iterations = 0
                min_length = min(len(sentenceList[wordNum]), len(userSplice[wordNum]))
                while iterations < min_length:
                    for char in range(0, min_length):
                        if sentenceList[wordNum][char] == userSplice[wordNum][char]:
                            correctChars += 1
                            iterations += 1
                        else:
                            incorrectChars += 1 
                            iterations += 1
                            userSplice[wordNum] = userSplice[wordNum][:char] + userSplice[wordNum][char+1:]
                incorrectChars += abs(len(sentenceList[wordNum]) - len(userSplice[wordNum]))
                
    print(f'total amt of correct: {correctChars}')
    print(f'total amt of incorrect: {incorrectChars}')      
      
    accuracy = round((correctChars / (correctChars+incorrectChars)), 2) * 100
    
def wordCheck():
    global wordsCompleted
    if " " in userSentence:
        wordsCompleted = userSentence.count(" ") + 1
    else:
        wordsCompleted = 1
    
def wpmCheck(wordsCompleted, timeElapsed):
    global wpm
    timeElapsedRatio = 60 / timeElapsed
    wpm = round(wordsCompleted*timeElapsedRatio)

def statistics():
    global wpm
    print(f'Accuracy: {accuracy}%')
    print(f'Time Elapsed: {timeElapsed} seconds')
    print(f'WPM: {wpm}')

programOn()