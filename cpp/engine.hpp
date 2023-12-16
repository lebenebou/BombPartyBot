
#ifndef ENGINE_HPP
#define ENGINE_HPP

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <array>
#include <functional>
#include <algorithm>
#include <optional>

class Engine {
public:
    static std::vector<std::string> fetchWordsFromFile(const std::string&);
    static std::array<int, 26> generateDefaultWeights();
    static std::optional<std::string> playTurn(const std::string&, std::vector<std::string>&, std::array<int, 26>&, std::function<void(const std::string&)>);

private:
    static bool containsSubtring(const std::string&, const std::string&);
    static int assignValue(const std::string&, const std::array<int, 26>&);
    static std::optional<std::pair<size_t, std::string>> findFirstMatch(const std::string&, const std::vector<std::string>&);
    static void removeWordAndRebalance(int, std::vector<std::string>&, std::array<int, 26>&);
};

#endif // ENGINE_HPP