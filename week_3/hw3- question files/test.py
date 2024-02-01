import HW3


def test_part_a():
    # Change me!
    print(HW3.remove_punctuation("Hi,I'm here!"))
    print(HW3.remove_digits("Hello 2024, goodbye 2023"))
    print(HW3.remove_spaces("hi,   i want  to join"))
    print(HW3.remove_stopwords(['I', 'can', 'love', 'me', 'better', 'than', 'you', 'can']))
    print(HW3.stemming(['hoodies', 'glasses', 'kids', 'knocked', 'reading']))
    print(HW3.preprocessing("Yesterday, I received 3 emails from my colleagues!"))

test_part_a()
