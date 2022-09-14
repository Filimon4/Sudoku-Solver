import pyautogui as pg
import time

board = []

while True:
    row = list(input("Row: "))
    ints = []

    for n in row:
        ints.append(int(n))
    board.append(ints)

    if len(board) == 9:
        break
    print("Row " + str(len(board)) + " complete")

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10):
        if valid(bo, i, (row,col)):
            bo[row][col] = i

            if solve(bo):
                return True
            bo[row][col] = 0
    return False

def valid(bo,num,pos):
    # Check row
    for i in range(len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for y in range(box_y * 3, box_y * 3 + 3):
        for x in range(box_x * 3, box_x * 3 + 3):
            if bo[y][x] == num and (y,x) != pos:
                return False
    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                if bo[i][j] == 0:
                    print(" ")
                else:
                    print(bo[i][j])
            else:
                if bo[i][j] == 0:
                    print("  ", end="")
                else:
                    print(str(bo[i][j]) + " ", end="")
                    

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)
    return None

def solve_sudoku(bo):
    final = []
    str_final = []
    for i in range(9):
        final.append(bo[i])

    for lists in final:
        for num in lists:
            str_final.append(str(num))

    counter = []

    for num in str_final:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter) % 9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')

print_board(board)
print("################################")
solve(board)
print_board(board)
solve_sudoku(board)