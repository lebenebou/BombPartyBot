
from BombPartyEngine import BombPartyEngine

class Prioritizer(BombPartyEngine):

# PUBLIC
    def __init__(self, acceptedWords: list[str], foundWordCallback: callable, gameOverCallback: callable = None, letterWeights: dict[chr, int] = None, startingHearts: int = 2, maxHearts: int = 3):

        super().__init__(acceptedWords, foundWordCallback, gameOverCallback, letterWeights, startingHearts, maxHearts)
        self.__prioritizeWords()

    # Override
    def reset(self):

        super().reset()
        self.__prioritizeWords()
        
# PROTECTED
    # Override
    def _quickFind(self, substring: str) -> str:

        index, increment = 0, 1

        if self.hearts == self.maxHearts:
            index, increment = -1, -1

        while abs(index) <= len(self.acceptedWords):

            word = self.acceptedWords[index]

            if substring in word:

                self.acceptedWords[index] = ""
                return word

            index += increment

        return None

    # Override
    def _rebalance(self):
        self.__prioritizeWords()
        
# PRIVATE
    def __prioritizeWords(self):
        self.acceptedWords.sort(key=lambda word: self._assignValue(word), reverse=True)