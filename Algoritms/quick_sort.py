def quick_sort(values):
    if len(values) <= 1:
        return values
    else:
        pivot = values[0]
        less = [i for i in values[1:] if i <= pivot]
        greater = [i for i in values[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


numbers = [9, 6, 5, 4, 0, 9, 1, 3, 4, 7, 0, 9, 4, 9, 2, 6]
print(quick_sort(numbers))
