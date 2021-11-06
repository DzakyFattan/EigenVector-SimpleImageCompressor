# Library svd_matrix
# Contains functions and procedures required to factorize a matrix using Singular Value Decomposition
# Contributor : 13520042

import numpy as np


def eigenvalue(matrix, eps=1e-10):
    """
    Returns an ndarray of matrix eigenvalues, sorted descendingly.
    Eigenvalues are approximated using QR-decomposition.

    Reference : https://cstl-csm.semo.edu/jwojdylo/MA345/Chapter6/qrmethod/qrmethod.pdf

    :param matrix: Matrix-like object whose eigenvalues to be calculated.
    :param eps: Small value acting as comparator to which entries below the main
    diagonal is compared to. The default value is 1e-10.
    :return: An ndarray of matrix eigenvalues, sorted in descending order.
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

        if abs(np.amax(lower_tri)) < eps and abs(np.amin(lower_tri)) < eps:
            enough_iteration = True

    eigenvalues = np.flip(np.sort(np.unique(np.diagonal(matrix))))

    return eigenvalues


def solve_homogeneous(matrix, eps=1e-10):
    """
    Returns an ndarray of solutions to a homogeneous system of linear equations.
    Solutions are computed by finding the null-space of the system matrix.

    Reference: https://stackoverflow.com/questions/1835246/how-to-solve-homogeneous-linear-equations-with-numpy

    :param matrix: Matrix-like object.
    :param eps: Small value acting as comparator to which entries of the singular matrix
    is compared to.
    :return: An ndarray of solutions.
    """
    u, s, vh = np.linalg.svd(matrix)
    solutions = np.compress(s <= eps, vh, axis=0)
    return solutions


def ortho_singular(matrix, ortho_type):
    """
    Returns an ndarray of orthogonal matrix created using the eigenvalues of
    said matrix.

    Reference: https://www.math.utah.edu/~goller/F15_M2270/BradyMathews_SVDImage.pdf

    :param matrix: Matrix-like object.
    :param ortho_type: Type of matrix output (i.e. left or right)
    :return: An orthogonal matrix consisted of singular vectors
    """
    if ortho_type == "left":
        singular = np.matmul(matrix, np.transpose(matrix))
    elif ortho_type == "right":
        singular = np.matmul(np.transpose(matrix), matrix)
    else:
        print("Invalid ortho_type!")
        return

    eigen_singular = eigenvalue(singular)
    singular_shape = np.shape(singular)
    ortho_matrix = np.empty(singular_shape)

    for i in range(len(eigen_singular)):
        eigen_identity = np.zeros(singular_shape)
        np.fill_diagonal(eigen_identity, eigen_singular[i])
        singular_eq = np.subtract(singular, eigen_identity)

        singular_vector = solve_homogeneous(singular_eq)
        if np.linalg.norm(singular_vector) == 0:
            singular_vector += 1
        normalised_singular_vector = singular_vector / np.linalg.norm(singular_vector)
        ortho_matrix[:, i] = normalised_singular_vector

    return ortho_matrix


def decompose(matrix):
    pass


if __name__ == "__main__":
    # test_list = [[4, -2, 3, -7],
    #              [1, 2, 6, 8],
    #              [8, 5, 1, -5],
    #              [-5, 8, -5, 3]]
    # arr_result = eigenvalue(test_list)
    # print(arr_result)
    test_array = [[3, 1, 1],
                  [-1, 3, 1]]
    ortho_result_left = ortho_singular(test_array, "left")
    ortho_result_right = ortho_singular(test_array, "right")
    print(ortho_result_left)
    print(ortho_result_right)
