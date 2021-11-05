# Library svd_matrix
# Contains functions and procedures required to factorize a matrix using Singular Value Decomposition
# Contributor : 13520042

import numpy as np


def eigen(matrix):
    """
    Returns an npArray of matrix eigenvalues, sorted descendingly.
    Eigenvalues are approximated using QR-decomposition.

    Reference : https://cstl-csm.semo.edu/jwojdylo/MA345/Chapter6/qrmethod/qrmethod.pdf
    """
    enough_iteration = False

    while not enough_iteration:
        try:
            orthogonal, upper_tri = np.linalg.qr(matrix)
        except np.linalg.LinAlgError:
            print("Matrix doesn't have eigenvalues.")
            return

        matrix = np.matmul(upper_tri, orthogonal)
        lower_tri = np.tril(matrix, k=-1)

        if np.amax(lower_tri) < 10**(-10):
            enough_iteration = True

    eigenvalues = np.flip(np.sort(np.unique(np.diagonal(matrix))))

    return eigenvalues


def svd(matrix):
    pass


if __name__ == "__main__":
    test_list = [[4, -2, 3, -7],
                 [1, 2, 6, 8],
                 [8, 5, 1, -5],
                 [-5, 8, -5, 3]]
    arr_result = eigen(test_list)
    print(arr_result)
