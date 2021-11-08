# Library svd_matrix
# Contains functions and procedures required to factorize a matrix using Singular Value Decomposition
# Contributor : 13520042

import numpy as np
import sys
import traceback

eigenvalue_array = np.array([])


def eigenvalue(matrix, eps=1e-5):
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
            traceback.print_exc()
            sys.exit(1)

        matrix = np.matmul(upper_tri, orthogonal)
        lower_tri = np.tril(matrix, k=-1)

        if abs(np.amax(lower_tri)) < eps and abs(np.amin(lower_tri)) < eps:
            enough_iteration = True

    eigenvalues = np.flip(np.sort(np.unique(np.diagonal(matrix))))

    return eigenvalues


def solve_homogeneous(matrix):
    """
    Returns an ndarray of solutions to a homogeneous system of linear
    equations. Solutions are computed by finding the null-space of the system
    matrix.

    Reference: https://stackoverflow.com/questions/1835246/how-to-solve-homogeneous-linear-equations-with-numpy

    :param matrix: Matrix-like object.
    :return: An ndarray of solutions.
    """
    u, s, vh = np.linalg.svd(matrix)
    solutions = np.compress(s == np.amin(s), vh, axis=0)
    return solutions


def ortho_singular(matrix, ortho_type):
    """
    Returns an ndarray of orthogonal matrix created using the eigenvalues of
    said matrix.

    :param matrix: Matrix-like object.
    :param ortho_type: Type of matrix output (i.e. left or right).
    :return: An orthogonal matrix consisted of singular vectors.
    """
    global eigenvalue_array

    if ortho_type == "left":
        singular = np.matmul(matrix, np.transpose(matrix))
    elif ortho_type == "right":
        singular = np.matmul(np.transpose(matrix), matrix)
    else:
        print("Invalid ortho_type!")
        return

    singular_shape = np.shape(singular)
    ortho_matrix = np.empty(singular_shape)

    for i in range(len(eigenvalue_array)):
        eigen_identity = np.zeros(singular_shape)
        np.fill_diagonal(eigen_identity, eigenvalue_array[i])
        singular_eq = np.subtract(singular, eigen_identity)

        singular_vector = solve_homogeneous(singular_eq)
        if np.linalg.norm(singular_vector) == 0:
            singular_vector += 1
        normalised_singular_vector = singular_vector / np.linalg.norm(singular_vector)
        ortho_matrix[:, i] = normalised_singular_vector

    return ortho_matrix


def singular_diagonal(matrix):
    """
    Returns an ndarray of diagonal matrix whose main diagonal consists of
    the matrix's singular values (i.e., the square root of its eigenvalues).

    :param matrix: Matrix-like object.
    :return: An ndarray of singular diagonal matrix.
    """
    global eigenvalue_array

    matrix_shape = np.shape(matrix)
    singular_value = np.sqrt(eigenvalue_array)
    sing_diag_matrix = np.zeros(matrix_shape)
    np.fill_diagonal(sing_diag_matrix, singular_value)

    return sing_diag_matrix


def decompose(matrix):
    """
    Returns a tuple consisted of an ndarray U representing a left-singular
    matrix, an ndarray Σ representing a singular-diagonal matrix, and an
    ndarray V* representing a transposed righ-singular matrix.

    Reference:
    https://informatika.stei.itb.ac.id/~rinaldi.munir/AljabarGeometri/2020-2021/Algeo-19b-Singular-value-decomposition.pdf

    :param matrix: Matrix-like object.
    :return: A tuple consisted of U, Σ, and V*
    """
    global eigenvalue_array

    matrix_shape = np.shape(matrix)
    if matrix_shape[0] < matrix_shape[1]:
        singular_matrix = np.matmul(matrix, np.transpose(matrix))
    else:
        singular_matrix = np.matmul(np.transpose(matrix), matrix)

    eigenvalue_array = eigenvalue(singular_matrix)

    left_singular = ortho_singular(matrix, "left")
    diagonal_singular = singular_diagonal(matrix)
    right_singular = ortho_singular(matrix, "right").transpose()

    return left_singular, diagonal_singular, right_singular


if __name__ == "__main__":
    # test_list = [[4, -2, 3, -7],
    #              [1, 2, 6, 8],
    #              [8, 5, 1, -5],
    #              [-5, 8, -5, 3]]
    # arr_result = eigenvalue(test_list)
    # print(arr_result)
    test_array = [[3, 1, 1],
                  [-1, 3, 1]]
    # ortho_result_left = ortho_singular(test_array, "left")
    # ortho_result_right = ortho_singular(test_array, "right")
    # sing_diag = singular_diagonal(test_array)
    # print(ortho_result_left)
    # print(ortho_result_right)
    # print(sing_diag)
    decomposition = decompose(test_array)
    for array in decomposition:
        print(array)
    result = np.matmul(decomposition[0], decomposition[1])
    result = np.matmul(result, decomposition[2])
    print(result)
