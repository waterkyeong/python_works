# s = list(input())
# a= 'abcdefghijklmnopqrstuvwxyz'
# for i in a:
#     if i in s:
#         print(s.index(i),end=" ")
#     else:
#         print(-1, end=" ")

# T = int(input())

# for i in range(T):
#     R,S = input().split()
#     for i in S:
#         print(int(R)*i, end='')
#     print()

# a = input().split() #입력 The Curious Case of Benjamin Button
# b = input() #입력 The Curious Case of Benjamin Button
# print(a) # 출력['The', 'Curious', 'Case', 'of', 'Benjamin', 'Button']
# print(b) # 출력The Curious Case of Benjamin Button
# print(len(a)) #6
# print(len(b)) #35


# 1=2, 3/3/3/3/3/4/3/4 규칙없이 나눠져서 if문 써야할듯
# 1=2, abc=3 +++ 이렇게 늘어나야겠음 그리고 append 시켜서 합쳐,,,?
a = input()
b = 0
for i in a:
    if i in 'ABC':
        b = b + 3
    elif i in 'DEF':
        b = b + 4
    elif i in 'GHI':
        b = b + 5
    elif i in 'JKL':
        b = b + 6
    elif i in 'MNO':
        b = b + 7
    elif i in 'PQRS':
        b = b + 8
    elif i in 'TUV':
        b = b + 9
    else:
        b = b + 10    
print(b)