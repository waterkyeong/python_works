# # data = [1, 2,3]

# # for d in data :
# #     print(d, end=' ')
# # data[1]=  5
# # print('-', data[1])
# # string = 'hello'
# # for s in string:
# #     print(s, end=' ')
# # # string[1] = 'E'
# # print('-', string[1])
# # data = (1,2,3)
# # for i in data:
# #     print(i)
# # # data[1] = 5

# # data2 = [i**2 for i in data if i**2 < 5]
# # print(data2,type(data2))

# # data3 =[]             # 위 data2의 원래 정석 풀이방법 =  data3
# # for i in data:
# #     if i**2 < 5:
# #         data3.append(i**2)
# # print(data3)

# # for(int i = 0; i < 10; i++) 예전 문법이다..! d보통 코테 잘 치는 친구들은 이걸 잘쓴다.
# # for(item : array) # 배열을 몰라도 돌릴수있는 형태로 많이 바꼈다. 하지만 현업에서는 이런 간단한 실용적인걸 잘 쓰는걸 좋아한다.
# # data = [1,2,3,4,5]

# # for d in data:
# #     print(d)

# # for i in range(10):
# #     print(i, end=' ')
# #     for d in data:
# #         print(d)

# # for _ in range(10):
# #     print('a', end=' ')

# # for idx, d in enumerate(data):
# #     print(idx, d)

# # data_2d =  [[1,2,3],[4,5,6]]
# # for d in data_2d:
# #     for d in data:
# #         print(d, end=' ')
# #     print()

# # range(1,10)
# # 1 x 1 = 1
# # 1 x 2 = 2
# # 1 x 3 = 3
# # ...
# # 2 x 1 = 2
# # 2 x 2 = 4
# # 2 x 3 = 6
# # ...
# # 9 x 9= 81

# for i in range(1,10):
#     for j in range(1,10):
#         print(f'{i} x {j} = {i*j}')
#     print()

# # range(1,11) - 1부터 10까지
# # sum,min,max,average = sum / len ---------------------------------------------- 이거 풀어보기

# for i in range(1,11):
#     print()

# # a = everything or object
# data = [1, 3.14, 'hello', max, range]
# for d in data:
#     print(d, type(d))
#     print('next')

# for i in range(len(data)):
#     print(data[i], type(data[i]))
# data[0]
# data[1]


# # 연습문제 4-1
# pizza = ['peperoni', 'combi', 'photato']
# for p in pizza:
#     print(f'i like {p} pizza')
# print('i really like pizza')

# #  4-2
# animal = ['dog', 'rabbit', 'cat']
# for a in animal:
#     print(f'{a} is very kind animal')
# print('they have a nice tali.')

# # ============================================

# # data = list(range(1, 1001))
# # print(data, type(data))


# # data = range(1, 1001)
# # print(data, type(data))
# # for d in data:
# #     print(d,end=' ')

# # data = range(1, 1001, 2) # 뒤의 2는 2칸씩 띄우란 의미 즉 홀수만 나오게된다. 짝수만 나오려면 2, 1001, 2
# # print(data, type(data))
# # for d in data:
# #     print(d,end=' ')

# # # 연습문제 4-3
# # data = range(1,21)
# # for i in data:
# #     print(i)

# # 4-4
# # data = range(1,1000001)
# # for i in data:
# #     print(i)

# # 4-5
# data = list(range(1,1000001))
# print(min(data))
# print(max(data))
# print(sum(data))

# # print(sum(range(1,1000001))) 이런식으로 바로 출력도 가능하다.

# # 4-6

# data = range(1,21,2)
# for i in data:
#     print(i)

# # 4-7

# data = range(3, 31, 3)
# for d in data:
#     print(d)

# # 4-8

# data=[]
# for i in range(1,11):
#     data.append(i**3)
# print(data)

# # 4-9

# print([i**3 for i in range(1,11)])

# # =============================================================================

# # [1,11)
# data = list(range(1,11))
# # [1,5)
# # print(data, data[1:5], sep='\n')
# # print(data, data[-2], sep='\n')
# print(data, data[:5], data[5:], sep='\n') # 반으로 자르고 싶을때 유용하게 사용가능 [:5][5:]
# print (data, data[::-1], sorted(data, reverse=True), sep='\n')

# def swap(a, b):
#     temp = a
#     a=b
#     b=temp
#     # a,b = b,a

# a, b = 1, 2
# print(a, b)
# swap(a, b)
# print(a, b)

# data = [1,2,3]
# data2= data[:]
# data2[1] = 5
# print(data, data2, sep='\n')

# data = [1,2,3]
# data2= data.copy()
# data2[1] = 5
# print(data, data2, sep='\n')

# # 연습문제 4-10

