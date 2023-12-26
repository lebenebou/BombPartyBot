
import os
import sys
sys.path.append("./Engines")

from Engines.BombPartyEngine import BombPartyEngine
from Engines.Prioritizer import Prioritizer

import pyautogui

def FocusChromeAndInputWord(word: str):

    if word is None:
        return

    pyautogui.hotkey("win", "4")
    pyautogui.typewrite(word, interval=0.1)
    pyautogui.press("enter")
    pyautogui.hotkey("alt", "tab")

def safeExit():
    exit(0)

def getValueFromInput(intputMessage: str) -> any:
    
    intputMessage = intputMessage.strip().strip(":") + ": "
    os.system("cls")

    value = input(intputMessage).strip().lower()
    return value

def handleCommand(command: str, engine: BombPartyEngine):

    command = command.strip(":")

    if command == "q":
        safeExit()
        return

    elif command == "r":
        engine.reset()
        return

    elif command == "h":
        engine.hearts = int(getValueFromInput(intputMessage="Set heart count"))
        return

    elif command == "m":
        engine.maxHearts = int(getValueFromInput(intputMessage="Set max heart count")) 
        return

    elif command == "l":

        letters = str(getValueFromInput(intputMessage="Set letters left"))
        engine.setLettersLeft(list(letters))
        return

    elif command == "u":

        letters = str(getValueFromInput(intputMessage="letters to use up"))
        engine.useLetters(list(letters))
        return

    elif command == "z":
        engine.unuseLastWord()
        return

def showMainScreen(engine: BombPartyEngine):

    if engine.lastFoundWord is not None:
        print(f"Last found word: {engine.lastFoundWord}", end="\n\n")

    print("Commands:")
    print("(:r) reset")
    print("(:z) unuse last word")
    print("(:u) use letters")
    print("(:l) set letters left")

    print()
    print("\t", " ".join(engine.unusedLetters()))
    print()

    print(f"Hearts: {engine.hearts}", "\t(:h) set")
    print(f"Max Hearts: {engine.maxHearts}", "\t(:m) set")
    print()
    
if __name__=="__main__":

    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    WORDS_FILE = os.path.join(CURRENT_DIR, "WordBank", "BombPartyDictionary.txt")

    words = []
    with open(WORDS_FILE) as f:
        words = f.read().splitlines()

    engine = Prioritizer(words, FocusChromeAndInputWord)

    while True:

        os.system("cls")

        showMainScreen(engine)

        substring = input("Enter substring or command: ").strip().lower()

        if substring.startswith(":"):

            handleCommand(substring, engine)
            continue

        engine.queryOnSubstring(substring)