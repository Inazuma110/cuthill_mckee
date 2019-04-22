from scipy import sparse
import numpy as np

m = np.array([
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1]
    ])
print(m)
print()

# 隣接行列
def create_cuthill_mckee_matrix(adjacency_matrix):
    csr_m = sparse.csr_matrix(adjacency_matrix)
    index_dict = sparse.csgraph.reverse_cuthill_mckee(csr_m)
    index_dict = {i[1]: i[0] for i in enumerate(index_dict)}

    cuthill_mckee_matrix = np.zeros_like(adjacency_matrix)
    row, column = csr_m.nonzero()

    for r, c in zip(row, column):
        cuthill_mckee_matrix[index_dict[r], index_dict[c]] = 1

    return cuthill_mckee_matrix

print(create_cuthill_mckee_matrix(m))