# data = ['a','b','c','d','f','g','h','i','j']
# print(f'리스트의 첫 세 항목은 :{data[0:3]}')
# print(f'리스트의 중간 세 항목은 :{data[3:6]}')
# print(f'리스트의 마지막 세 항목은 :{data[6:]}')

# # 4-11
# friend_pizzas = pizza[:]
# pizza.append('hawaian')
# friend_pizzas.append('bulgogi')
# print('which i like pizza is')
# for b in pizza:
#     print(f'-{b}')
# print('\n which my friend like pizza is')
# for a in friend_pizzas:
#     print(f'-{a}')



# # ------------------------------------------------------------------------------------------------------------
# # ch5 if문 짤때 else 없이 if만 있다면 프로그램이 틀리진 않았지만 논리적 오류이다. 앞으로 코딩할때 else는 뭐할지 생각해보기!

# a=5
# if(a<100):
#     print('right!')

# score = int(input())
# if (90<=score) and (score<=100): #if (90 <= score <= 100):
#     print('A')
# elif (80 <= score) and (score <90):
#     print('B')
# else:
#     print('F')

# a = 5
# if a == 5:
#     print('right')

# msg = 'hello'
# if msg == 'hello':
#     print('right')

# data=[1,2,3]    # list 비교 가능하나 수와 내용이 다 같아야한다.
# if data == [1,2,3]:
#     print('right')

# if data:
#     print('right!!')

# data=[]    
# if data == [1,2,3]:
#     print('right')
# if data:        #빈 리스트일땐 작동하지 않는다.
#     print('right!!')

data=[1,2,3]   
if 3 in data:
    print('Here!')

string ='hello'
if 'e' in string:
    print('Here!!!')

string ='hello'
print(string.capitalize())
if 'e' in string:
    print('Here!!!')

a = 5
print( a ==5 )
print( a !=5 )

msg1 = 'hello'
msg2 = 'Hello'
print(msg1>msg2)

a=3
if a <5 or a>10:
    print('a')

# A B   AND  OR
# 0 0   0    0
# 0 1   0    1
# 1 0   0    1
# 1 1   1    1

# 연습문제 5-1

car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car=='audi')

# 연습문제 5-3
alien_color = 'green'

if alien_color == 'green':
    print('player got 5point!')
if alien_color == 'red':
    print('player got 5point!')

# 5-4
alien_color='red'

if alien_color == 'green':
    print('player got 5point!')
else:
    print('player got 10point!')

if alien_color == 'green':
    print('player got 5point!')
if alien_color != 'green':
    print('player got 10point!')

# 5-5

if alien_color == 'green':
    print('player got 5point!')
elif alien_color == 'yello':
    print('player got 10point!')
else: 
    print('player got 15point!')

alien_color = 'yello'

if alien_color == 'green':
    print('player got 5point!')
elif alien_color == 'yello':
    print('player got 10point!')
else: 
    print('player got 15point!')

alien_color = 'green'

if alien_color == 'green':
    print('player got 5point!')
elif alien_color == 'yello':
    print('player got 10point!')
else: 
    print('player got 15point!')

# 5-6

age= 20

if age <2:
    print('baby')
elif age >=2 and age <4:
    print('toddler')
elif age >=4 and age <13:
    print('kid')
elif age >=13 and age <20:
    print('teenager')
elif age>=20 and age <65:
    print('adult')
else: 
    print('elder')
    
# 5-7

favorite_fruits = ['apple','banana','pear'] 

if 'apple' in favorite_fruits:
    print('u really luv apple!')
if 'banana' in favorite_fruits:
    print('u really luv banana!')
if 'pear' in favorite_fruits:
    print('u really luv pear!')
if 'mango' in favorite_fruits:
    print('u really luv mango!')
if 'strawberry' in favorite_fruits:
    print('u really luv strawberry!')


# ==============================================================================================

data = [1,2,3]
for d in data:
    if d < 2:
        print(d)
    else:
        print('wrong!')

# 연습문제 5-8

name = ['kim','park', 'admin','lee','choi']
for i in name:
    if i == 'admin':
        print('welcom admin, do you want statue report?')
    else:
        print(f'welcome{i}, thk for log-in again.')

# 5-9
name = []
if name:
    print('u shoud need user')

# 5-10 

current_users = ['Kim','Park','Choi','Lee','Seo']
new_users = ['kim','hong','jason','lee','jane']

for i in new_users:
    if i in current_users:
        print('plz write another name')
    else: 
        print('u can use this name')


current_users_lower = [i.lower() for i in current_users]

for i in new_users:
    if i.lower() in current_users_lower:
        print(f'{i} is already in our web')
    else:
        print(f'{i} is avaliable!')
