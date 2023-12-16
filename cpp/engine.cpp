
#include "Engine.hpp"

std::vector<std::string> Engine::fetchWordsFromFile(const std::string& filename) {
    
    std::vector<std::string> words;
    std::ifstream file(filename);

    if (!file.is_open())
        std::cerr << "Error: Unable to open file " << filename << std::endl;

    std::string line;

    while (std::getline(file, line)) {
        std::istringstream iss(line);
        while (iss) {
            std::string word;
            iss >> word;

            if (!word.empty())
                words.push_back(word);
        }
    }

    file.close();
    return words;
}

std::array<int, 26> Engine::generateDefaultWeights() {

    std::array<int, 26> weight;
    std::fill(weight.begin(), weight.end(), 1);

    weight['j' - 'a'] = 7;
    weight['v' - 'a'] = 7;
    weight['q' - 'a'] = 7;
    weight['w' - 'a'] = 5;
    weight['y' - 'a'] = 5;
    weight['z' - 'a'] = 5;

    return weight;
}

std::optional<std::string> Engine::playTurn(const std::string& substring, std::vector<std::string>& words, std::array<int, 26>& letterWeight, std::function<void(const std::string&)> callback) {

    auto foundWord = findFirstMatch(substring, words);

    if (!foundWord.has_value())
        return std::nullopt;

    callback(foundWord.value().second);

    removeWordAndRebalance(foundWord.value().first, words, letterWeight);

    return foundWord.value().second;
}

bool Engine::containsSubtring(const std::string& word, const std::string& substring) {

    return word.find(substring) != std::string::npos;
}

int Engine::assignValue(const std::string& word, const std::array<int, 26>& letterWeight) {

    int value = 0;

    for (char letter : word)
        value += letterWeight[letter - 'a'];

    return value;
}

std::optional<std::pair<size_t, std::string>> Engine::findFirstMatch(const std::string& substring, const std::vector<std::string>& words) {

    auto it = std::find_if(words.begin(), words.end(), [&substring](const std::string& word) { return containsSubtring(word, substring); });

    if (it == words.end())
        return std::nullopt;

    return std::make_pair(std::distance(words.begin(), it), *it);
}

void Engine::removeWordAndRebalance(int foundWordIndex, std::vector<std::string>& words, std::array<int, 26>& letterWeight) {

    for (char letter : words.at(foundWordIndex))
        letterWeight[letter - 'a'] = 0;

    words.at(foundWordIndex) = "";
    std::sort(words.begin(), words.end(), [&letterWeight](const std::string& w1, const std::string& w2) { return assignValue(w1, letterWeight) > assignValue(w2, letterWeight); });

    while (!words.empty() && words.back() == "")
        words.pop_back();
}