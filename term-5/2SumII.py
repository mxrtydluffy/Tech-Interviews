# Two Sum II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

#_________________________________________________________________________________________________________________________________

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

#_________________________________________________________________________________________________________________________________

# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

#_________________________________________________________________________________________________________________________________

# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

#_________________________________________________________________________________________________________________________________

# Constraints:

# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

#                               Big O Notation
#                                   O(n^2)

def twoSumII(numbers, target):
    # Assign pointers then get the length of the last index of array
    left, right = 0, len(numbers) - 1

    while left < right:

        # The sum variable (s) left the left and right pointer elements
        s = numbers[left] + numbers[right]

        # if the sum is greater than target
        if s > target:
            # Move in opposite direction
            right -= 1
        # Move towards the front
        elif s < target:
            left += 1
        # If answer is found then return the current index
        else:
            return [left + 1, right + 1]
        
print(f" Example 1 Solution:", twoSumII([2,7,11,15], 9))
print(f" Example 2 Solution:", twoSumII([2,3,4], 6))
print(f" Example 3 Solution:", twoSumII([-1,0], -1))