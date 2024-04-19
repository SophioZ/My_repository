# 1 amocana
lst = [43, '22', 12, 66, 210, ['hi']]
index = lst.index(210)
print("210 is on index", index)
lst.append("hello")
print(lst)
lst.pop(2)
print(lst)
mylist_2 = lst.copy()
print(mylist_2)
# 2 amocana
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Y= [[0, 0, 0],
   [0, 0, 0],
    [0, 0, 0]]

for i in range(3):
    for j in range(3):
        Y[j][i] = M[i][j]

print("second matrix")
for row in Y:
    print(row)
