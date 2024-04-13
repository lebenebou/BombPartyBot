
import sys
sys.path.append("./Engines")

import os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
BENCHMARK_FOLDER = os.path.join(CURRENT_DIR, "BenchmarkResults")

import json
from random import shuffle

from Engines.BombPartyEngine import BombPartyEngine
from Engines.BasicEngine import BasicEngine
from Engines.GreedyEngine import GreedyEngine
from Engines.Prioritizer import Prioritizer
    
def benchmarkEngine(engine: BombPartyEngine, substrings: list[str], saveFolder: str = BENCHMARK_FOLDER) -> dict:

    if not os.path.exists(saveFolder):
        os.mkdir(saveFolder)

    gameLog: list[dict] = []

    for substring in substrings:

        engine.queryOnSubstring(substring)
        gameLog.append(engine.toDict())

    jsonFilePath = os.path.join(saveFolder, f"{engine.__class__.__name__}Gamelog.json")
    with open(jsonFilePath, "w") as f:
        json.dump(gameLog, f, indent=4)

    print(f"Saved game log to {jsonFilePath}")

    turnsPlayed = len(substrings)

    return {
        "engine": engine.__class__.__name__,
        "turnsPlayed": turnsPlayed,
        "heartsLost": engine.lostHearts,
        "heartRefills": engine.heartRefills,
        "averageTurnsPerRefill": -1 if not engine.heartRefills else turnsPlayed / engine.heartRefills,
        "averageResponseTimeMs": sum([turn["responseTimeMs"] for turn in gameLog]) / turnsPlayed,
    }

if __name__ == "__main__":

    if not os.path.exists(BENCHMARK_FOLDER):
        os.mkdir(BENCHMARK_FOLDER)

    foundWordCallback = lambda word : None
    gameOverCallback = None

    WORDS_FILE = os.path.join(CURRENT_DIR, "WordBank", "BombPartyDictionary.txt")

    words = []
    with open(WORDS_FILE) as f:
        words = f.read().splitlines()

    substrings = ["ti", "ese", "el", "erm", "oat", "pic", "eu", "ro", "nes", "pri", "ide", "er", "nd", "led", "et", "ela", "ise", "uri", "te", "enn", "in", "pi", "to", "od", "rd", "mi", "er", "men", "ort", "re", "pol", "tes", "ly", "olo", "lay", "ref", "bin", "un", "ome", "rea", "end"]
    shuffle(substrings)
    iterations = len(substrings)

    basic = BasicEngine(words, foundWordCallback, maxHearts=iterations)
    greedy = GreedyEngine(words, foundWordCallback, maxHearts=iterations)
    prioritizer = Prioritizer(words, foundWordCallback, maxHearts=iterations)

    print("Benchmarking...", flush=True)
    engineLogs = []

    engineLogs.append(benchmarkEngine(basic, substrings))
    engineLogs.append(benchmarkEngine(greedy, substrings))
    engineLogs.append(benchmarkEngine(prioritizer, substrings))

    benchmarkResultsFileName = "BenchmarkResults.json"
    benchmarkResultsFilePath = os.path.join(BENCHMARK_FOLDER, benchmarkResultsFileName)

    with open(benchmarkResultsFilePath, "w") as f:
        json.dump(engineLogs, f, indent=4)

    print()
    print(f"Saved benchmark results to {benchmarkResultsFilePath}")