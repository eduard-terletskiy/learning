# A right rotation operation on an array of size n shifts each of the array's
# elements 1 unit to the right. Given an integer, d, rotate the array that
# many steps right and return the result.

# Example:
# d=2
# arr=[1,2,3,4,5]
# After 2 rotation, arr's = [4,5,1,2,3]

def right_rotate(k, nums):
    for i in range(k):
        item = nums.pop(len(nums)-1)
        nums.insert(0, item)
    return nums


print(right_rotate(3, [1, 2, 3, 4, 5, 6, 7]))
