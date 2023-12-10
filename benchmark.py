
from GameSession import GameSession
import random
import json

def generateRandomSubtring(words: list[str], maxLength: int) -> str:

    word = random.choice(words)

    if len(word) <= maxLength:
        return word

    startIndex = random.randint(0, len(word) - maxLength)
    endIndex = startIndex + random.choice([2, maxLength])

    return word[startIndex:endIndex]

def onWordFound(word: str):

    pass

def onGameOver():

    pass

if __name__ == "__main__":

    session = GameSession("words10k.txt", onWordFound, onGameOver, 3, 3)

    turns = 50
    gameLog = []
    
    for roundNumber in range(turns):

        substring = generateRandomSubtring(session.acceptedWords, 3)
        session.queryOnSubstring(substring)
        gameLog.append(session.toDict())

    print(f"Played {turns} turns.")
    print(f"Lost {session.lostHearts} hearts.")
    print(f"Refilled hearts {session.heartRefills} times.")
    print(f"Current heart count: {session.hearts}")
    print(f"Average turns until refill: {session.averageTurnsPerRefill()}")

    with open("game_log.json", "w") as f:
        json.dump(gameLog, f, indent=4)

    print("\nGame Log written to game_log.json")