
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

        if len(self.acceptedWords) == 0:
            return None

        wordsIterator = enumerate(self.acceptedWords)

        if self.hearts >= self.maxHearts:
            wordsIterator = reversed(list(wordsIterator))

        for index, word in wordsIterator:

            if substring not in word:
                continue

            self.acceptedWords[index] = ""
            return word

        return None

    # Override
    def _rebalance(self):
        self.__prioritizeWords()
        
# PRIVATE
    def __prioritizeWords(self):
        self.acceptedWords.sort(key=lambda word: self._assignValue(word), reverse=True)