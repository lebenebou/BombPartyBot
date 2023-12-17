
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

if __name__ == "__main__":

    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    WORDS_FILE_PATH = os.path.join(CURRENT_DIR, "wordBank", "words60k.txt")

    acceptedWords = []
    with open(WORDS_FILE_PATH, "r") as f:
        acceptedWords = f.read().splitlines()

    session = GameSession(acceptedWords, handleFoundWord, doNothing, 3, 3)

    os.system("cls")

    while(True):

        if session.lastFoundWord is not None:
            print(f"Last found word: {session.lastFoundWord}\n")
        else:
            print("No word found.\n")

        substring: str = input("Enter the substring: ").replace(" ", "")
        session.queryOnSubstring(substring)

        os.system("cls")