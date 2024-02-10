def colcat(mat_a, mat_b):
    # Your Code Here
    if len(mat_a) == 1 and len(mat_b) == 1:
        return [mat_a[0] + mat_b[0]]
    return colcat([mat_a[0]], [mat_b[0]]) + colcat(mat_a[1:], mat_b[1:])

def vertical_split(input_mat):
    # Your Code Here
    return


def rotate_mat_rec(input_mat):
    # Your Code Here - Bonus for 20% additional assignment grade!
    return
