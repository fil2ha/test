table = [
 [".",".",".",".",".",".",".","."],
 ["p","p","p","p","p","p","p","p"],
 [".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".","."],
 ["P","P","P","P","P","P","P","P"],
 [".",".",".",".",".",".",".","."]
]
row = ["a", "b", "c", "d", "e", "f", "g", "h"]

def move(move_list):
    flag = True
    counter = 0
    first_white = []
    first_black = []
    for step in move_list:
        counter += 1
        if len(step) == 2:
            x = row.index(step[0])
            y = 8 - int(step[1])
            if table[y][x] == "." and counter % 2 != 0:
                if table[y+1][x] == "P":
                    table[y][x] = "P"
                    table[y+1][x] = "."
                    first_white.append(x)
                elif table[y+2][x] == "P" and x not in first_white:
                    table[y][x] = "P"
                    table[y + 2][x] = "."
                    first_white.append(x)
                else:
                    flag = False
                    print(f'{step} is invalid')
                    break
            elif table[y][x] == "." and counter % 2 == 0:
                if table[y-1][x] == "p":
                    table[y][x] = "p"
                    table[y-1][x] = "."
                    first_black.append(x)
                elif  table[y-2][x] == "p" and x not in first_black:
                    table[y][x] = "p"
                    table[y - 2][x] = "."
                    first_black.append(x)
        elif len(step) == 4:
            x = row.index(step[2])
            y = 8 - int(step[3])
            win = row.index(step[0])
            if table[y][x] != ".":
                if table[y-1][win] == "P" or table[y-1][win] == "p" and table[y][x] != ".":
                    table[y][x], table[y-1][win] = table[y-1][win], "."
                elif  table[y+1][win] == "P" or table[y+1][win] == "p" and table[y][x] != ".":
                    table[y][x], table[y+1][win] = table[y+1][win], "."
            else:
                flag = False
                print(f'{step} is invalid')
                break
    if flag:
        for row_table in table:
            print(row_table)


# move(["c3"])
# move(["d4", "d5", "f3", "c6", "f4"])
# move(["d4", "d5", "f3", "c6", "f4", "c5", "dxc5"])
# move(["e6"])
# move(["e4", "d5", "exf5"])