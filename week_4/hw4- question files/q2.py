def estate_homogeneity(divisions, total_area):
    # Your Code Here
    return rec_estate_homogeneity(divisions, total_area, 0)
    pass


def rec_estate_homogeneity(divisions, total_area, counter):
    if isinstance(divisions, int):
        divisions = [divisions]
    if not divisions:
        divisions.append(0)
    if rec_all_numbers(divisions, 0):
        return rec_all_equal(divisions, total_area, 0)
    if counter == len(divisions):
        return True
    return rec_estate_homogeneity(divisions[counter], total_area / len(divisions), 0) and rec_estate_homogeneity(
        divisions, total_area, counter + 1)

    pass


def rec_all_numbers(mylist, counter):
    length = len(mylist)
    if counter == length:
        return True
    if isinstance(mylist[counter], list):
        return False
    if counter < length:
        counter += 1
        return rec_all_numbers(mylist, counter)


def rec_all_equal(mylist, total_area, counter):
    length = len(mylist)
    area_each = total_area / length
    if counter == length:
        return True
    if mylist[counter] != area_each:
        return False
    if counter < length:
        counter += 1
        return rec_all_equal(mylist, total_area, counter)



