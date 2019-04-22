#!/usr/bin/env python3
'''
カットヒルマキー法のお勉強
'''

from scipy import sparse
import numpy as np

MATRIX = np.array([
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1]
    ])
print(MATRIX)
print()


def create_cuthill_mckee_matrix(adjacency_matrix):
    '''
    @params numpy.ndarray型の隣接行列
    '''
    csr_m = sparse.csr_matrix(adjacency_matrix)
    index_dict = sparse.csgraph.reverse_cuthill_mckee(csr_m)
    index_dict = {i[1]: i[0] for i in enumerate(index_dict)}

    cuthill_mckee_matrix = np.zeros_like(adjacency_matrix)
    rows, columns = csr_m.nonzero()

    for row, column in zip(rows, columns):
        cuthill_mckee_matrix[index_dict[row], index_dict[column]] = 1

    return cuthill_mckee_matrix


print(create_cuthill_mckee_matrix(MATRIX))
