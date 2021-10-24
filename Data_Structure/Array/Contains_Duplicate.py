# Given an integer array nums, return true if any value appears 
# at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false





def containsDuplicate(nums):
    new_nums = set(nums)
    if len(new_nums) != len(nums):
            return True
    return False


print(containsDuplicate([2, 14, 18, 22, 22]))
