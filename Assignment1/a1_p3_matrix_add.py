# Course: CS261 - Data Structures
# Student Name: John Clarke
# Assignment: 1
# Description:


def matrix_add(a: [[]], b: [[]]) -> [[]]:
    """ function that takes two matrics has input and returns the sum a output"""
    # Check that each metric has the same number of dimensions
    if len(a) != len(b):
        results = None
    else:
        row_len = 0
        for x in a[0]:
            row_len += 1
        # create metrix to hold results
        results = [[0] * row_len for _ in range(len(a))]
        a_row = 0
        for i in a:
            a_col = 0
            for x in i:
                results[a_row][a_col] = a[a_row][a_col] + b[a_row][a_col]
                a_col += 1
            a_row += 1

    return results





# BASIC TESTING
if __name__ == "__main__":
    # example 1
    m1 = [[1, 2, 3], [2, 3, 4]]
    m2 = [[5, 6, 7], [8, 9, 10]]
    m3 = [[1, 2], [3, 4], [5, 6]]

    #print(matrix_add(m1, m2))
   # print(matrix_add(m1, m3))
   # print(matrix_add(m1, m1))
   # print(matrix_add([[]], [[]]))
   # print(matrix_add([[]], m1))
    print(matrix_add([[]], [[]]))
    print(matrix_add( m1, m3 ))
    print(matrix_add( [[]], m1 ))

