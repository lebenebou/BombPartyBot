
#include "GameSession.hpp"

GameSession::GameSession(
    std::filesystem::path wordsFilePath,
    std::function<void(const std::string&)> foundWordCallback,
    std::function<void()> gameOverCallback,
    int startingHearts,
    int maxHearts
) : foundWordCallback(foundWordCallback), gameOverCallback(gameOverCallback), hearts(startingHearts), maxHearts(maxHearts), turnsPlayed(0), heartRefills(0), lostHearts(0)
{
    letterWeights = Engine::generateDefaultWeights();
    acceptedWords = Engine::fetchWordsFromFile(wordsFilePath);

    lastFoundWord = std::nullopt;
    lastQueriedSubtring = std::nullopt;
}

std::optional<std::string> GameSession::queryOnSubtring(const std::string& substring)
{
    lastQueriedSubtring = substring;
    ++turnsPlayed;

    lastFoundWord = Engine::playTurn(
        substring,
        acceptedWords,
        letterWeights,
        foundWordCallback
    );

    if (!lastFoundWord.has_value())
    {
        --hearts;
        ++lostHearts;

        if (hearts == 0)
            gameOverCallback();

        return std::nullopt;
    }

    if (allLettersAreUsed())
    {
        resetLetterWeights();
        ++heartRefills;
        hearts = std::min(hearts + 1, maxHearts);
    }

    return lastFoundWord;
}

bool GameSession::allLettersAreUsed()
{
    return std::all_of(
        letterWeights.begin(), letterWeights.end(),
        [](int i) { return i == 0; }
    );
}

void GameSession::resetLetterWeights()
{
    this->letterWeights = Engine::generateDefaultWeights();
}

double GameSession::averageTurnsPerRefill()
{
    return (double)turnsPlayed / (double)heartRefills;
}

std::string GameSession::toString()
{
    std::string repr;

    repr += "-- GameSession -- \n";
    repr += "turn: " + std::to_string(turnsPlayed) + "\n";
    repr += "query: " + (lastQueriedSubtring.has_value() ? lastQueriedSubtring.value() : "_null_") + "\n";
    repr += "foundWord: " + (lastFoundWord.has_value() ? lastFoundWord.value() : "_null_") + "\n";
    repr += "hearts: " + std::to_string(hearts) + "\n";

    std::vector<char> unusedLetters;
    for(int i = 0; i < letterWeights.size(); ++i)
        
        if (letterWeights[i])
            unusedLetters.push_back('a' + i);

    repr += "unusedLetters: ";
    for (char letter : unusedLetters)
        repr += std::string(1, letter) + " ";
    repr += "\n";

    repr += "heartRefills: " + std::to_string(heartRefills) + "\n";
    repr += "lostHearts: " + std::to_string(lostHearts) + "\n";
    repr += "-----------------";

    return repr;
}