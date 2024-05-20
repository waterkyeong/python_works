# print('hello, world!')
# age = 5;
# pi = 3.14
# msg = 'hello, world!'
# data = [1,2,3]
# mask = 'everything' or 'object'
# print(type(age), type(pi), type(msg), type(data), type(mask))

def calc(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)
    print(a ** b)

# a=2
# b=4
# calc(a, b)
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a ** b)

# a = 3.14
# b = 1.2
# calc(a, b)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)

# a = 3.14
# b = 1
# print(a, b)
# calc(a, b)

# a=5
# b=3
# print(a, b)

# b, a = map(int, input().split())
# b, a = a, b # 이게 파이썬의 스왑
# print(a, b)

# # swap
# temp = a
# a=b
# b=temp
# print(a, b)

# PI = 3.14 # 대문자는 바꾸지말고 그대로 써라는 의미



# msg = 'hello, world!'
# print(msg)

# print(msg[0])
# print(msg[1])
# msg=[0]='H'
# print(msg[1])


# a = 'hello'
# b = 'world'

# def add(a, b):
#     return a+b;
# print(f'{a},{b}, {add(1, 2)}!hahahahaha')

# msg = '    hello            '
# print(len(msg))
# print(len(msg.lstrip().rstrip())) # 새로운 객체를 만들어서 적용하여내는것. 그래서 밑에 결과가 다시 원점으로 돌아가는것이다.
# print(len(msg))

data = [1,2,3,3,3]
print(data, type(data))

# data = list() # 자바에서 data = new List(); 와 같은 객체 생성의 의미다.
# print(data, type(data))

print(data[0])
print(data[1])
print(data[2])
print(len(data))

data.append(6)
data.append(7)
data.append(8)
data.append(9)
data.append(10)
print(data, len(data))

data[3] = 4
data[4] = 5
print(data, len(data), sum(data), min(data), max(data))

data =[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
data = list(range(10, 0, -1))
print(data, type(data), sorted(data))

#10
# 10 9 8 7 6 5 4 3 2 1
# 합계를 구하시오!, 정렬하시오 최댓값을 찾으시오 최솟값을 찾으시오

# data = input()
# data= data.split() # list  이 두줄을 input().split() 이걸로 대체가능
# data = list(map(int, input().split()))
# print(data, type(data), type(data[0]))
# print(sum(data))

number = int('56')
print(number, type(number))

data = [1,2,3]
del data[1]
print(data)

# ArrayList<int> arr = new ArrayList<>();

data = [1,2,3.14, 'hello', len, range(5)]
for d in data:
    print(d, type(d))

data = [1,2,3,4,5]
print(data[len(data)-1])
print(data[::-1]) # reverse랑 같음

msg = 'aga'
print(msg == msg[::-1])

data.append(1)
print(data)
data.pop()
print(data)

data.insert(0, 333)
print(data)
data.insert(1, 1)
print(data)



del data[1]
print(data)

data.remove(3)
print(data)
data.remove(1)
print(data)

print(sorted(data)) # sorted는 원본값을 바꾸지 않는다.
print(data)

sorted_data = sorted(data)
print(sorted_data)

data.sort()
print(data)