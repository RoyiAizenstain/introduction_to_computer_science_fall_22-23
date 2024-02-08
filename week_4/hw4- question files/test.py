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
    all_false = output_false1 or output_false2 or output_false3 or output_false4 or output_false5 or output_false6
    if all_true and not all_false:
        print("q1-all tests passed")
    else:
        print("q1-not all tests passed")


def test_q2():
    pass


def test_q3():
    pass


def test_q4():
    pass


def test_all():
    test_q1()
    test_q2()
    test_q3()
    test_q4()


test_all()
