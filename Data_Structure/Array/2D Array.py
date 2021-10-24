# Given a 6x6 2D Array:

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

# An hourglass in A is a subset of values with indices falling in this pattern in arr's graphical representation:

# a b c
#   d
# e f g

# There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values.
# Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum. The array will always be 6x6.


def hourglassSum(arr):
    sum = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1]
                       [j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            max_sum = max(sum)
    return max_sum


array = ([1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0],
         [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0])
print(hourglassSum(array))
