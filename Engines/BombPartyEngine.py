
import os
import json

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_WEIGHTS_FILE = os.path.join(CURRENT_DIR, "defaultLetterWeights.json")

def getDefaultLetterWeights() -> dict[chr, int]:

    with open(DEFAULT_WEIGHTS_FILE) as f:
        return json.load(f)

class BombPartyEngine:

# PUBLIC
    def __init__(self, acceptedWords: list[str], foundWordCallback: callable, gameOverCallback: callable = None, letterWeights: dict[chr, int] = None, startingHearts: int = 3, maxHearts: int = 3):

        self.acceptedWords: list[str] = acceptedWords

        if(letterWeights == None):
            self.letterWeights:dict[chr, int] = getDefaultLetterWeights()
        else:
            self.letterWeights:dict[chr, int] = letterWeights

        self.turnsPlayed = 0
        self.hearts: int = startingHearts
        self.maxHearts: int = maxHearts

        self.heartRefills = 0
        self.lostHearts = 0

        self.foundWordCallback: callable = foundWordCallback
        self.gameOverCallback: callable = gameOverCallback

        self.lastFoundWord: str = None
        self.lastQueriedSubstring: str = None
        self.lastResponseTimeMs: float = 0


    def averageTurnsPerRefill(self) -> float:
        return self.turnsPlayed / self.heartRefills

    def queryOnSubstring(self, substring: str) -> str:
        raise NotImplementedError("This is an abstract method, please use a subclass")

    def toDict(self) -> dict:

        return {
            "turn": self.turnsPlayed,
            "lastQueriedSubstring": self.lastQueriedSubstring,
            "lastFoundWord": self.lastFoundWord,
            "hearts": self.hearts,
            "refillCount": self.heartRefills,
            "unusedLetters": [letter for letter in self.letterWeights if self.letterWeights[letter] > 0],
        }

# PRIVATE
    def __allLettersAreUsed(self) -> bool:
        return not any(self.letterWeights.values())