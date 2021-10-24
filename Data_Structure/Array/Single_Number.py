# Given a non-empty array of integers nums, every element appears
# twice except for one. Find that single one.


def singleNumber(nums):
    new_nums = set(nums)
    for i in new_nums:
        if nums.count(i) == 1:
            return i
    return None


print(singleNumber([2, 2, 14, 18, 18, 22, 22]))
