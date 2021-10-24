def selection_sort(value):
    sorted_list = []
    for i in range(0, len(value)):
        index_to_move = index_of_min(value)
        sorted_list.append(value.pop(index_to_move))
        print("%-35s %-35s" % (value, sorted_list))
    return sorted_list


def index_of_min(value):
    min_index = 0
    for i in range(1, len(value)):
        if value[i] < value[min_index]:
            min_index = i
    return min_index


numbers = [2, 5, 1, 1, 9, 9, 6, 5, 0, 2]
print(selection_sort(numbers))
