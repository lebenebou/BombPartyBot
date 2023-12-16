
#include "GameSession.hpp"
#include <filesystem>

int main(int argc, char const *argv[])
{
    auto currentDir = std::filesystem::current_path();
    auto wordsFilePath = currentDir / "..\\wordBank\\words10k.txt";

    auto foundWordCallback = [](const std::string& w) { std::cout << "Word found: " << w << std::endl; };
    auto gameOverCallback = [](){};

    auto session = GameSession(wordsFilePath, foundWordCallback, gameOverCallback);
    session.queryOnSubtring("ab");

    std::cout << session.toString() << std::endl;

    return 0;
}