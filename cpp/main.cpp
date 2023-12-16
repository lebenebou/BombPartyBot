
#include "engine.hpp"
#include <filesystem>

int main(int argc, char const *argv[])
{
    const auto currentPath = std::filesystem::current_path();
    const auto wordsFilePath = currentPath / std::filesystem::path("wordBank\\words10k.txt");

    std::vector<std::string> words = Engine::fetchWordsFromFile((wordsFilePath).string());
    std::array<int, 26> letterWeight = Engine::generateDefaultWeights();
    
    while(true)
    {
        std::string subtring;
        std::cout << "Enter substring: ";
        std::cin >> subtring;

        auto foundWord = Engine::playTurn(subtring, words, letterWeight, [](const std::string& word) { return; });

        if(!foundWord.has_value())
        {
            std::cout << "No word found" << std::endl;
            continue;
        }

        std::cout << "Word found: " << foundWord.value() << std::endl;
        std::cout << std::endl;

        if(std::all_of(letterWeight.begin(), letterWeight.end(), [](int i) { return i == 0; }))
        {
            std::cout << "Used all letters." << std::endl;
            exit(0);
        }
    }

    return 0;
}