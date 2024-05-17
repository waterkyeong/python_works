class Dog2:
    """클래스 Dog 정의"""

    def __init__(self, name, age):
        """클래스 Dog 생성자"""
        self.name = name
        self.age = age
        self.city = "busan"

    def sit(self):
        """개가 앉기 동작"""
        print(f'개가 앉기 {self.name}')

myDog = Dog2("hong", 10)
myDog.sit()

# muntari Log 블로그 참조해서 한번 더 공부해라. by.prof

class Car2:
    """자동차 클래스"""

    def __init__(self, make, model, year, color):
        """생성자 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.odometer = 0

    def fill_gas_tank(self):
        print(f'휘발유 차의 탱크')
    def get_descriptive_name(self):
        """자동차 객체 기술"""
        long_name = f'{self.year}식 {self.make}제조사 {self.model}\n 색상 {self.color}'
        return long_name
    
    def update_odometer(self,mileage):
        print(f'주행기록계')
class Battery():
    def __init__(self, battary_size=40):
        self.battary_size = battary_size

class ElectricCar(Car2):
    """슈퍼클래스의 subclass"""
    def __init__(self, make, model, year, color):
        """superclass의 생성자 호출"""
        super().__init__(make, model, year, color)
        self.battery = Battery() #클래스 Battary의 생성자

    def fill_gas_tank(self):
        super().fill_gas_tank()
        print(f'전기차는 탱크 없음')

my_new_car = Car2('audi', 'a6', 2024, 'red')
print(my_new_car.get_descriptive_name())
my_new_car.color = 'green'  # 클래스 객체의 attribute는 public
print(my_new_car.get_descriptive_name())
my_electric_car = ElectricCar('kia', 'k3', 2024, 'red')
my_electric_car.fill_gas_tank()


# ======================================================================
class Student:
    count = 0
    def __init__(self):
        Student.count = 1
    @classmethod
    def printing(self):
        print(f'클래스 메소드 출력 = {Student.count}')
print(f'{Student.count}') # 클래스 변수 접근
s = Student()
print(f'{Student.count}')
Student.printing() # 클래스 메소드의 호출

def initialize():
    return 1, 2, 3
_,_,b = initialize()

a=[1,2,3]
b=[4,5,6]
mergeList = [*a, *b]# *기호는 iterable 객체를 나타내고 unpacking
print(mergeList)

# class instance에 대한 인덱싱과 슬라이싱 처리
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index): # 자주 사용된다.
        return self.data[index]

mlist = MyList([1,2,3,4])
print(mlist[1:3])
s = [s1, s2, s3]
num = [5,3,7]
score = zip(s,num)
for a, b in score:
    print(f'[{a},{b}]')
