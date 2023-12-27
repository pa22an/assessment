s = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

p = [list(r) for r in s.split("\n")]

for i, row in enumerate(p):
    for j, v in enumerate(row):
        if v == "O":
            row_id, col_id = i, j
            while (row_id-1 >= 0 and p[row_id-1][col_id] == "."):
                p[row_id][col_id] = "."
                p[row_id-1][col_id] = "O"
                row_id -= 1

res = 0
n = len(p)
for i in p:
    res += i.count('O')*n
    n -= 1
print(res)