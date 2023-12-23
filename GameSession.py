
import os
import sys
sys.path.append("./Engines")

from Engines.Prioritizer import Prioritizer
from Engines.SubstringMapper import SubstringMapper

if __name__=="__main__":

    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    WORDS_FILE = os.path.join(CURRENT_DIR, "WordBank", "BombPartyDictionary.txt")

    words = []
    with open(WORDS_FILE) as f:
        words = f.read().splitlines()

    prioritizer = Prioritizer(words, lambda word : print(f"Prioritizer found word: {word}"))
    prioritizer.queryOnSubstring("fr")
    print(f"Found in {prioritizer.lastResponseTimeMs} ms")

    print()

    mapper = SubstringMapper(words, lambda word : print(f"Mapper found word: {word}"))
    mapper.queryOnSubstring("fr")
    print(f"Found in {mapper.lastResponseTimeMs} ms")