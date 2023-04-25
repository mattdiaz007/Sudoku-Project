import math, random

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        # initalize the sudoku board
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0] * row_length for i in range(row_length)]
        self.box_length = int(math.sqrt(row_length))

    def get_board(self):
        # return the sudoku board
        return self.board


    def print_board(self):
        # print the sudoku board
        print(self.board)


    def valid_in_row(self, row, num):
        # checks the row for the number given as input
        # returns True if the input in not in the row, else False
        for i in self.board[row]:
            if i == num:
                return False
        return True




    def valid_in_col(self, col, num):
        # check the each list at position [col] for num, return False if found, else True
        for current_row in range(self.row_length):
            if self.board[current_row][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        # this will check the 'box,' nine in total (3x3 grid)
        # for i in the range(starting position of the row to ((row_start+3)-1 position)))
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                #  for j in the range of the starting column position to the 2 columns over
                if self.board[i][j] == num:
                    # will return False if the input is not valid within the box (the number (1-9) cannot be repeated within box)
                    return False
        return True

    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(
                row // self.box_length * self.box_length, col // self.box_length * self.box_length, num):
            return True
        else:
            return False


    def fill_box(self, row_start, col_start):
        # fills box at random with num from unused_nums
        unused_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(unused_nums)
        k = 0
        for current_row in range(row_start, row_start + 3):
            for current_col in range(col_start, col_start + 3):
                self.board[current_row][current_col] = unused_nums[k]
                k += 1
    

    def fill_diagonal(self):
        # randomly fill num along the three diagonal boxes of the board
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)


    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False


    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)


    def remove_cells(self):
        # remove cells from the board, cells to remove defined in constructor
        # keep removing cells until the num_cells_remove is == 0
        num_cells_remove = self.removed_cells
        while num_cells_remove > 0:
            row = random.randint(0, self.row_length-1)
            col = random.randint(0, self.row_length-1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                num_cells_remove -= 1

def generate_sudoku(size, removed):
    # given to us and will generate the sudoku board
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
