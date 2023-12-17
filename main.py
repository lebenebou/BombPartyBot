
from GameSession import GameSession
import pyautogui
import os

def switchApps():

    pyautogui.hotkey("alt", "tab")

def typeAndSubmit(word:str):

    if word is None:
        return

    pyautogui.typewrite(word, interval=0.25)
    pyautogui.press("enter")

def handleFoundWord(word: str):

    switchApps()
    typeAndSubmit(word)
    switchApps()

def doNothing():
    pass

if __name__ == "__main__":

    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    WORDS_FILE_PATH = os.path.join(CURRENT_DIR, "../wordBank/words10k.txt")

    session = GameSession(WORDS_FILE_PATH, handleFoundWord, doNothing, 3, 3)

    while(True):

        if session.lastFoundWord is not None:
            print(f"Last found word: {session.lastFoundWord}\n")

        substring: str = input("Enter the substring: ").replace(" ", "")
        session.queryOnSubstring(substring)

        os.system("cls")