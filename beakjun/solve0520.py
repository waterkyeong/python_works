# a =[]
# for i in range(9):
#     i = list(map(int,input().split()))
#     a.append(i)
# r = 0
# c = 0
# max_a = 0
# for i in range(9):
#     for j in range(9):
#         if max_a <= a[i][j]:
#             max_a = a[i][j]
#             r = i + 1
#             c = j + 1

# print(max_a)
# print(r, c, end=' ')

a =[]
for i in range(5):
    b=list(map(str,input().split()))
    a.append(b)
print(a)
for j in range(len(a[j])):
    for i in range(len(a)):
        c = j[i+1]
        print(c,end='')