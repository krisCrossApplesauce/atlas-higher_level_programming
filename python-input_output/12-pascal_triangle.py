#!/usr/bin/python3
"""
wow, not allowed to google
"""


def pascal_triangle(n):
    """ returns a list of ints representing the Pascal's triangle of n """
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = []
        for ii in range(i + 1):
            if i > 1 and ii > 0 and ii < i:
                row.append(triangle[i - 1][ii - 1] + triangle[i - 1][ii])
            else:
                row.append(1)
        triangle.append(row)
    return triangle
