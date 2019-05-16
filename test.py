#!/usr/bin/env python3
'''
cuthill_mckee
'''

from scipy import sparse
import numpy as np

np.set_printoptions(threshold=np.inf)

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
# print(MATRIX)
# print()


def create_cuthill_mckee_matrix(adjacency_matrix):
    '''
    cuthill_mckeeをしたあとの行列を求める

    Parameters
    ---
    adjacency_matrix: np.array
        隣接行列
    '''
    csr_m = sparse.csr_matrix(adjacency_matrix)
    index_dict = sparse.csgraph.reverse_cuthill_mckee(csr_m)
    index_dict = {i[1]: i[0] for i in enumerate(index_dict)}

    cuthill_mckee_matrix = np.zeros_like(adjacency_matrix)
    rows, columns = csr_m.nonzero()

    for row, column in zip(rows, columns):
        cuthill_mckee_matrix[index_dict[row], index_dict[column]] = 1

    return cuthill_mckee_matrix


def random_adjacency_matrix(index, fill_rate=0.1):
    '''
    1辺の要素数がindexのランダムな隣接行列を作成する。
    '''
    import random
    adjacency_matrix = np.zeros((index, index), dtype=np.int)
    fill_num = int(index * index * fill_rate * 0.5)

    for i in range(fill_num):
        while True:
            column = random.randint(0, index-1)
            row = random.randint(0, index-1)
            if not(row == column) and adjacency_matrix[row, column] == 0:
                break

        adjacency_matrix[row, column] = 1
        adjacency_matrix[column, row] = 1

    return adjacency_matrix


MATRIX = random_adjacency_matrix(10, 0.1)
print(MATRIX)
print()
AFTER_MATRIX = create_cuthill_mckee_matrix(MATRIX)
print(AFTER_MATRIX)
