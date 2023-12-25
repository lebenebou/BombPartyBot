
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

def markAsInvalid(word: str):
    pass

def handleCommand(command: str, engine: BombPartyEngine):

    command = command.strip(":")

    if command == "q":
        safeExit()
        return

    elif command == "r":
        engine.reset()
        return

    elif command == "i":
        markAsInvalid(engine.lastFoundWord)
        return

    elif command.startswith("h"):
        engine.hearts = int(command[1])
        return

    elif command.startswith("m"):
        engine.maxHearts = int(command[1])
        return

    elif command.startswith("l"):
        engine.setLettersLeft(list(command[1:]))
        return

    elif command.startswith("u"):
        engine.useLetters(list(command[1:]))
        return

    elif command.startswith("z"):
        engine.unuseLastWord()
        return

def showEngineInfo(engine: BombPartyEngine):

    if engine.lastFoundWord is not None:
        print(f"Found word: {engine.lastFoundWord}", end="\n\n")

    print("(:r) reset")
    print("(:z) unuse last word")
    print("(:i) last word is invalid")
    print("(:u) use letters")
    print("(:l) set letters left")
    print()
    print("\t", "".join(engine.unusedLetters()))
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

        showEngineInfo(engine)

        substring = input("Enter substring or command: ").strip().lower()

        if substring.startswith(":"):

            handleCommand(substring, engine)
            continue

        engine.queryOnSubstring(substring)