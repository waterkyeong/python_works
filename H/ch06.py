# 연습문제 6-1, 6-7
friend01 ={'first_name':'Kim','last_name':'jane', 'age':'25', 'city':'busan'}
print(friend01)
print('\n')
friend02 ={'first_name':'choi','last_name':'poll', 'age':'30', 'city':'seoul'}
friend03 ={'first_name':'lee','last_name':'jun', 'age':'10', 'city':'ulsan'}
people = [friend01,friend02,friend03]
print(people)


# 6-2

favrorit_num ={'kim':5, 'lee':6, 'choi':7, 'hong':8, 'seo':9}
print(f'{favrorit_num["kim"]} is kim\'s fav num. ')
print(f'{favrorit_num["lee"]} is lee\'s fav num. ')
print(f'{favrorit_num["choi"]} is choi\'s fav num. ')
print(f'{favrorit_num["hong"]} is hong\'s fav num. ')
print(f'{favrorit_num["seo"]} is seo\'s fav num. ')

# 6-3,6-4

dic = { 'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.'}

for world in dic:
    print(f'{world.title()} : {dic[world]}\n')

# 6-5

riv ={'nile':'egypt', 'hangha':'china', 'naia':'america'}
for sent in riv:
    print(f'{sent.title()} is at {riv[sent]}')
for key in riv.keys():
    print(key)
for value in riv.values():
    print(value)

# 6-6
favorite_languages = {
      'jen': ['python', 'rust'],
      'sarah': ['c'],
      'edward': ['rust', 'go'],
      'phil': ['python', 'haskell']
      }
researcher = ['kim','hong','lee','phil','jen']

for name in researcher:
    if name in favorite_languages:
        print('thk for join this research')
    else:
        print('plz join this research')

# 6-8

pets = []
pet ={'name':'choco','owner':'kim'}
pets.append(pet)
pet ={'name':'meo','owner':'lee'}
pets.append(pet)
pet ={'name':'dubu','owner':'poll'}
pets.append(pet)

for pet in pets:
    print(f'{pet["name"].title()} is {pet["owner"].title()}\'s pet')

# 6-9

favorite_places ={ 'kim': ['park', 'beach'], 'hong':['house', 'malysia'], 'jhon':['korea', 'vietnam']}
for name, places in favorite_places.items():
    print(f'{name.title()}\'s favorite places :')
    for place in places:
        print(f'-{place.title()}')

#6-10

favrorit_num ={'kim':[5,10], 'lee':[6,11], 'choi':[7,12], 'hong':[8,13], 'seo':[9,14]}
for name, num in favrorit_num.items():
    print(f'{name.title()}\'s fav num :')
    for number in num:
        print(number)

# 6-11

cities ={'busan':{'country':'haundae', 'population':60000, 'fact':'idk'},
         'ulsan':{'country':'teahwa', 'population':40000, 'fact':'idktoo'},
         'seoul':{'country':'gangnam', 'population':100000, 'fact':'many'}}
for city, cityinfo in cities.items():
    print(city.title())
    print(f'-{cityinfo["country"]} \n-{cityinfo["population"]} \n-{cityinfo["fact"]}')
