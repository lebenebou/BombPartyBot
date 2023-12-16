
#ifndef GAMESESSION_HPP
#define GAMESESSION_HPP

#include "engine.hpp"
#include <functional>
#include <vector>
#include <array>
#include <optional>
#include <filesystem>

class GameSession {

private:
    std::array<int, 26> letterWeights;
    std::vector<std::string> acceptedWords;

    std::function<void(const std::string&)> foundWordCallback;
    std::function<void()> gameOverCallback;

    std::optional<std::string> lastFoundWord;
    std::optional<std::string> lastQueriedSubtring;

    int hearts;
    int maxHearts;

    int turnsPlayed;
    int heartRefills;
    int lostHearts;

public:
    GameSession(
        std::filesystem::path wordsFilePath,
        std::function<void(const std::string&)> foundWordCallback,
        std::function<void()> gameOverCallback,
        int startingHearts = 3,
        int maxHearts = 3
    );

    std::optional<std::string> queryOnSubtring(const std::string& substring);

    bool allLettersAreUsed();
    void resetLetterWeights();
    double averageTurnsPerRefill();
};

#endif // GAMESESSION_HPP