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

x = 'ABCBDAB'
y = 'BDCABA'

string1 = x.rjust(len(x)+1)
string2 = y.rjust(len(y)+1)

if len(string1) < len(string2):
    tmpString = string2
    string2 = string1
    string1 = tmpString

arrayI = list(string1)
#arrayI = np.fromstring(string1, sep='')
arrayJ = list(string2)
#arrayJ = np.fromstring(string2, sep='')

# Create empty 2d Array
arrayIJ = np.zeros(shape=(len(string1), len(string2)))

#print(arrayIJ)

for positionM, itemM in enumerate(arrayI):
    for positionN, itemN in enumerate(arrayJ):
        if itemM == ' ' or itemN == ' ':

            arrayIJ[positionM, positionN] = 0

            #print("{0}, {1}, set=0".format(itemM, itemN))
        else:
            if itemM != itemN:
                upper_arrayIJ_value  = arrayIJ[positionM-1, positionN]
                left_arrayIJ_value = arrayIJ[positionM, positionN-1]

                arrayIJ[positionM, positionN] = max(upper_arrayIJ_value, left_arrayIJ_value)

                #print("{0}, {1}, set={2}".format(itemM, itemN, arrayIJ[positionM, positionN]))
            else:
                upper_arrayIJ_value  = arrayIJ[positionM-1, positionN]
                left_arrayIJ_value = arrayIJ[positionM, positionN-1]
                upper_left_arrayIJ_value = arrayIJ[positionM-1, positionN-1]

                arrayIJ[positionM, positionN] = max(upper_arrayIJ_value, left_arrayIJ_value, (upper_left_arrayIJ_value+1))

                #print("{0}, {1}, set={2}".format(itemM, itemN, arrayIJ[positionM, positionN]))

#print(arrayIJ)

## Getting Subsequence
common_subseqI = ''
common_subseqJ = ''

max_arrayI_position = len(arrayI)
max_arrayJ_position = len(arrayJ)
new_position_arrayJ = max_arrayJ_position

for position_arrayI in range(max_arrayI_position, 1, -1):
    continue_left = True

    if continue_left:
        for position_arrayJ in range(max_arrayJ_position, 1, -1):
            if position_arrayJ <= new_position_arrayJ:
                #1.  Get current 2d array value
                current_arrayIJ_value = arrayIJ[position_arrayI - 1, position_arrayJ - 1]
                left_arrayIJ_value = arrayIJ[position_arrayI - 1, position_arrayJ - 2]
                upper_arrayIJ_value = arrayIJ[position_arrayI - 2, position_arrayJ - 1]

                # 2.  Compare bottom right element with his left element
                if (current_arrayIJ_value != left_arrayIJ_value) and (current_arrayIJ_value != upper_arrayIJ_value):
                    common_subseqI = ''.join((arrayI[position_arrayI-1], common_subseqJ))
                    common_subseqJ = ''.join((arrayJ[position_arrayJ-1], common_subseqJ))

                    #Get arrayJ Position
                    new_position_arrayJ = position_arrayJ

                    print("currentI: {0}, currentJ: {1}, cell_value: {2}, common_subseqI: {3}"
                          .format(position_arrayI-1, position_arrayJ-1, current_arrayIJ_value, common_subseqI))

                    continue_left = False
                    break

print(common_subseqI)
print()
print(common_subseqJ)