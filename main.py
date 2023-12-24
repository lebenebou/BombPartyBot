
import os
import sys
sys.path.append("./Engines")

from Engines.Prioritizer import Prioritizer
from Engines.SubstringMapper import SubstringMapper
from Engines.BasicEngine import BasicEngine

if __name__=="__main__":

    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    WORDS_FILE = os.path.join(CURRENT_DIR, "WordBank", "BombPartyDictionary.txt")

    words = []
    with open(WORDS_FILE) as f:
        words = f.read().splitlines()

    callback = lambda word : print(f"Found word: {word}")
    substring = "au"

    prioritizer = Prioritizer(words, callback)
    prioritizer.queryOnSubstring(substring)
    print(f"Found in {prioritizer.lastResponseTimeMs} ms")

    print()

    mapper = SubstringMapper(words, callback)
    mapper.queryOnSubstring(substring)
    print(f"Found in {mapper.lastResponseTimeMs} ms")

    print()

    basic = BasicEngine(words, callback)
    mapper.queryOnSubstring(substring)
    print(f"Found in {mapper.lastResponseTimeMs} ms")