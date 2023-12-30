# ************************ QUESTION 1.1 **************************
### WRITE CODE HERE
def generate_pascals_triangle(rows):
    """Takes in a number of rows, returns a nested lists that are pascals triangle"""
    pascals_triangle = [[1]]
    for row in range(rows):
        cols = row + 1
        if row == 0:
            continue
        pascals_triangle_row = []
        for col in range(cols):
            if col == 0 or col + 1 == cols:
                pascals_triangle_row.append(1)
            else:
                pascals_triangle_row.append(pascals_triangle[row - 1][col - 1] + pascals_triangle[row - 1][col])
        pascals_triangle.append(pascals_triangle_row)
    return pascals_triangle


def print_pascals_triangle(triangle):
    """Takes in a pascals triangle, prints the pascals triangle"""
    triangle_rows = len(triangle)
    spaces_to_add = triangle_rows - 1
    for row in range(triangle_rows):
        print(spaces_to_add * " " + list_to_str(triangle[row]))
        spaces_to_add -= 1;


def list_to_str(my_list):
    """Takes in a list, return a string format of the list"""
    string = ""
    for i in range(len(my_list)):
        string += str(my_list[i]) + " "
    return string

# ************************ QUESTION 1.2 **************************
### WRITE CODE HERE
