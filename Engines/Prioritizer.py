
from BombPartyEngine import BombPartyEngine

class Prioritizer(BombPartyEngine):

# PUBLIC
    def __init__(self, acceptedWords: list[str], foundWordCallback: callable, gameOverCallback: callable = None, letterWeights: dict[chr, int] = None, startingHearts: int = 3, maxHearts: int = 3):

        super().__init__(acceptedWords, foundWordCallback, gameOverCallback, letterWeights, startingHearts, maxHearts)

        self.lastFoundWordIndex: int = -1
        self.__prioritizeWords()

    # Override
    def reset(self):

        super().reset()
        self.lastFoundWordIndex = -1
        self.__prioritizeWords()
        
# PROTECTED
    # Override
    def _quickFind(self, substring: str) -> str:

        for index, word in enumerate(self.acceptedWords):

            if substring not in word:
                continue

            self.lastFoundWordIndex = index
            return word

        return None

    # Override
    def _rebalance(self):

        if self.lastFoundWordIndex != -1:
            self.acceptedWords[self.lastFoundWordIndex] = ""

        self.acceptedWords.sort(key=lambda word: self._assignValue(word), reverse=True)
        
        while len(self.acceptedWords) > 0 and self.acceptedWords[-1] == "":
            self.acceptedWords.pop()

# PRIVATE
    def __prioritizeWords(self):
        self.acceptedWords.sort(key=lambda word: self._assignValue(word), reverse=True)