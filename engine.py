
class Engine:

    def __init__(self):
        pass

    @staticmethod
    def __distinctLetters(word: str) -> list[chr]:
        return list(set(word))

    @staticmethod
    def __assignValue(word: str, letterWeight: dict[chr, int]) -> int:

        value = 0
        letters = Engine.__distinctLetters(word)

        for letter in letters:
            value += letterWeight[letter]

        return value

    @staticmethod
    def __findFirst(substring: str, words: list[str]) -> tuple[int, str]:

        for index, word in enumerate(words):

            if substring in word:

                return (index, word)

        return (-1, "")
            
    @staticmethod
    def __removeWordAndReset(wordIndex: int, words: list[str], letterWeight: dict[chr, int]):

        foundWord = words[wordIndex]
        words[wordIndex] = ""

        for letter in foundWord:
            letterWeight[letter] = 0

        words.sort(key=lambda word: Engine.__assignValue(word, letterWeight), reverse=True)

    @staticmethod
    def playTurn(subtring: str, words: list[str], letterWeight: dict[chr, int], processWordCallback) -> str:

        foundIndex, foundWord = Engine.__findFirst(subtring, words)

        if foundIndex == -1:

            processWordCallback(None)
            return None
        
        processWordCallback(foundWord)
        Engine.__removeWordAndReset(foundIndex, words, letterWeight)

        return foundWord