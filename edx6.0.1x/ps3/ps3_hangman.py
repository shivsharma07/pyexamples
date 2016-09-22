# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "F:/Workspaces/PyDev/edx6.0.1x/ps3/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    modifiedLettersList = list(lettersGuessed)
    for letter in secretWord:
        if letter in modifiedLettersList:
            count += 1
            modifiedLettersList.remove(letter)
        else:
            return False
        if count > len(lettersGuessed):
            return False
        if count == len(secretWord)-1:
            return True
            
#print isWordGuessed('apple', ['e', 'i', 'k', 'p', 'r', 's'])
#print isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])
#print isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])
#print isWordGuessed('lettuce', ['z', 'x', 'q', 'l', 'e', 't', 't', 'u', 'c', 'e'])

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedWord += letter
        else:
            guessedWord += "_ "
    return guessedWord
    
#print getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    lowercaseAlphabetList = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in lowercaseAlphabetList:
            lowercaseAlphabetList.remove(letter)
    return "".join(lowercaseAlphabetList)
    
#print getAvailableLetters(['e', 'e'])
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print "Welcome to the game, Hangman!"
    numberOfSecretLetters = len(secretWord)
    numberOfGuesses = 8
    print "I am thinking of a word that is " + str(numberOfSecretLetters) + " letters long."
    lettersGuessed = []
    mistakesMade = 0
    while numberOfSecretLetters > 0 and numberOfGuesses > 0:
        print "-----------"
        print "You have "+  str(numberOfGuesses) +" guesses left."
        availableLetters = getAvailableLetters(lettersGuessed)
        print "Available letters: "+availableLetters
        guess = raw_input("Please guess a letter: ")
        guessInLowerCase = guess.lower()
        
        lettersGuessed.append(guessInLowerCase)
        alreadyFlag = False
        
        if guessInLowerCase not in availableLetters:
            print  "Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed)
            alreadyFlag = True
        
        if guessInLowerCase in secretWord and alreadyFlag != True:
            print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
            numberOfSecretLetters = getGuessedWord(secretWord, lettersGuessed).count("_")       
        elif guessInLowerCase not in secretWord and alreadyFlag != True:            
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            mistakesMade += 1
            numberOfGuesses -= 1
        #isWordGuessed(secretWord, lettersGuessed)
        
    print "-----------"
    if numberOfGuesses > 0:
        print "Congratulations, you won!"
    else:
        print "Sorry, you ran out of guesses. The word was else."

hangman("x")
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
