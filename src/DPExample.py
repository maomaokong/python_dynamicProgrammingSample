"""

Try to understand the Dynamic Programming in edX
- ColumbiaX DS102X Machine Learning for Data Science and Analytics
- Week 2 Algorithm 2
- 2.7 Dynamic Programming 1 and 2.8 Dynamic Programming 2

## Longest Common Subsequence Problem

1.  Given two sequences X=x1...xm, Y=y1...yn, find the longest common subsequence
2.  Example: For X = ABCBDAB, Y = BDCABA, one longest common subsequence is BCBA

X       = A B   C   B D A B
Y       =   B D C A B   A
Answer  =   B   C   B   A

3.  Measure of similarity of two strings
4.  More generally, edit distance

"""

import numpy as np


def main():
    x = 'ABCBDAB'
    y = 'BDCABA'

    string1 = x.rjust(len(x)+1)
    string2 = y.rjust(len(y)+1)

    if len(string1) < len(string2):
        tmp_string = string2
        string2 = string1
        string1 = tmp_string

    array_i = list(string1)
    array_j = list(string2)

    # Create empty 2d Array
    array_ij = np.zeros(shape=(len(string1), len(string2)))

    for positionM, itemM in enumerate(array_i):
        for positionN, itemN in enumerate(array_j):
            if itemM == ' ' or itemN == ' ':
                array_ij[positionM, positionN] = 0
            else:
                if itemM != itemN:
                    upper_array_ij_value  = array_ij[positionM-1, positionN]
                    left_array_ij_value = array_ij[positionM, positionN-1]

                    array_ij[positionM, positionN] = max(upper_array_ij_value, left_array_ij_value)
                else:
                    upper_array_ij_value  = array_ij[positionM-1, positionN]
                    left_array_ij_value = array_ij[positionM, positionN-1]
                    upper_left_array_ij_value = array_ij[positionM-1, positionN-1]

                    array_ij[positionM, positionN] = max(upper_array_ij_value
                                                         , left_array_ij_value
                                                         , (upper_left_array_ij_value+1)
                                                         )

    # Getting Subsequence
    common_subseq_i = ''
    common_subseq_j = ''

    max_array_i_position = len(array_i)
    max_array_j_position = len(array_j)
    new_position_array_j = max_array_j_position

    for position_arrayI in range(max_array_i_position, 1, -1):
        continue_left = True

        if continue_left:
            for position_arrayJ in range(max_array_j_position, 1, -1):
                if position_arrayJ <= new_position_array_j:
                    # 1.  Get current 2d array value
                    current_array_ij_value = array_ij[position_arrayI - 1, position_arrayJ - 1]
                    left_array_ij_value = array_ij[position_arrayI - 1, position_arrayJ - 2]
                    upper_array_ij_value = array_ij[position_arrayI - 2, position_arrayJ - 1]

                    # 2.  Compare bottom right element with his left element
                    if (current_array_ij_value != left_array_ij_value) \
                            and (current_array_ij_value != upper_array_ij_value):
                        common_subseq_i = ''.join((array_i[position_arrayI-1], common_subseq_i))
                        common_subseq_j = ''.join((array_j[position_arrayJ-1], common_subseq_j))

                        # Get arrayJ Position
                        new_position_array_j = position_arrayJ

                        print("currentI: {0}, currentJ: {1}, cell_value: {2}, common_subseqI: {3}"
                              .format(position_arrayI-1, position_arrayJ-1, current_array_ij_value, common_subseq_i))

                        continue_left = False
                        break

    print(common_subseq_i)
    print()
    print(common_subseq_j)


if __name__ == '__main__':
    main()
