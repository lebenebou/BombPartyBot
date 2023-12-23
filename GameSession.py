
import os
import sys
sys.path.append("./Engines")

from Engines.Prioritizer import Prioritizer

if __name__=="__main__":

    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    WORDS_FILE = os.path.join(CURRENT_DIR, "WordBank", "BombPartyDictionary.txt")

    words = []
    with open(WORDS_FILE) as f:
        words = f.read().splitlines()

    engine = Prioritizer(words, lambda word : print(f"Found word: {word}"))
    engine.queryOnSubstring("fr")