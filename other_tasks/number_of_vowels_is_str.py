# Implement a function count_vowels that accepts a string as the parameter and
# returns a number of vowels. You need to count only English vowels.
# If string is empty or None return 0.

# Example: string Pythonista has 3 vowels „o“, „i“, „a“

# -----------------------------------------------------

def count_vowels(input: str) -> int:
    list = ["o", "a", "i", "e", "u", "y"]
    if input is None:
        print("String is empty")
        exit(0)
    input = input.lower()
    sum = 0
    new_list = []
    for i in input:
        if i in list:
            sum += 1
            new_list.append(i)
    print("String has", sum, "vowels: ", new_list)
