# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:

def length(input_string: str) -> int:
    """ find the length of the string"""
    value = 0
    for i in input_string:
        value += 1
    return value


def input_cleanup(input_string: str) -> str:
    """ This function receives the original input string from the user and returns a ‘clean’ version ofit.  """
    results = input_string
    f = 0
    for i in input_string:
        # flip upper case letters to lower cases
        if i == 'A':
            i = 'a'
        elif i == 'B':
            i = 'b'
        elif i == 'C':
            i = 'c'
        elif i == 'D':
            i = 'd'
        elif i == 'E':
            i = 'e'
        elif i == 'F':
            i = 'f'
        elif i == 'G':
            i = 'g'
        elif i == 'H':
            i = 'h'
        elif i == 'I':
            i = 'i'
        elif i == 'J':
            i = 'j'
        elif i == 'K':
            i = 'k'
        elif i == 'L':
            i = 'l'
        elif i == 'M':
            i = 'm'
        elif i == 'N':
            i = 'n'
        elif i == 'O':
            i = 'o'
        elif i == 'P':
            i = 'p'
        elif i == 'Q':
            i = 'q'
        elif i == 'R':
            i = 'r'
        elif i == 'S':
            i = 's'
        elif i == 'T':
            i = 't'
        elif i == 'U':
            i = 'u'
        elif i == 'V':
            i = 'v'
        elif i == 'W':
            i = 'w'
        elif i == 'V':
            i = 'v'
        elif i == 'W':
            i = 'w'
        elif i == 'X':
            i = 'x'
        elif i == 'Y':
            i = 'y'
        elif i == 'Z':
            i = 'z'

        #    replace all non english letters with '_'
        if i not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']:
            i = '_'

        if f == 0:
            result = i
        else:
            if i == '_':
                if result[-1] != '_':
                    result = result+i
            else:
                result = result + i
        if f !=0:
            f += 1
        elif i != '_':
            f += 1

    if result[-1] == '_':
        l = length(result) -1
        s = 0
        if result[0] == '_':
            result = ''
        else:
            temp = result
            result = temp[0]
            for t in temp:
                if s != l and s != 0:
                    result = result+t
                s += 1

    return result


def is_clean_string(input_string: str) -> bool:
    """ This function verifies whether input string is ‘clean’ and is ready for a ‘camel case’"""
    status = True
    for x in input_string:
        if x not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z', '_']:
            status = False
    if status == True:
        v = 0
        for i in input_string:
            if v != 0 and i == '_':
                if input_string[v - 1] == '_':
                    status = False
            v += 1
    if input_string == True and status == True:
        if input_string[0] == '_' or input_string[-1] == '_':
            status = False

    return status


def camel_case(input_string: str, func_is_clean, func_cleanup):
    """
    This function accepts the original input string from the user, as well as functions
        is_clean_string() and input_clean() and returns camel case
    """
    # sanitize input string
    clean_input = func_cleanup(input_string)     # DO NOT DELETE / CHANGE

    # check if input string is ready for camelCase conversion

    if not func_is_clean(clean_input):           # DO NOT DELETE / CHANGE
        return None                              # DO NOT DELETE / CHANGE

    # check that input string has at least two words in it
    # return None if it does not
    elif '_' not in clean_input:
        return None

    # convert clean input string into camelCase
    else:
        s = 0
        camel = clean_input[0]
        for i in clean_input:
            if s != 0:
                if clean_input[s-1] == '_':
                   if i == 'a':
                       camel = camel+"A"
                   elif i == 'b':
                       camel = camel + "B"
                   elif i == 'c':
                       camel = camel + "C"
                   elif i == 'd':
                       camel = camel + "D"
                   elif i == 'e':
                       camel = camel + "E"
                   elif i == 'f':
                       camel = camel + "F"
                   elif i == 'g':
                       camel = camel + "G"
                   elif i == 'h':
                       camel = camel + "H"
                   elif i == 'i':
                       camel = camel + "I"
                   elif i == 'j':
                       camel = camel + "J"
                   elif i == 'k':
                       camel = camel + "K"
                   elif i == 'l':
                       camel = camel + "L"
                   elif i == 'm':
                       camel = camel + "M"
                   elif i == 'n':
                       camel = camel + "N"
                   elif i == 'o':
                       camel = camel + "O"
                   elif i == 'p':
                       camel = camel + "P"
                   elif i == 'q':
                       camel = camel + "Q"
                   elif i == 'r':
                       camel = camel + "R"
                   elif i == 's':
                       camel = camel + "S"
                   elif i == 't':
                       camel = camel + "T"
                   elif i == 'u':
                       camel = camel + "U"
                   elif i == 'v':
                       camel = camel + "V"
                   elif i == 'w':
                       camel = camel + "W"
                   elif i == 'x':
                       camel = camel + "X"
                   elif i == 'y':
                       camel = camel + "Y"
                   elif i == 'z':
                       camel = camel + "Z"
                elif i != '_':
                    camel = camel+i
            s += 1

    return camel






# BASIC TESTING
if __name__ == "__main__":
    if __name__ == "__main__":
        test_set = ("_random_ _word_provided",
                    "@$ptr*4con_", " ran  dom  word",
                    "example    word   ", "ANOTHER_Word",
                    "__", "_ _ _", "    ", "435%7_$$", "random")
        test_set2 = ("__", "_ _ _")

        # example 1
        for test_string in test_set:
            result = input_cleanup(test_string)
           # print(length(result), result)
        print()

        # example 2
        for test_string in test_set:
            result = input_cleanup(test_string)
            #print(is_clean_string(test_string), is_clean_string(result))
        print()

        # example 3
        for test_string in test_set:
            result = camel_case(test_string, is_clean_string, input_cleanup)
            print("'" + test_string + "'", "-->", result)