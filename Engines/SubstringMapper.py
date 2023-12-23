
from BombPartyEngine import BombPartyEngine

import os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
SUBSTRINGS_FOLDER = os.path.join(CURRENT_DIR, "..", "Wordbank", "Substrings")


class SubstringMapper(BombPartyEngine):

# PUBLIC
    def __init__(self, acceptedWords: list[str], foundWordCallback: callable, gameOverCallback: callable = None, letterWeights: dict[chr, int] = None, startingHearts: int = 3, maxHearts: int = 3):

        super().__init__(acceptedWords, foundWordCallback, gameOverCallback, letterWeights, startingHearts, maxHearts)
        self.usedWords = set()
        
# PROTECTED
    # Override
    def _rebalance(self):
        self.usedWords.add(self.lastFoundWord)

    # Override
    def _quickFind(self, substring: str) -> str:

        fileName = substring + ".txt"
        filePath = os.path.join(SUBSTRINGS_FOLDER, fileName)

        candidates = []
        with open(filePath) as f:
            candidates = f.read().splitlines()

        maxValue = 0
        argMax: str = None

        for word in candidates:

            if word in self.usedWords:
                continue

            value = self._assignValue(word)

            if value > maxValue:
                maxValue = value
                argMax = word

        return argMax