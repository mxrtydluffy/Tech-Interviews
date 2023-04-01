# Question

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

'''
Symbol  Value
I       1
V       5
X       10
L       50
C       100
D       500
M       1000
'''

# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. 
# The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
# Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
# The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

#_____________________________________________________________________________________________________________________________________

# Example 1

# Input: s = "III"
# Output: 3
# Explanation: III = 3.

#______________________________________________________________________________________________________________________________________

# Example 2

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.


def romanToInt(s):

    roman = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000 
    }
    
    result = 0

    for i in range(len(s)- 1):
        if roman[s[i]] < roman[s[i + 1]]:
            result -= roman[s[i]]
        else:
            result += roman[s[i]]
    
    return result + roman[s[-1]]

print(romanToInt("III"))
print((romanToInt("LVIII")))


#                                          Pseudocode
# 1.) Create a function that checks of what values of the symbols are next to each other. 
    # If its from largest to smallest then add. If smallest then largest subtract the smallest.
# 2.) Place a key value lets say "s" in the parameter which will be a place holder for the argument.
# 3.) Create a dictionary that corresponds to the correct symbol and value.
# 4.) Declare a result variable and set it to 0 which will accumulate the total value
    # as the roman numeral is added up.
# 5.) Reiterate throughout input string by checking if we're subtracting the value.
    # i + 1 makes sure to not be negative then get value of index i by accessing the roman index map by passing
    # the key value chracter s and i which is index. Place < symbol to see if its smaller than the next character.
# 6.) However if its in an increasing order the smaller value must be subtracted (roman[s[i]]) from the result. To do this,
    # result -= will subtract it from the result.
# 7.) Otherwise the else case is to add the roman value of the particular character.
# 8.) Outside of function use a print state to print the function and input any roman numeral. 