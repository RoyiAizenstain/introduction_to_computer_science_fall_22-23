def estate_homogeneity(divisions, total_area):
    # Your Code Here
    return rec_estate_homogeneity(divisions, total_area, 0)
    pass


def rec_estate_homogeneity(divisions, total_area, counter):
    if isinstance(divisions, int):
        if total_area == divisions:
            return True
        else:
            return False
    len_of_list = len(divisions)
    rec_estate_homogeneity(divisions[counter], total_area / len_of_list, counter)
    rec_estate_homogeneity(divisions, total_area / len_of_list, counter+1)


