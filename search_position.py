# Search Insert Position Question

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

#______________________________________________________________________________________________________________________________________

# Example 1
# Input: nums = [1,3,5,6], target = 5
# Output: 2

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize left and right corners. Minus 1 is the right most value.
        l, r = 0, len(nums) -1

        # Begin binary search
        # While left is less than right 
        while l <= r:
            # compute middle pointer to some fractions
            mid = (l + r) // 2

            # Check if equal to target
            if target == nums[mid]:
                return mid
            
            # Target is too big start searching to the right
            if target > nums[id]:
                l = mid + 1

            # Start searching to the left since the target is small
            else:
                r = mid - 1
        
        # If didn't return target return left pointer bc
            # if target is 1 and array of 2. Since 1 is less than 2 start searching to the left
        return l 