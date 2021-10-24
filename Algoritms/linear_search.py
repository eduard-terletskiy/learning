def linear_search(list, target):
    """
    return the index position target found
    """
    for item in range(0, len(list)):
        if list[item] == target:
            return item
    return None


def verify(index):
    if index is not None:
        print("Tagret found at index: ", index)
    else:
        print("tagret not found")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)