
import time
from copy import deepcopy

import sys
sys.path.append("..")

import os
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_WEIGHTS_FILE = os.path.join(CURRENT_DIR, "defaultLetterWeights.json")

import json
def getDefaultLetterWeights() -> dict[chr, int]:

    with open(DEFAULT_WEIGHTS_FILE) as f:
        return json.load(f)

class BombPartyEngine:

# PUBLIC
    def __init__(self, acceptedWords: list[str], foundWordCallback: callable, gameOverCallback: callable = lambda word: None, letterWeights: dict[chr, int] = None, startingHearts: int = 3, maxHearts: int = 3):

        self.acceptedWords: list[str] = acceptedWords

        if(letterWeights is None):
            self.letterWeights:dict[chr, int] = getDefaultLetterWeights()
        else:
            self.letterWeights:dict[chr, int] = letterWeights

        self.originalLetterWeights: dict[chr, int] = self.letterWeights.copy()

        self.turnsPlayed = 0
        self.hearts: int = startingHearts
        self.maxHearts: int = maxHearts

        self.heartRefills: int = 0
        self.lostHearts: int = 0

        self.foundWordCallback: callable = foundWordCallback
        self.gameOverCallback: callable = gameOverCallback

        self.lastFoundWord: str = None
        self.lastQueriedSubstring: str = None
        self.lastResponseTimeMs: float = 0

        self._initialState = deepcopy(self.__dict__)

    def reset(self):
        self.__dict__.update(deepcopy(self._initialState))

    def unusedLetters(self) -> list[chr]:
        return [letter for letter in self.letterWeights if self.letterWeights[letter] > 0]

    def queryOnSubstring(self, substring: str) -> str:
        
        timerStart = time.time()
        foundWord = self._quickFind(substring)
        self.lastResponseTimeMs = (time.time() - timerStart) * 1000

        self.foundWordCallback(foundWord)

        self.turnsPlayed += 1
        self.lastFoundWord = foundWord
        self.lastQueriedSubstring = substring

        if foundWord is None:

            self.hearts -= 1
            self.lostHearts += 1

            if self.hearts == 0:
                self.gameOverCallback()

            return None

        for letter in foundWord:
            self.letterWeights[letter] = 0

        if self._allLettersAreUsed():

            self.hearts = min(self.hearts + 1, self.maxHearts)
            self.heartRefills += 1
            self._resetLetterWeights()

        self._rebalance()
        return foundWord

    def toDict(self) -> dict:

        return {
            "turn": self.turnsPlayed,
            "queriedSubstring": self.lastQueriedSubstring,
            "foundWord": self.lastFoundWord,
            "responseTimeMs": self.lastResponseTimeMs,
            "hearts": self.hearts,
            "lostHearts": self.lostHearts,
            "refillCount": self.heartRefills,
            "unusedLetters": [letter for letter in self.letterWeights if self.letterWeights[letter] > 0],
        }

# PROTECTED
    def _assignValue(self, word: str) -> int:
        # return the sum of the disctinct letters' weights
        return sum([self.letterWeights[letter] for letter in set(word)])

    def _allLettersAreUsed(self) -> bool:
        return not any(self.letterWeights.values())

    def _resetLetterWeights(self):
        self.letterWeights = self.originalLetterWeights.copy()

    def _quickFind(self, subtring: str) -> str:
        raise NotImplementedError("This is a virtual method. Please override it.")

    def _rebalance(self):
        raise NotImplementedError("This is a virtual method. Please override it.")