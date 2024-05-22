# 연습문제 7-1
# car = input('which car do u want to lant?: ')
# print(f'i will find {car}')

# # 7-2
# people = int(input('how many in your party? :'))
# if people >=9 :
#     print('u should wait')
# else:
#     print('u can take a table')

# # 7-3
# num = int(input('put ur num: '))
# if num % 10 == 0:
#     print(f'{num} is multiples of 10.')
# else:
#     print(f'{num} is not multiples of 10.')

# 7-4
# pizza = 'which toppings do you want?: '
# pizza += '\n(Enter "quit" when you are finishied.)'

# a = True
# while a:
#     a = input(pizza)
#     if a == 'quit':
#         a = False 
#     else:
#         print(f'i will add {a}')

# 7-5


# while True:
#     age = int(input('how old are u?: '))
#     if age < 3:
#         print('under 3 is free')
#         continue
#     elif 3<= age < 12:
#         print('3-12 is 10 box')
#         continue
#     else:
#         print('over 12 is 15 box')
#         continue 

# 7-8
sandwich_orders = ['tuna', 'club', 'turky']
finished_sandwiches = []

for i in sandwich_orders:
    print(f'made {i.title()} sandwich')
    finished_sandwiches.append(i)
print(f'congrathuration! u made {finished_sandwiches} sandwiches!')

# 7-9
sandwich_orders = ['tuna', 'club', 'turky']
sandwich_orders.append('pastrami')
sandwich_orders.append('pastrami')
sandwich_orders.append('pastrami')

print('now we all used pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# for i in sandwich_orders:
#     print(f'made {i.title()} sandwich')
#     finished_sandwiches.append(i)
while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print(f'now u make {made_sandwich}')
    finished_sandwiches.append(made_sandwich)

print(f'congrathuration! u made {finished_sandwiches} sandwiches!')


# 7-10
poll ={}
a=True
while a:
    name = input('plz put ur name : ')
    place = input('If you could visit one place in the world, where would you go? :')
    poll[name] = place
    finish = input('will another person respond? (respond y or n) : ')
    if finish == 'n':
        a = False
    
for name, place in poll.items():
    print(f'{name} want to visit {place}.')