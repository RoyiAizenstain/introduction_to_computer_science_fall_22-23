def colcat(mat_a, mat_b):
    """

    :param mat_a:
    :param mat_b:
    :return: the combination of them
    """
    # Your Code Here
    if len(mat_a) == 1 and len(mat_b) == 1:
        return [mat_a[0] + mat_b[0]]
    return colcat([mat_a[0]], [mat_b[0]]) + colcat(mat_a[1:], mat_b[1:])


def vertical_split(input_mat):
    # Your Code Here
    """

    :param input_mat:
    :return: vertical split of input_mat
    """
    if not input_mat:
        return ([], [])
    n = len(input_mat[0])
    p = n // 2
    mat = input_mat.pop()
    tuple = vertical_split(input_mat)
    tuple[0].append(mat[0:p])
    tuple[1].append(mat[p:])
    return (tuple[0], tuple[1])




def rotate_mat_rec(input_mat):
    # Your Code Here - Bonus for 20% additional assignment grade!
    return
