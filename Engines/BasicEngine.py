
from BombPartyEngine import BombPartyEngine

import os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
SUBSTRINGS_FOLDER = os.path.join(CURRENT_DIR, "..", "Wordbank", "Substrings")

class BasicEngine(BombPartyEngine):

# PUBLIC
    def __init__(self, acceptedWords: list[str], foundWordCallback: callable, gameOverCallback = lambda word: None, letterWeights: dict[chr, int] = None, startingHearts: int = 3, maxHearts: int = 3):
        
        super().__init__(acceptedWords, foundWordCallback, gameOverCallback, letterWeights, startingHearts, maxHearts)
        self.usedWords = set()

    # Override
    def reset(self):

        super().reset()
        self.usedWords.clear()

# PROTECTED
    # Override
    def _quickFind(self, substring: str) -> str:

        for word in self.acceptedWords:

            if substring in word and not self.__isAlreadyUsed(word):
                return word

        return None

    # Override
    def _rebalance(self):
        self.usedWords.add(self.lastFoundWord)

# PRIVATE
    def __isAlreadyUsed(self, word: str) -> bool:
        return word in self.usedWords