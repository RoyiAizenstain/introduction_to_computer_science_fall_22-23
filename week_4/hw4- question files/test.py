import q1, q2, q3, q4


def test_q1():
    # Change me!
    output_true1 = q1.word_reconstruction("feed", ["f", "z", "i", "e", "x", "5", "a", "@", "d", "~"])
    output_true2 = q1.word_reconstruction("", ["f", "z", "i", "e", "x", "5", "a", "@", "d", "~"])
    output_true3 = q1.word_reconstruction("", [])
    output_true4 = q1.word_reconstruction("oooo", ["o", "r", "o", "y", "i"])
    output_true5 = q1.word_reconstruction("t", ["r", "t", "s"])
    output_true6 = q1.word_reconstruction("eefeee", ["e", "f", "z", "i", "e", "x", "5", "a", "@", "d", "~"])
    output_true7 = q1.word_reconstruction("feeed", ["f", "z", "i", "e", "x", "5", "a", "@", "d", "~"])
    output_false1 = q1.word_reconstruction("sad", ["f", "z", "i", "e", "x", "5", "a", "@", "d", "~"])
    output_false2 = q1.word_reconstruction("fax", ["f", "z", "i", "e", "x", "5", "a", "@", "d", "~"])
    output_false3 = q1.word_reconstruction("royi", ["o", "r", "y", "i"])
    output_false4 = q1.word_reconstruction("royi", ["r", "y", "i", "o"])
    output_false5 = q1.word_reconstruction("royi", ["o", "r", "o", "y"])
    output_false6 = q1.word_reconstruction("r", [""])
    all_true = output_true1 and output_true2 and output_true3 and output_true4 and output_true5 and output_true6 and output_true7
    all_false = not (output_false1 or output_false2 or output_false3 or output_false4 or output_false5 or output_false6)
    if all_true and all_false:
        print("q1-all tests passed")
    else:
        print("q1-not all tests passed")


def test_q2():
    output_true1 = q2.estate_homogeneity([300, [100, [50, 50], [25, 25, 25, 25]]], 600)
    output_true2 = q2.estate_homogeneity([[50, 50], 100], 200)
    output_true3 = q2.estate_homogeneity([[], [[]], []], 0)
    output_true4 = q2.estate_homogeneity([100, 100, 100], 300)
    output_false1 = q2.estate_homogeneity([[50, 50], 100, [50, [10, 20, 20]]], 300)
    output_false2 = q2.estate_homogeneity([[50, 50], 100, [50, [20, 10, 20]]], 300)
    output_false3 = q2.estate_homogeneity([[], [[]], []], 100)
    output_false4 = q2.estate_homogeneity([100, 100, 50, 50], 300)
    all_true = output_true1 and output_true2 and output_true3 and output_true4
    all_false = not (output_false1 or output_false2 or output_false3 or output_false4)
    if all_true and all_false:
        print("q2-all tests passed")
    else:
        print("q2-not all tests passed")


def test_q3():
    print("q3-need to build the tests")
    pass


def test_q4():
    test_colcat()
    test_vertical_split()
    pass


def test_colcat():
    mat_1 = [[0, 1], [2, 3]]
    mat_2 = [[6], [7]]
    colcat_1 = q4.colcat(mat_2, mat_1)
    output_true1 = colcat_1 == [[6, 0, 1], [7, 2, 3]]
    output_false1 = colcat_1 == [[7, 2, 3], [6, 0, 1]]
    colcat_mat2 = q4.colcat(mat_1, mat_1)
    output_true2 = colcat_mat2 == [[0, 1, 0, 1], [2, 3, 2, 3]]
    output_false2 = colcat_mat2 == [[0, 1, 0, 1], [2, 3, 3, 3]]
    colcat_mat3 = q4.colcat([[1, 2]], [[-9, 6]])
    output_true3 = colcat_mat3 == [[1, 2, -9, 6]]
    output_false3 = colcat_mat3 == [1, 2, -9, 6]
    all_true = output_true1 and output_true2 and output_true3
    all_false = not (output_false1 and output_false2 and output_false3)
    if all_true and all_false:
        print("q4- part a -all tests passed")
    else:
        print("q4- part a -not all tests passed")


def test_vertical_split():
    test_1 = False
    in_mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    output = q4.vertical_split(in_mat)
    if isinstance(output, tuple):
        output_true1 = output[0] == [[1, 2], [5, 6], [9, 10], [13, 14]] and output[1] == [[3, 4], [7, 8], [11, 12],[15, 16]]
        if output_true1:
            print("q4- part b -the test passed ")
    else:
        print("q4- part b -the test did not pass ")



def test_all():
    test_q1()
    test_q2()
    test_q3()
    test_q4()


test_all()
