# Given an integer array nums sorted in non-decreasing order, remove the duplicates
# such that each unique element appears only once. The relative order of the elements
# should be kept the same.

# ------------------------------------
def removeDuplicates(nums):
    return list(set(nums))

# ------------------------------------


# def removeDuplicates(nums):
    # x = 0
    # while x < len(nums)-1:
    #     if nums[x] == nums[x+1]:
    #         nums.remove(nums[x+1])
    #     else:
    #         x += 1
    # return nums


print(removeDuplicates([0, 0, 0, 0, 1, 2, 2, 2, 3, 4, 5, 7, 7]))
print(removeDuplicates([0, 1, 2, 3, 4, 5, 6, 7]))
print(removeDuplicates([1, 1, 2]))
