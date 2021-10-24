# A left rotation operation on an array of size n shifts each of the array's
# elements 1 # unit to the left. Given an integer, d, rotate the array that
# many steps left and return the result.

# Example:
# d=2
# arr=[1,2,3,4,5]
# After 2 rotation, arr's = [3,4,5,1,2]

def rotateLeft(d, arr):
    # Write your code here
    for i in range(d):
        item = arr.pop(0)
        arr.append(item)
    return arr


print(rotateLeft(3, [1, 2, 3, 4, 5, 6, 7]))
