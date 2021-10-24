# Write a function that splits a given list in 2 parts.
# For example, [1, 2, 3, 4, 5, 6] splits into ([1, 2, 3], [4, 5, 6])

def split_list(list):
    return 0 if len(list) == 0 else list[:len(list)//2], list[len(list)//2:]


alist = [1, 2, 3, 4, 5, 6, 7, 8]
print(split_list(alist))
