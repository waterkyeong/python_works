# 8-1
def display_message():
    print('at ch8, learn about function')

display_message()

# 8-2
def favorite_book(title):
    print(f'Title of my favorite book is "{title.title()}"')
favorite_book('alice of wonderland')

# 8-3
# def make_shirt(ssize,smsg):
#     print(f'u r shirt size is {ssize} and want print {smsg}.')

# make_shirt(100,'IlUVNY')
# make_shirt(ssize=100,smsg='iluvny')

# 8-4
def make_shirt(ssize='L',smsg='I love Python'):
    print(f'u order shirt {ssize} size and {smsg} printing')

make_shirt()
make_shirt(ssize='M')
make_shirt(ssize='XL', smsg='i love busan')

# 8-5
def describe_city(lake, country='island'):
    print(f'{lake.title()} is at a {country.title()}')

describe_city('naiagara',country='America')
describe_city('laykarbik')
describe_city('hangha', 'china')

# 8-6
def city_country(city,cun):
    cc={'city':city, 'cun':cun}
    return cc
a = city_country('santiago', 'chile')
b = city_country('busan', 'korea')
c = city_country('bazing', 'china')
print(f'{a} \n{b} \n{c}')

# 8-7
def make_album(name,title):
    album = {"name":name, "title":title}
    return album
albums = []
albums.append(make_album('2ne1','fire'))
albums.append(make_album('infinite','chaiser'))
albums.append(make_album('seventeen','world'))
print(albums)

# 8-8
while True:
    print('if u want to quit this put "N"')
    musician = input('plz put musician\'s name :')
    if musician == "N":
        break
    title = input('plz put title of album : ')
    if title == "N":
        break
    print(make_album(musician,title))

# 8-9
    