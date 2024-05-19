# a = list(input())
# if a == a[::-1]:
#     print(1)
# else:
#     print(0)

# 문자 입력받고 대소문자 섞여있으니 하나로 통일해주고 그안에서 돌면서 각자 몇개인지 볼건데 중복으로 볼 필요없으니까 중복없이 만들고 각자 몇개인지 세고 가장 많은걸 출력
# 근데 이제 각자 몇개인지 센다음 가장 많은게 어떤 문자인지,,, 어떻게 도출하지? 딕셔너리 써야하나,,,

# a = input().upper()
# b = list(set(a))
# c =[]
# for i in b:
#     c.append(a.count(i))

# if c.count(max(c))>1:
#     print('?')
# elif c.count(max(c)) == 1 :
#     print(b[c.index(max(c))])
    
#N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오. 
# 첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 
# 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.
# 첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

# n,m = map(int,input().split())

# a = []
# b = []

# #  수식은 다 맞으나 백준에서는 한번 입력 시 행렬로 입력하고 싶어함! 그래서 입력 수식을 바꿔야한다.
 
# # for i in range(n):
# #     c = []
# #     for j in range(m):
# #         d = int(input())
# #         c.append(d)
# #     a.append(c)

# for i in range(n):
#     row = list(map(int,input().split()))
#     a.append(row)

# # for i in range(n):
# #     c = []
# #     for j in range(m):
# #         d = int(input())
# #         c.append(d)
# #     b.append(c)
# # print(a, b)

# for i in range(n):
#     row = list(map(int,input().split()))
#     b.append(row)
 
# c =[]
# for i in range(n):
#     c_1=[]
#     for j in range(m):
#         d = a[i][j] + b[i][j]
#         c_1.append(d)
#     c.append(c_1)   

# for i in range(len(c)):
#     for j in range(len(c[i])):
#         print(c[i][j], end=' ')
#     print()
