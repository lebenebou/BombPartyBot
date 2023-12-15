
import engine

class GameSession:

    def __init__(self, wordsFilePath: str, foundWordCallback, gameOverCallback, startingHearts: int = 3, maxHearts: int = 3):
        
        self.letterWeights = engine.generateDefaultWeights()
        self.acceptedWords = engine.getWordsFromFile(wordsFilePath)
        self.maxHearts = maxHearts

        self.foundWordCallback = foundWordCallback
        self.gameOverCallback = gameOverCallback

        self.turnsPlayed = 0
        self.lastFoundWord = None
        self.lastQueriedSubstring = None
        self.hearts = startingHearts
        self.heartRefills = 0
        self.lostHearts = 0


    def allLettersAreUsed(self) -> bool:

        return not any(self.letterWeights.values())

    def resetLetterWeights(self):

        self.letterWeights = engine.generateDefaultWeights()
    
    def averageTurnsPerRefill(self) -> float:

        return self.turnsPlayed / self.heartRefills
    
    def queryOnSubstring(self, substring: str) -> str:
        
        self.lastQueriedSubstring = substring
        self.turnsPlayed += 1
        self.lastFoundWord = engine.playTurn(substring, self.acceptedWords, self.letterWeights, self.foundWordCallback)

        if self.lastFoundWord == None:

            self.hearts -= 1
            self.lostHearts =+1

            if self.hearts == 0:
                self.gameOverCallback()

            return None

        if self.allLettersAreUsed():

            self.resetLetterWeights()
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