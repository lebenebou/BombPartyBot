# BombPartyBot
A bot capable of playing [BombParty](https://jklm.fun/) without ever losing. With heavy emphasis on efficiency when it comes to refilling hearts by using up all letters.

## Game Rules
Each turn, you are given a substring of 2 or 3 letters. You (or your bot) must provide a word which contains that substring.
### Example
Subtring is "ppl"; you provide "apple". (Turn 1)
Subtring is "ng"; you provide "orange". (Turn 2)

In these 2 turns, you've used up the letters "a, p, l, e, o, r, n, g".
You must use all letters of the alphabet in as few turns as possible.

## Implemented Engines
### 1. Basic Engine
Finds the first word which contains the subtring.

### 2. Greedy Engine
Everytime a substring is given, it goes through all words to find the best one to use.

### 3. Prioritizer Engine
Takes advantage of pre-processing. Sorts all the accepted words by most relevant.
Each time a substring is given, goes through the already sorted word list to find the first word containing the subtring.
Re-sort the words after each turn.

## A Hunger For Efficiency
Prioritizer engine is by far the fastest. Think you can implement a faster one? Create a pull request!
