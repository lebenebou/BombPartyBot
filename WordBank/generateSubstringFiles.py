
import time
import os

def generatePossibleSubstrings():

    subtrings = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for l1 in alphabet:
        for l2 in alphabet:
            subtrings.append(l1+l2)

    
    for l1 in alphabet:
        for l2 in alphabet:
            for l3 in alphabet:
                subtrings.append(l1+l2+l3)

    return subtrings

def addWordsToSubstringFile(substring: str, words: list):

    fileName = (substring + ".txt")
    filePath = os.path.join(SUBSTRING_FOLDER, fileName)

    filteredWords = [word for word in words if (substring in word)]

    with open(filePath, 'w') as f:
        f.writelines(filteredWords)

    return

if __name__=="__main__":

    os.system("cls")

    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    WORDS_FILE = os.path.join(CURRENT_DIR, "BombPartyDictionary.txt")
    SUBSTRING_FOLDER = os.path.join(CURRENT_DIR, "Substrings")

    if not os.path.exists(SUBSTRING_FOLDER):
        os.mkdir(SUBSTRING_FOLDER)

    print("Generating substring files...")
    print("This will take about 5 minutes...")

    allWords = []
    with open(WORDS_FILE, "r") as f:
        allWords = f.readlines()

    for substring in generatePossibleSubstrings():
        addWordsToSubstringFile(substring, allWords)

    print("Substring files generated.")