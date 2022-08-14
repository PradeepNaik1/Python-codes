a = [
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 1, 0, 0, 1]
]

end_i, end_j = 4, 3
path_so_far = []

count = 0
def go_to(i, j):
    global path_so_far, end_i, end_j, a, count
    if i < 0 or j < 0 or i > len(a) - 1 or j > len(a[0]) - 1:
        return
    if (i, j) in path_so_far or a[i][j] > 0:
        return
    path_so_far.append((i, j))
    a[i][j] = 2
    if (i, j) == (end_i, end_j):
        print("Found!", path_so_far)
        count+=1
        path_so_far.pop()
        return
    else:
        go_to(i + 1, j)
        if count == 1:
            return
        go_to(i, j + 1)
        if count == 1:
            return
        go_to(i, j - 1)
        if count == 1:
            return
        go_to(i - 1, j)

    return


go_to(0, 0)

for row in a:
    for val in row:
        print(val, end=" ")
    print()
