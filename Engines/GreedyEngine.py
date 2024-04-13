
from BombPartyEngine import BombPartyEngine

import os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
SUBSTRINGS_FOLDER = os.path.join(CURRENT_DIR, "..", "Wordbank", "Substrings")

class GreedyEngine(BombPartyEngine):

# PUBLIC
    def __init__(self, acceptedWords: list[str], foundWordCallback: callable, gameOverCallback: callable = None, letterWeights: dict[chr, int] = None, startingHearts: int = 2, maxHearts: int = 3):

        super().__init__(acceptedWords, foundWordCallback, gameOverCallback, letterWeights, startingHearts, maxHearts)
        self.usedWords = set()

    # Override
    def reset(self):
        super().reset()

# PROTECTED
    # Override
    def _quickFind(self, substring: str) -> str:

        bestWord: str = None
        bestScore: int = -1

        for word in self.acceptedWords:

            if self.__isAlreadyUsed(word) or substring not in word:
                continue

            score = self._assignValue(word)
            if score > bestScore:
                bestWord = word
                bestScore = score

        return bestWord

    # Override
    def _rebalance(self):
        self.usedWords.add(self.lastFoundWord)

# PRIVATE
    def __isAlreadyUsed(self, word: str) -> bool:
        return word in self.usedWords