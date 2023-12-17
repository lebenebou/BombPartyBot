
from engine import Engine 

class GameSession:

    def __init__(self, acceptedWords: list[str], foundWordCallback, gameOverCallback, startingHearts: int = 3, maxHearts: int = 3):
        
        self.acceptedWords = acceptedWords

        self.originalLetterWeights = self.__generateLetterWeights()
        self.letterWeights = self.__generateLetterWeights()

        Engine.sortWords(self.acceptedWords, self.letterWeights)

        self.foundWordCallback = foundWordCallback
        self.gameOverCallback = gameOverCallback

        self.hearts = startingHearts
        self.maxHearts = maxHearts
        self.lostHearts = 0

        self.lastFoundWord = None
        self.lastQueriedSubstring = None

        self.turnsPlayed = 0
        self.heartRefills = 0

    def __generateLetterWeights(self) -> dict[chr, int]:

        letterWeight = {}
        for order in range(97, 97 + 26):
            letterWeight[chr(order)] = 1
        
        rareLetterWeight = {
            'j':7, 'v':7, 'q':7, 'w':5, 'y':5, 'z':5
        }
    
        letterWeight.update(rareLetterWeight)
        letterWeight['x'] = 0
        letterWeight['z'] = 0

        return letterWeight
    
    def __allLettersAreUsed(self) -> bool:
        return not any(self.letterWeights.values())

    def __resetLetterWeights(self):
        self.letterWeights = dict(self.originalLetterWeights)
    
    def averageTurnsPerRefill(self) -> float:
        return self.turnsPlayed / self.heartRefills
    
    def queryOnSubstring(self, substring: str) -> str:
        
        self.lastQueriedSubstring = substring
        self.turnsPlayed += 1
        self.lastFoundWord = Engine.playTurn(substring, self.acceptedWords, self.letterWeights, self.foundWordCallback)

        if self.lastFoundWord == None:

            self.hearts -= 1
            self.lostHearts =+1

            if self.hearts == 0:
                self.gameOverCallback()

            return None

        if self.__allLettersAreUsed():

            self.__resetLetterWeights()
            self.heartRefills += 1
            self.hearts = min(self.hearts + 1, self.maxHearts)

        
        return self.lastFoundWord

    def toDict(self) -> dict:

        return {
            "turn": self.turnsPlayed,
            "lastQueriedSubstring": self.lastQueriedSubstring,
            "lastFoundWord": self.lastFoundWord,
            "hearts": self.hearts,
            "refillCount": self.heartRefills,
            "unusedLetters": [letter for letter in self.letterWeights if self.letterWeights[letter] > 0],
       }