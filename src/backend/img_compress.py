# Library img_compress
# Contains functions and procedures required to compress an image
# Contributor : 13520042

import numpy as np
from PIL import Image
import svd_matrix as svd


def recompose(matrix, mode):
    """
    Recompose the original image matrix from its Singular Value Decomposition.

    :param matrix: A tuple of left-orthogonal matrix, singular matrix, and
                   right-orthogonal matrix, all normalised.
    :param mode: Integer representing the proportion of matrix row and column
                 to be removed.
    :return: An ndarray of recomposed and rescaled image matrix.
    """
    slicing_ratio = 1 - mode/10
    original_size = np.shape(matrix[1])[1]

    reduced_left = matrix[0][:, :round(slicing_ratio * original_size) + 1]
    reduced_singular = matrix[1][:round(slicing_ratio * original_size) + 1,
                                 :round(slicing_ratio * original_size) + 1]
    reduced_right = matrix[2][:round(slicing_ratio * original_size) + 1, :]

    recomposed_matrix = (reduced_left @ reduced_singular @ reduced_right) * 255

    return recomposed_matrix.astype("uint8")


def compress(image, mode):
    """
    Compress a given image using Singular Value Decomposition.

    :param image: An image object.
    :param mode: Integer representing the proportion of matrix row and column
                 to be removed.
    :return: A compressed image based on the mode.
    """
    image_matrix = np.array(image)
    mode = int(mode)
    red_image = image_matrix[:, :, 0]
    green_image = image_matrix[:, :, 1]
    blue_image = image_matrix[:, :, 2]

    decomposed_red = svd.decompose(red_image)
    decomposed_green = svd.decompose(green_image)
    decomposed_blue = svd.decompose(blue_image)

    recomposed_red = recompose(decomposed_red, mode)
    recomposed_green = recompose(decomposed_green, mode)
    recomposed_blue = recompose(decomposed_blue, mode)

    image_matrix[:, :, 0] = recomposed_red
    image_matrix[:, :, 1] = recomposed_green
    image_matrix[:, :, 2] = recomposed_blue

    compressed_image = Image.fromarray(image_matrix)
    return compressed_image


if __name__ == "__main__":
    compressed = compress("../../test/aht4.jpg", 5)
    compressed.save("aht4_compressed.jpg")
