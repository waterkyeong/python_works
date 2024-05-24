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

# a =[]
# for i in range(5):
#     b=input()
#     a.append(b)
# print(a)

# for j in range(15):
#     for i in range(5):
#        if j < len(a[i]):   
#         print(a[i][j],end='')
import math
day, nt, v = map(int,input().split())
a = day - nt
if a == v :
    print(1)
else:
    print(math.ceil((v-day)/a)+1)
