amount = 5
n = [1, 2, 3]
k = len(n)

#creating a matrix

tabular = [[0]*(amount+1) for _ in range(k+1)]

# Logic of the code
for i in range(k+1):
    tabular[i][0] = 1

for i in range(1, k+1):
    for j in range(1, amount+1):
        if n[i-1] > j:
            tabular[i][j] = tabular[i-1][j]
        else:
            tabular[i][j] = tabular[i-1][j] or tabular[i-1][(j-(n[i-1]))]

#To print the table
for i in range(amount+1):
    if i == 0:
        print('    ', end=" ")
        print(i,end='  ')
    else:
        print(i, end='   ')
print('\n')
for i in range(k+1):
    print(i,"  ", end=" ")
    for j in range(amount+1):
        print(tabular[i][j], end='   ')
    print('\n')


