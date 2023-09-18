#!/usr/bin/env python3
"""Rotate Matrix"""


def rotate_2d_matrix(matrix):
    """Rotate 2D Matrix """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            a = matrix[j]
            b = matrix[i]
            b, a = a, b
            
    for i in range(n):
        matrix[i] = matrix[i][::-1]
