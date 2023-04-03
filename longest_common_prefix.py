# Question

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

#_________________________________________________________________________________________________________________________________

# Example 1
# Input: strs = ["flower","flow","flight"]
# Output: "fl"


def longestCommonPrefix(strs: List[str]) -> str:
    res = ""

    for i in range(len(str[0])):
        # s in the list of strings given check if every single string at 
        # index i are the same.
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
    return  res
    

#                                   Pseudocode
# Begin by initiaizing the result that is an empty string. This is used if no common prefix is used.
# Simultaneously iterate through all the index of strings by using a for loop. Look for every single character
    # of the first string str[0] since it can be possible this string is not the shortest string in the input.
    # Must be handled rather than using a conditional.
# After reiterating through every index, reiterate through every single string and make sure all the strings have
    # the exact same character at index i.
# Initially, since i is in bounds of the first string from what is being iterated yet, s[i] might be out of bounds
# need to make sure is in bounds by using a or statement.
# Lastly return output.