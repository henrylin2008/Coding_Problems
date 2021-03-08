# Breadth-First search
# Auxiliary Space: 2(n+m) ==> O(n+m); n=rows, m=columns
# Time: O(n*m)
# Solution: using Breadth-First search; when a cell is clicked (given_i, given_j), check surrounding 8 cells, and use -2
# as a marker for reviewed cells, put the cell in a to_check queue; then use a while loop to repeat the process for the
# surrounding 8 cells, until there's no more cells with 0.
def click(field, num_rows, num_cols, given_i, given_j):
    import queue
    to_check = queue.Queue()  # new queue: check 8 cells surrounding clicked cell
    if field[given_i][given_j] == 0:  # if clicked cell is 0
        field[given_i][given_j] = -2  # set the value of clicked cell (from 0) to -2; -2 as a marker for reviewed
        to_check.put((given_i, given_j))  # store clicked cell as a tuple/array to the to_check queue
    else:  # else if clicked cell is not 0
        # print("Field: ", field)
        return field  # return the field
    while not to_check.empty():  # while to_check queue is not empty
        (current_i, current_j) = to_check.get()  # next item in to_check queue to check
        for i in range(current_i - 1, current_i + 2):  # range of rows to check: i-1 to i+1
            for j in range(current_j - 1, current_j + 2):  # range of cols to check: j-1 to j+1
                if 0 <= i < num_rows and 0 <= j < num_cols and field[i][j] == 0:  # within the range and cell is 0
                    field[i][j] = -2        # set the current field to -2
                    to_check.put((i, j))    # store it to to_check queue for review later
    # print("field: ", field)
    return field


# NOTE: The following input values will be used for testing your solution.
field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

# click(field1, 3, 5, 2, 2)   # should return:
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, -1, 1, 0]]

click(field1, 3, 5, 1, 4)   # should return:
# [[-2, -2, -2, -2, -2],
#  [-2, 1, 1, 1, -2],
#  [-2, 1, -1, 1, -2]]


field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

click(field2, 4, 4, 0, 1)  # should return:
# [[-1, 1, 0, 0],
#  [1, 1, 0, 0],
#  [0, 0, 1, 1],
#  [0, 0, 1, -1]]

click(field2, 4, 4, 1, 3) # should return:
# [[-1, 1, -2, -2],
#  [1, 1, -2, -2],
#  [-2, -2, 1, 1],
#  [-2, -2, 1, -1]]
