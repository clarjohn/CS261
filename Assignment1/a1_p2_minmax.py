# Course: CS261 - Data Structures
# Student Name: John Clarke
# Assignment: 1
# Description: function that returns the min and max from a list


def min_max(arr: []) -> ():
    """ Function returns the min and max value from a list"""
    # first check to see if list is empty
    if arr == []:
        min = None
        max = None
    else:
        min = arr.pop()
        max = min
        for i in arr:
            if i < min:
                min = i
            elif i > max:
                max = i
    return min, max





# BASIC TESTING
if __name__ == "__main__":
    # example 1
    print(min_max([1, 2, 3, 4, 5]))

    # example 2
    print(min_max([8, 7, 6, -5, 4]))

    # example 3
    print(min_max([]))
