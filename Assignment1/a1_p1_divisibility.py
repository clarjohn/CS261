# Course: CS261 - Data Structures
# Student Name: John Clarke
# Assignment: 1
# Description:


def length(s: str) -> int:
    """ find the length of the string"""
    value = 0
    for i in s:
        value += 1
    return value


def is_divisible(m: int, n: int, a: int, b: int) -> []:
    """ function that returns if a giving number in a range is divisable by two pre
        selected numbers"""
    final_result = []

    # check if any numbers are none positive
    if m < 0 or n < 0 or a < 0 or b < 0:
        final_result = "Incorrect input"

    # check if m > n
    elif m > n:
        final_result = "Incorrect input"
    # check if a equals b
    elif a == b:
        final_result = "Incorrect input"
    else:
        # add header using provided code
        header1 = "Num"
        header2 = "\tDiv by %s and/or %d?" % (a, b)
        under1 = "-" * length(header1) + "\t"
        under2 = "-" * length(header2)

        # test for each value
        final_result.append(header1+header2)
        final_result.append(under1+under2)
        cur_num = n
        while cur_num >= m:
            if cur_num % a == 0 and cur_num % b == 0:
                result = "both"
            elif cur_num % a == 0:
                result = "div by "+str(a)
            elif cur_num % b == 0:
                result = "div by " + str(b)
            else:
                result = "None"
            final_result.append(str(cur_num)+"\t"+result)
            cur_num -= 1
    return final_result





# BASIC TESTING
if __name__ == "__main__":
    # example 1
    #print(*is_divisible(2, 7, 2, 3), sep="\n")

    # example 2
   # print(is_divisible(1, 20, -1, 3))
   # print(is_divisible(20, 0, 100, 200))
   # print(is_divisible(10, 8, 7, 2))
   # print(is_divisible(3, 30, 7, 7))
    #print(is_divisible(-7, -2, 2, 3))
    print(*is_divisible(2, 24, 2, 4), sep="\n")
