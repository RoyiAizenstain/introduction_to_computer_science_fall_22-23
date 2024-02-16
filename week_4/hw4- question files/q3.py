def is_zigzag(list):
    ups_and_downs = rec_is_zigzag(list)
    if ups_and_downs[0] + ups_and_downs[1] == len(list) - 1 or not list:
        return True
    else:
        return False


def rec_is_zigzag(list):
    if len(list) == 1 or not list:
        return [0, 0]
    if list[0] < 0.5 * list[1]:
        ups_and_downs = rec_is_zigzag(list[1:])
        ups_and_downs[0] += 1
        if abs(ups_and_downs[0] - ups_and_downs[1]) > 1:
            return [0, 0]
        return ups_and_downs
    if list[0] > 2 * list[1]:
        ups_and_downs = rec_is_zigzag(list[1:])
        ups_and_downs[1] += 1
        if abs(ups_and_downs[0] - ups_and_downs[1]) > 1:
            return [0, 0]
        return ups_and_downs
    return [0, 0]


def longest_list(list):
    if not list:
        return []
    if len(list) == 1:
        return list[0]
    if len(list[0]) <= len(list[1]):
        return longest_list(list[1:])
    if len(list[0]) > len(list[1]):
        return longest_list([list[0]] + list[2:])


def merge_zigzag(list1, list2, merge_list=[]):
    if not is_zigzag(merge_list):
        return merge_list[:-1]
    all_options = []
    if not list1 and not list2:
        return merge_list
    if list1:
        option1 = merge_zigzag(list1[1:], list2, merge_list + [list1[0]])
        option2 = merge_zigzag(list1[1:], list2, merge_list)
        all_options.append(option1)
        all_options.append(option2)
    if list2:
        option3 = merge_zigzag(list1, list2[1:], merge_list + [list2[0]])
        option4 = merge_zigzag(list1, list2[1:], merge_list)
        all_options.append(option3)
        all_options.append(option4)
    return longest_list(all_options)


print(merge_zigzag([3], [2]))
