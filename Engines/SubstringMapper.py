
from BombPartyEngine import BombPartyEngine

import os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
SUBSTRINGS_FOLDER = os.path.join(CURRENT_DIR, "..", "Wordbank", "Substrings")

class SubstringMapper(BombPartyEngine):

# PUBLIC
    def __init__(self, acceptedWords: list[str], foundWordCallback: callable, gameOverCallback: callable = None, letterWeights: dict[chr, int] = None, startingHearts: int = 2, maxHearts: int = 3):

        super().__init__(acceptedWords, foundWordCallback, gameOverCallback, letterWeights, startingHearts, maxHearts)
        self.usedWords: list[str] = []
        
    # Override
    def reset(self):

        super().reset()
        self.usedWords.clear()

# PROTECTED
    # Override
    def _quickFind(self, substring: str) -> str:

        fileName = substring + ".txt"
        filePath = os.path.join(SUBSTRINGS_FOLDER, fileName)

        candidates = []
        with open(filePath) as f:
            candidates = f.read().splitlines()

        if self.hearts < self.maxHearts:
            return max(candidates, key = lambda word : 0 if self.__isAlreadyUsed(word) else self._assignValue(word))

        for candidate in candidates:

            if self.__isAlreadyUsed(candidate):
                continue

            return candidate

        return None

    # Override
    def _rebalance(self):
        self.usedWords.append(self.lastFoundWord)

# PRIVATE
    def __isAlreadyUsed(self, word: str) -> bool:
        return word in self.usedWords