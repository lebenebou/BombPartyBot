
from GameSession import GameSession
import pyautogui
import os

def switchApps():

    pyautogui.hotkey("alt", "tab")

def typeAndSubmit(word:str):

    pyautogui.typewrite(word, interval=0.1)
    pyautogui.press("enter")

def handleFoundWord(word: str):

    if word is None:
        return

    switchApps()
    typeAndSubmit(word)
    switchApps()

def doNothing():
    pass

def saveInvalidWords(invalidWords: list[str]):

    with open(INVALID_WORDS_PATH, "a") as f:
        f.write("\n".join(invalidWords))

def safeExit(invalidWords: list[str]):

    saveInvalidWords(invalidWords)
    exit(0)

def reset(session: GameSession):

    session = GameSession(acceptedWords, handleFoundWord, doNothing, 3, 3)
    os.system("cls")

def showSessionInfo(session: GameSession):

    print(f"{session.lastQueriedSubstring}: ", end="")

    if session.lastFoundWord is None:
        print("No word found")
    else:
        print(f"found wrod: {session.lastFoundWord}")
    
    for letter, weight in session.letterWeights.items():
        
        if weight == 0:
            continue

        print(letter, end="")

    print("\n")

if __name__ == "__main__":

    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    WORDS_PATH = os.path.join(CURRENT_DIR, "wordBank", "BombPartyDictionary.txt")
    INVALID_WORDS_PATH = os.path.join(CURRENT_DIR, "wordBank", "invalidWords.txt")

    acceptedWords = []
    with open(WORDS_PATH, "r") as f:
        acceptedWords = f.read().splitlines()

    session = GameSession(acceptedWords, handleFoundWord, doNothing, 3, 3)

    invalidWords = []

    os.system("cls")

    while(True):

        showSessionInfo(session)

        substring: str = input("Enter the substring: ").replace(" ", "")

        if substring == ":q":
            safeExit(invalidWords)
        
        if substring == ":r":
            reset(session)
            continue

        if substring == session.lastQueriedSubstring:
            invalidWords.append(session.lastFoundWord)

        if len(substring) > 3:
            os.system("cls")
            continue
            
        session.queryOnSubstring(substring)

        os.system("cls")