# Course: CS261 - Data Structures
# Student Name: John Clarke
# Assignment: 1
# Description:


def swap_pairs(arr: []) -> []:
    """ Function takes a list of integers and returns a list with the pairs flipped"""

    for i in range(len(arr)):
        if i % 2 != 0:
            temp = arr[i-1]
            arr[i-1] = arr[i]
            arr[i] = temp

    return arr





# BASIC TESTING
if __name__ == "__main__":
    # example 1
    print(swap_pairs([1, 2, 3, 4, 5]))

    # example 2
    print(swap_pairs([8, 7, 6, -5, 4, 10]))

    # example 3
    print(swap_pairs([]))
