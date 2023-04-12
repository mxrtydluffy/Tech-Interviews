# Original Question

# Given a pattern and a string s, find if s follows the same pattern.

#______________________________________________________________________________________________________________________________________

#                                                       Overview

#  * split function will give us a list of the four words.

# * 2 hashmaps to go from a letter to a word and a word to a letter
# * A word needs to map to a single character. 
# * Two words can't map to a single character
# * Time complexity is O(n+m) based on the total amount of character have on each strings.

#______________________________________________________________________________________________________________________________________

def problem(pattern: str, s: str) -> bool:
    # Get list of words for the string s and split it via space character.
    words = s.split(" ")
    # Then check if its going to be a valid solution.
    # Characters in pattern should be eqaul to the number of words we have
    # if not then return False solution isn't possible.
    if len(pattern) != len(words):
        return False
    
    # Initilize hashmaps to Map each character to the word.
    charToWord = {}
    # Initilize hashmaps to Map each word to the character. 
    wordToChar = {}

    # Iterate through both of the characters in patten and each word in our list at the same exact time
    # To do this use each character in each word and zip through them to iterate simutaneously.
    # zip chracters in pattern and the words in the list.
    for c, w in zip(pattern, words):
        # Check if this character maps to a different word.
        # Therefore looking c has a character in hashmap and the word that it maps to is not equal 
            # to this word we're currently looking at.
        
        if c in charToWord and charToWord[c] != w:
            # Returns False if patterns don't match.
            return False
        
        # Do the same for the opposite data structure.
        if w in wordToChar and wordToChar[w] != c:
            # Returns False if patterns don't match.
            return False

        # Add to hashmap for the first time or mapping to the word that's already in hashmap.
        charToWord[c] = w
        wordToChar[w] = c
    # If there are no mismataches the patterns match so we can return true
    return True

print(problem("yzyz","apples oranges apples oranges"))
print(problem("abba","apples oranges apples oranges"))
print(problem("popo","ramen boba ramen boba"))