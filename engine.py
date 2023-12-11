
import os
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_DIR)

def getWordsFromFile(filepath: str) -> list[str]:

    with open(filepath, "r") as f:
        return f.read().splitlines()

def generateDefaultWeights() -> dict[chr, int]:

    letterWeight = {}
    for order in range(97, 97 + 26):

        letterWeight[chr(order)] = 1
    
    rareLetterWeight = {
        'j':7, 'v':7, 'q':7, 'w':5, 'y':5, 'z':5
    }
   
    letterWeight.update(rareLetterWeight)
    return letterWeight

def distinctLetters(word: str) -> set[chr]:

    return set(word)

def assignValue(word: str, letterWeight: dict[chr, int]) -> int:

    value = 0

    letters = distinctLetters(word)

    for letter in letters:
        value += letterWeight[letter]

    return value

def findFirst(substring: str, words: list[str]) -> tuple[int, str]:

    for index, word in enumerate(words):

        if substring in word:

            return (index, word)

    return (-1, "")
        
def removeWordAndReset(wordIndex: int, words: list[str], letterWeight: dict[chr, int]):

    foundWord = words[wordIndex]
    words[wordIndex] = ""

    for letter in foundWord:
        letterWeight[letter] = 0

    words.sort(key=lambda word: assignValue(word, letterWeight), reverse=True)

def playTurn(subtring: str, words: list[str], letterWeight: dict[chr, int], processWordCallback) -> str:

    foundIndex, foundWord = findFirst(subtring, words)

    if foundIndex == -1:

        processWordCallback(None)
        return None
    
    processWordCallback(foundWord)
    removeWordAndReset(foundIndex, words, letterWeight)

    return foundWord