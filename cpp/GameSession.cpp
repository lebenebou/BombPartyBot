
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