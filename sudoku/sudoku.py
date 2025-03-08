import sys


def sudoku():
    input_file = open(sys.argv[1], "r")
    sudoku_table = []

    for line in input_file:
        row = line.split()
        sudoku_table.append(row)

    input_file.close()

    return sudoku_table


def empty_cell_coordinate(sudoku_table,selected_cell): #If there is a possibility that more than one number may appear in the checked 0's, it checks the 0's after the 0 it checks.

    for row in range(9):
        for column in range(9):

            if (row == selected_cell[0]):
                if (column <= selected_cell[1]):

                    pass
                else:

                    if sudoku_table[row][column] == "0":


                        return (row, column)
            elif (row > selected_cell[0]):

                if sudoku_table[row][column] == "0":


                    return (row, column)


    return None

def columns(sudoku_table):

    column = [[], [], [], [], [], [], [], [], []]
    for row in sudoku_table:
        for i in range(9):
            column[i].append(row[i])
    return column


def small_squares(sudoku_table):
    small_square = [[], [], [], [], [], [], [], [], []]

    for row in sudoku_table[0:3]:
        small_square[0].extend(row[0:3])
        small_square[1].extend(row[3:6])
        small_square[2].extend(row[6:9])
    for row in sudoku_table[3:6]:
        small_square[3].extend(row[0:3])
        small_square[4].extend(row[3:6])
        small_square[5].extend(row[6:9])
    for row in sudoku_table[6:9]:
        small_square[6].extend(row[0:3])
        small_square[7].extend(row[3:6])
        small_square[8].extend(row[6:9])
    return small_square


def find_number():
    sudoku_table = sudoku()

    numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    step = 1

    solved = False
    selected_cell = [-1,-1]
    while not solved:

        empty_cell = empty_cell_coordinate(sudoku_table,selected_cell)



        if not empty_cell:

            output(1,1,1)
            solved = True
            break

        existing_numbers = []
        row_index = int(empty_cell[0])
        column_index = int(empty_cell[1])
        small_square_index = (column_index // 3) + (3 * (row_index // 3))

        existing_numbers.extend(sudoku_table[row_index])  # Adds the numbers in the row containing the empty cell
        existing_numbers.extend(columns(sudoku_table)[column_index])  # Adds the numbers in the column containing the empty cell
        existing_numbers.extend(small_squares(sudoku_table)[small_square_index])  # Adds the numbers in the small square containing the empty cell

        possible_numbers = list(numbers - set(existing_numbers))


        if len(possible_numbers) == 1:
            sudoku_table[row_index][column_index] = possible_numbers[0]

            output([step,possible_numbers[0],row_index + 1,column_index + 1],sudoku_table,0)
            step += 1

            selected_cell = [-1,-1] #The selected cell was initially assigned a random value.
        else:

            selected_cell[0],selected_cell[1] = row_index,column_index


def output(title,sudoku_table,is_solved):
    output_file = open(sys.argv[2], "a")
    if is_solved == 0:

        output_file.write("------------------\n")

        output_file.write(f"Step {title[0]} - {title[1]} @ R{title[2]}C{title[3]}\n")
        output_file.write("------------------\n")
        for row in range(9):
            line = ""

            for column in range(9):
                line += str(sudoku_table[row][column]) + " "
            line = line[:-1]
            output_file.write(line + "\n")


    else:

        output_file.write("------------------")
        output_file.close()


def main():

    sudoku_solver = find_number()


if __name__ == '__main__':
    main()


