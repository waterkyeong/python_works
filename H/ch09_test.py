# person
class Dept:
    def __init__(self, me, css, ee, math) :
        self.me = me
        self.css = css
        self.ee = ee
        self.math = math

class Student(Dept):    
    def __init__(self, me, css, ee, math, sid, syear, sdept):
        super().__init__(me, css, ee, math)
        self.sid = sid
        self.syear = syear
        self.sdept = sdept

class person:
    def __init__(self,pid, pname, age) :
        self.pid = pid
        self.pname = pname
        self.age = age
        self.students = []
    

    def add_student(self, sid, syear, sdept):
        student = Student(sid, syear, sdept)
        self.students.append(student)
    
    def out_student(self):
        for i in self.students:
            print(i)

who_am_i = person 
who_am_i.add_student('',20240516,2024, 'electric')
who_am_i.add_student('',20240415,2024, 'medical')
who_am_i.add_student('',20240314,2024, 'cook')
who_am_i.out_student()
    
        



# 연습문제 9-13
from random import randint 
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1,self.sides)

dice6 = Die()













# 연습문제 9-14














# 연습문제 9-15
