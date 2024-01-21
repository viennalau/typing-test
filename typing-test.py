import time
from wonderwords import *

generator = RandomWord()

sentenceList = []
generatedSentence = ""

wordsCompleted = 0
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
    
# Generates a sentence based on the amount of the words the user specified, using "simple" words    
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
    
# Doesn't do much on its own. Basically prints out the generated sentence and tells the user to type it.
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
        # Calculates the difference between when the test was started and finished to find the elapsed time.
        endTime = time.time()
        timeElapsed = round((endTime - startTime), 2)
        testOn = False
    # After the calculation is done, calls the other functions    
    accuracyCheck(userSentence)
    wordCheck()
    wpmCheck(wordsCompleted, timeElapsed)
    statistics()

def accuracyCheck(userSentence):
    global correctChars
    global incorrectChars
    global accuracy
    
    # Turns the user's sentence into a list
    userSplice = userSentence.split()

    if wordsCompleted == wordTotal:
        # for a number between 0 and the length of the list (amount of items/words)
        # check if the length of the word in the original list
        # is the same as the number in the user's list (sentence)
        # if they're the same length, check if the words are the same
        #if the words are the same, add the amount of correct characters in the word (all) to the total amount of correct characters
        for wordNum in range(0, len(sentenceList)):
            if len(sentenceList[wordNum]) == len(userSplice[wordNum]):
                if sentenceList[wordNum] == userSplice[wordNum]:
                    correctChars = correctChars + len(userSplice[wordNum])
                else:
                    # goes through each individual character in the word and checks if its the same as the original word
                    for char in range(0, len(userSplice[wordNum])):
                        if sentenceList[wordNum][char] == userSplice[wordNum][char]:
                            correctChars += 1
                        else:
                            incorrectChars += 1 
                            
            else:
                # if the lengths arent the same, we need to use iterations & min length to prevent indexing errors
                iterations = 0
                min_length = min(len(sentenceList[wordNum]), len(userSplice[wordNum]))
                while iterations < min_length:
                    # goes through the amount of characters that the original list and user list have in common (# wise)
                    for char in range(0, min_length):
                        if sentenceList[wordNum][char] == userSplice[wordNum][char]:
                            correctChars += 1
                            iterations += 1
                        else:
                            incorrectChars += 1 
                            iterations += 1
                            # string splicing occurs because if there is a duplicate character or extra character, it will offset
                            # the whole string, making the rest of the characters incorrect when they were "technically" the same
                            userSplice[wordNum] = userSplice[wordNum][:char] + userSplice[wordNum][char+1:]
                # finds the difference in length between the original word and the user's word.
                # absolute value is used because the user's word could be longer than the original word, ending up in a negative value.
                incorrectChars += abs(len(sentenceList[wordNum]) - len(userSplice[wordNum]))
                
    print(f'total amt of correct: {correctChars}')
    print(f'total amt of incorrect: {incorrectChars}')      
    
    # rounds the accuracy percentage to 2 decimal places, and multiplies it by 100 to find the percentage
    accuracy = round((correctChars / (correctChars+incorrectChars)), 2) * 100
    
# checks for the amount of words in the sentence
def wordCheck():
    global wordsCompleted
    if " " in userSentence:
        # + 1 because a space between two words is just one space but two words in total
        # counts the number of spaces to determine the amount of words
        wordsCompleted = userSentence.count(" ") + 1
    else:
        wordsCompleted = 1
    
def wpmCheck(wordsCompleted, timeElapsed):
    global wpm
    # finds the ratio between the time that has passed to one minute, then applies that to the amount of words completed
    # to determine the ratio of words to minutes (WPM)
    timeElapsedRatio = 60 / timeElapsed
    wpm = round(wordsCompleted*timeElapsedRatio)

def statistics():
    global wpm
    print(f'Accuracy: {accuracy}%')
    print(f'Time Elapsed: {timeElapsed} seconds')
    print(f'WPM: {wpm}')

programOn()