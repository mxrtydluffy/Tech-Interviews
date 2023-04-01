# Question

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

#_________________________________________________________________________________________________________________________________#

# Example 1

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums, target):
    count = 1
    for ind in range(0,len(nums)):
        for ind2 in range(count,len(nums)):
            if (nums[ind] + nums[ind2]) == target:
                print("Found!")
                return [ind, ind2]
        count += 1

print(two_sum([3, 2, 4], 6))

#                                   Pseudocode
# Create a function that takes in two parameters, which is the number and the maximum target value.
# Set the inital count to one so python knows where to begin.
# Add a for loop to loop in the index in range. Values in range from 0 to the length of the numbers present.
# Inside that for loop another for loop is added to make sure the range is monitring the count of the length of numbers.
# From there is vital to check when to stop at the target. If found the function will then print found and return the values.


# Solution [1, 2]