def estate_homogeneity(divisions, total_area):
    # Your Code Here
    """

    :param divisions:
    :param total_area:
    :return: bool- if the estate is homogeneity
    """
    return rec_estate_homogeneity(divisions, total_area, 0)


def rec_estate_homogeneity(divisions, total_area, counter):
    """

        :param divisions:
        :param total_area:
        :param counter
        :return: bool- if the estate is homogeneity
        """
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


def rec_all_numbers(mylist, counter):
    """

    :param mylist:
    :param counter:
    :return: bool-if all in list are numbers
    """
    length = len(mylist)
    if counter == length:
        return True
    if isinstance(mylist[counter], list):
        return False
    if counter < length:
        counter += 1
        return rec_all_numbers(mylist, counter)


def rec_all_equal(mylist, total_area, counter):
    """

    :param mylist:
    :param total_area:
    :param counter:
    :return: bool- if all are equal
    """
    length = len(mylist)
    area_each = total_area / length
    if counter == length:
        return True
    if mylist[counter] != area_each:
        return False
    if counter < length:
        counter += 1
        return rec_all_equal(mylist, total_area, counter)
