
import importlib.resources
import time
import functools
import sys
import module1
import importlib





# Nested Class 
# Nested Class Example 1
class Person:
    class __Adress:
        def __init__(self):
            self.__street = None
            self.__city = None
        def readAddress(self):
            self.__street = input("Enter Street Name: ")
            self.__city = input("Enter City Name: ")
        
        def printAdress(self):
            return f"Street: {self.__street} City: {self.__city}"
           # print(f"Street: {self.__street} City: {self.__city}")
            
    
    def __init__(self): #initilizing person object, there will be 2 address object in person object 
        self.__name = None
        self.__add1 = Person.__Adress()
        self.__add2 = Person.__Adress()

    def readPerson(self):
        self.__name = input("Input Person Name: ")
        self.__add1.readAddress()
        self.__add2.readAddress()
    
    def printPerson(self):
        print(f"Person Name: {self.__name}")
        print(f"Adress #1: {self.__add1.printAdress()}")
        print(f"Adress #2: {self.__add2.printAdress()}")
        #self.__add1.printAdress()
        #self.__add2.printAdress()

person1 = Person()
person1.readPerson()
person1.printPerson()


# ##INHARITANCE

# class A:
#     def m1(self):
#         print("m1 of class A")
# class B(A):
#     def m2(self):
#         print("m2 of class B")
# class C(B):
#     def m3(self):
#         print("m3 of class C")
# c1 = C()
# c1.m3()
# print(C.__mro__)


#Abstract methods
# #exmaple of abstraction 2
# from abc import ABC, abstractmethod

# class Debitcard(ABC):
#     @abstractmethod
#     def withdraw(self):
#         pass

# class SBIDebitcard(Debitcard):
#     def withdraw(self):
#         print("Widrawing Money from SBI Bank")

# class HDFCDebitcard(Debitcard):
#     def withdraw(self):
#         print("widhdrawing Money from HDFC Bank")

# class ATM:
#     def width(self, obj):
#         obj.withdraw()

# sbi= SBIDebitcard()
# hdfc = HDFCDebitcard()
# atm = ATM()
# atm.width(sbi)
# atm.width(hdfc)
        




#exmaple of abstraction 1
# from abc import ABC, abstractmethod
# class shape(ABC):
#     def readDim(self):
#         self.dim1 = float(input("enter value of dim1: "))
#         self.dim2 = float(input("enter value of dim2: "))
#     @abstractmethod
#     def area(self):
#         pass

# class Triangle(shape):
#     def area(self):
#         super().readDim() #super is holding class 'shape' reference
#         return self.dim1 * self.dim2 * 0.5
    
# class Rectangle(shape):
#     def area(self):
#         super().readDim()
#         return self.dim1 * self.dim2
    
# t1 = Triangle()
# r1 = Rectangle()

# tri_area = t1.area()
# print(tri_area)

# rec_area = r1.area()
# print(rec_area)





# from abc import ABC, abstractmethod #ABC is a class of abc module, and abstract is funciton of abc module
# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass

# class Dog(Animal):
#     def eat(self):
#         print("Dog ets Non-veg")
    
# class Cat(Animal):
#     def eat(self):
#         print("Cat eats Chuha")

# d1 = Dog()
# c1 = Cat()
# d1.eat()
# c1.eat()










# #Method Overloading
# # overriding magic method
#overriding __iter__(self) method. 

# class sequenceInteger:
#     def __init__(self, list1):
#         self.__x = list1
#         self.__index = -1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.__index<len(self.__x):
#             self.__index = self.__index+1
#             return self.__x[self.__index]


# list1 = [1,2,3,4,5]
# si1 = sequenceInteger(list1)
# itobj = iter(si1)
# value = next(itobj)
# print(value)
# value2 = next(itobj)
# print(value2)


# # overrideing __new__ method. 
# # restrincing to create only one object of class A
# class A:
#     c = 0
#     obj = None
#     def __new__(cls, *args, **kwargs):
#         if A.c<1:
#             A.c = A.c+1
#             A.obj = super().__new__(cls)
#         return A.obj
    
#     def __init__(self, x, y):
#         print("inside construcor")

# a1 = A(100, 200)
# a2 = A()
# print(a1, a2)







#overriding __cacll__() method. 
# class based decorator
# class DrawStarts:
#     def __init__(self, func):
#         self.__func = func
#     def __call__(self, str):
#         print("*" * 30)
#         self.__func(str)
#         print("*" * 30)

# @DrawStarts  # creating object, will return a object with added functionality, and calling returned  object 
# def display(str): # will take any stirng
#     print(str)

# a = "i love python"
# display(a)




# #function based decorator
# def draw_star(func):
#     def wrapper(n, r):
#         print("*"*30)
#         func()
#         print("*" * 30)
#         print(n,r)
#     return wrapper

# @draw_star
# def printf():
#     print("hello world")

# printf("rahul", 1001)



#example 1
# class A:
#     def __init__(self):
#         print("inside Consutror")

#     def __call__(self):
#         print("inside call funtion")

# a1 = A()
# a1()
        






# #overriding __eq__, __hash__, __str__
# class Employee:
#     def __init__(self, n, empno):
#         self.__name = n
#         self.__empno = empno

#     def __eq__(self, other):
#         return self.__empno == other.__empno
    
#     def __hash__(self):
#         return self.__empno
    
#     def __str__(self):
#         return f"{self.__empno} {self.__name}"

# e1 = Employee("rahul", 1001)
# e2 = Employee("Ramu", 1001)
# e3 = Employee("suresh", 1002)

# set1 = {e1, e2, e3}
# for s in set1:
#     print(s) # s.__str__() #inside s, there employe object, on which str method is called, so _str_ method will be invoked. 
# print(e1 == e2) #e1.__eq__(e2), calling the eq method this way. 






# class Employee:
#     def __init__(self, n, empno):
#         self.__name = n
#         self.__empno = empno

#     def __str__(self):
#         return f"Name = {self.__name}, Employee No = {self.__empno}"



# e1 = Employee("rahul", 1001)
# e2 = Employee("raju", 1002)
# print(e1, e2, sep= "\n")



# #method overridding example 1
# class Person:
#     def __init__(self):
#         self.__name = input("Enter emp name: ")
    
#     def getName(self):
#         print(f"{self.__name}")
    
# class Employee(Person):
#     def __init__(self):
#         super().__init__()
#         self.__salary = input("input salary : ")

#     def getName(self):
#         super().getName()
#         print(f"{self.__salary}")
    
# e1 = Employee()
# e1.getName()
        

###
# class A:
#     def __init__(self):
#         self.x = 100  
#     def m1(self):
#         print("hi")
# class B(A):
#     def m2(self):
#         print("bye")

# b1 = B()

# print(b1)



###





# class A:
#     def m1(self):
#         print(" Hello parent claass A")

# class B(A):

#     def m1(self):
#         print("hell class B")
    
# b1 = B()
# b1.m1()


#write examle for hierarychcal inheriance and hibrid inheritacne example.

# # Multiple Inheritance example: 2
# class Person:
#     def __init__(self):
#         self.__name = None

#     def setName(self, n):
#         self.__name = n

#     def getName(self):
#         return self.__name
    

# class Employee:
#     def __init__(self):
#         self.__job = None

#     def setJob(self, j):
#         self.__job = j
    

#     def getJob(self):
#         return self.__job
    
# class Worker(Person, Employee):
#     def __init__(self):
#         super().__init__()  #calling person's construtor
#         Employee.__init__(self) #calling Employee's constructor, self has ref of object 'workder1'
#         self.__wage = None
    
#     def setWage(self, w):
#         self.__wage = w
    
#     def getWage(self):
#         return self.__wage
    
# worker1 = Worker()
# #setting values 
# worker1.setName("Rahul")
# worker1.setJob("DevOps Enginner")
# worker1.setWage("12000")

# #printing values
# print(f"{worker1.getName()} {worker1.getJob()} {worker1.getWage()}")







# # Multiple Inheritance 1
# class A:
#     def __init__(self):
#         print("constructor of Class A")
# class B:
#     def __init__(self):
#         print("constructor of Class B")
#     def m1(self):
#         print("m1")

# class C(A, B):
#     def __init__(self):
#         super().__init__()
#         B.__init__(self)
#         print("constructor of Class C")
        
        

# objc = C()
# objc.m1()






# #multi-level inheritance
# class Person:                     #LEVEL 1 
#     def __init__(self):
#         self.__name = None
#     def setName(self, n):
#         self.__name = n
#     def getName(self):
#         return self.__name

# class Employee(Person):         #LEVEL 2 (Employe derived from person)
#     def __init__(self):         # 'Employee' class have prperties of 'Person' class
#         super().__init__()
#         self.__job = None
#     def setJob(self, j):
#         self.__job = j
#     def getJob(self):
#         return self.__job
    
# class salariedEmployee(Employee):  #LEVEL 3 ('salariedEmployee' Derived from Person and Employee)
#     def __init__(self):            # 'slariedEmployee' class have properties of Person as well as Employee
#         super().__init__()
#         self.__salary = None
#     def setSalary(self, s):
#         self.__salary = s
#     def getSalary(self):
#         return self.__salary

# sobj = salariedEmployee()
# sobj.setName("Rahul") #method of parent classs(Person)
# sobj.setJob("DevOps Engineer") # method of dervied-class(Employee) from 'Person' class
# sobj.setSalary("12000") # method of derved from derived class(Employee)
# #All being called from only one object of 'salariedEmployee' class. 
# #Which means Person class and Employee class's properties is imported in 'salariedEmployee' class
# print(f"Employee Name:{sobj.getName()}\n{sobj.getJob()}\n{sobj.getSalary()}")








# #Single Level Inharitance

# class Person:
#     def __init__(self, n):
#         self.__name = n # __name = "Rahul" , Initialized. 
        
#     def getName(self):
#         return self.__name
    
# class Student(Person):
#     def __init__(self, r, n):
#         super().__init__(n) #calling parent constructor & passing value n="Rahul"
#         self.__roll_no = r
        
#     def getRollNo(self):
#         return self.__roll_no
    

# s1 = Student(1001, "Rahul") #Creating Student's Object,Passing roll, name to Student's constructor
# print(f"Student Name: {s1.getName()}") # Method of Parent Class 'Person'
# print(f"Student Roll Number: {s1.getRollNo()}") # Method of child class 'Student'








# #example 3

# class Person:
#     def __init__(self):
#         self.__name = None
    
#     def setName(self, n):
#         self.__name = n
#     def getName(self):
#         return self.__name


# class Employee(Person):
#     def __init__(self):
#         super().__init__()
#         self.__job = None
#     def setJob(self, j):
#         self.__job = j
#     def getJob(self):
#         return self.__job

# emp1 = Employee()
# emp1.setName("suresh")
# emp1.setJob("HR")
# print("print employe details".upper())
# print(f"Name : {emp1.getName()}, Job : {emp1.getJob()}")


# #example 2
# class A:
#     def __init__(self):
#         self.x = 100

# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.y = 200
# b1 = B()
# print(b1.x, b1.y, b1.__dict__)


# #exmaple 1
# class A:
#     def m1(self):
#         print("method m1 of class A")
    
# class B(A):
#     def m2(self):
#         print("method m2 of class B")


# b1 = B()
# b1.m1()
# b1.m2()



##AGGRIGATION
# class Dept:
#     def __init__(self, dptname, dptno):
#         self.__dpt_name = dptname
#         self.__dpt_number = dptno
    
#     def getDeptName(self):
#         return self.__dpt_name
#     def getDeptNum(self):
#         return self.__dpt_number

# class Employee:
#     def __init__(self, enum, ename, dpt):
#         self.__emp_number=enum
#         self.__emp_name=ename
#         self.__emp_dpt = dpt 

#     def printEmpDetail(self):
#         print(self.__emp_number, self.__emp_name, self.__emp_dpt.getDeptName(), self.__emp_dpt.getDeptNum())

# d1 = Dept("HR", 1001)
# e1 = Employee(201, "Ramesh", d1)
# e1.printEmpDetail()

# class Engine:
#     def __init__(self):
#         pass
#     def engStart(self):
#         print("Engine Starting...")
#     def engStop(self):
#         print("Engine Stoping...")
    
# class Car():
#     def __init__(self, engObj):
#         self.__eng = engObj
    
#     def carStart(self):
#         self.__eng.engStart()
    
#     def carStop(self):
#         self.__eng.engStop()

# e1 = Engine() #object of Engine Class
# c1 = Car(e1) # Engine object passed in Class Car. 
# c1.carStart() # using Car obect (c1)and car method (carStart,cartStop)we are able to call Engine's object
# c1.carStop()





# #COMPOSITION
# class Date:
#     def __init__(self):
#         self.__dd = None
#         self.__mm = None
#         self.__yy = None
    
#     def readDate(self):
#         self.__dd = int(input("Enter Date: dd "))
#         self.__mm = int(input("Enter Month : mm "))
#         self.__yy = int(input("Enter Year yyyy "))

#     def printDate(self):
#         print(self.__dd, self.__mm, self.__yy, sep='/')
      
    
# class Employee:
#     def __init__(self):
#         self.__name = None
#         self.__company = None
#         self.__dob = Date()
#         self.__doj = Date()

#     def readEmpDetail(self):
#         self.__name = input("Enter Emp Name: ")
#         self.__company = input("Enter Emp's Company Name: ")
#         print(f"Enter Date of Bith ")
#         self.__dob.readDate()
#         print(f"Enter Date of Joining ")
#         self.__doj.readDate()

#     def printEmpDatail(self):
#         print(f"Employe Name: {self.__name}")
#         print(f"Employee's Company: {self.__company}")
#         print("Date of Birth")
#         self.__dob.printDate()
#         print("Date of Joining")
#         self.__doj.printDate()

# emp1 = Employee()
# emp1.readEmpDetail()
# emp1.printEmpDatail()







# class Adress:
#     def __init__(self):
#         self.__city = None
#         self.__street = None
    
#     def readAddr(self):
#         self.__city = input(f"Enter Your City Name: ")
#         self.__street = int(input(f"Enter your Street Number: "))
    
#     def printAddr(self):
#         print(f"Your City: {self.__city} \nYour Street: {self.__street}")

# class Person:
#     def __init__(self):
#         self.__name = None
#         self.__addrObj = Adress() # __addObj is holding object of Adress class. 

#     def readPerson(self):
#         self.__name = input(f"Enter person's Name: ")
#         self.__addrObj.readAddr()
    
#     def printPerson(self):
#         print(f"Person Name {self.__name}")
#         self.__addrObj.printAddr()


# p1 = Person()
# p1.readPerson()
# p1.printPerson()











# #Demonstrate Class Method


# #static method
# class Math:
#     @staticmethod
#     def power(num, p):
#         return num**p
    
#     @staticmethod
#     def factorial(num):
#         if num == 0:
#             return 1
#         else:
#             fact = num*Math.factorial(num-1)
#             return fact

#     def func1(self, n, p):
#         return Math.power(n,p)  

# #print(Math.power( 5, 5))
# #print(Math.factorial(4))

# m1 = Math()
# print(m1.func1(4, 5))






# class Student:
#     __count = 0

#     def __init__(self):
#         self.__roll = 0
#         self.__name = None
#         Student.__count = Student.__count+1
#         print(f"New object created succesfully")
#     @classmethod
#     def displayObjCount(self): #class variable
#         print(f"Total Object: {Student.__count} ") #class variable
    
# std1 = Student()
# std2 = Student()
# Student.displayObjCount() #accesing, class var using class mehod. 


    



# class A:
#     def msg(self):
#         print("msg() inside class A")
#     @classmethod
#     def msg1(cls):
#         print("msg2() inside class A")

# a1 = A()

# a1.msg()
# a1.msg1()
# A.msg1()




# class B:
#     pass

# b1 = B()
# b2 = B()
# setattr(b1, "name", "ramu")
# setattr(b2, "name", "suresh")
# print(b1.__dict__)
# print(b2.__dict__)
# print(getattr(b1, "name"))


# class  A:
#     def __init__(self):
#         self.x =100
#         self.y = 200

# a1 = A()
# a1.y = 500
# print(a1.x, a1.y)
# print(a1.__dict__)
# a1.__dict__.update({"p":600, "u": 700}) # updating a1 attribute after object creation. 
# print(a1.__dict__)

#Class Level Variable. 

# #***********************
# #FINISH IT LATER

# '''
# #Create following application using class and object. use instance variable. 
# # usel class variable for those values which are common for all object. 
# ******ATM*****
# 1.Deposit
# 2.Withdraw
# 3.Check Balance
# 4. Exit
# Enter Your Option 1
# Enter Amount to Deposit 2000

# '''
# class Accounts:
#     __min_balance = 5000
#     __acounts = []
#     def __init__(self, ac, n, bl):
#         Accounts.__acounts = {ac:[n,bl]}
    

#     def deposte(self, amt):
#         self.__ballance = self.__ballance+amt
#         print(f"Amount Succesfully Deposited. ")
#         print(f"Cureent Balance : {self.__ballance}")

#     def withdraw(self, amt):
#         if self.__ballance>=amt+self.__min_balance:  # means 5k har samay rahna chahiye account me.
#             self.__ballance = self.__ballance-amt
#             print(f"Amount {amt} Withdrawn from Account {Accounts.__acounts}")
#             print(f"Current Balance: {self.__ballance}")
#         else:
#             print("Insufficient balance")

#     def displayallAcounts(self):
#         for acount in Accounts.__acounts.items:
#             print(acount[0], acount[1][0], acount[1][1])


#     def checkBallance(self):
#         print(f" Curent Balance : {Accounts.__acounts}")



# a1 = Accounts(1001, "ramu", 4000)
# a1.checkBallance()

# # def main():
# #     while True:
# #         print("********ATM************")
# #         print("1. Deposite")
# #         print ("2.Withdraw")
# #         print("3.Check balance")
# #         print("4.Create Acount")
# #         print("5.Exit")


# #         opt = int(input("Input your choice: "))
# #         if opt == 4:




# #*********************************



# List all the package which is being managed by pip, 
#from a log file which has n number of lines. 

#packages.txt
# '''
# pandas 1.03.5 pipy
# numpy 3.4.23 pipy
# scikit-learn 0.24.2 conda
# matplotlib 3.4.3 pipy
# tensorflow 2.7.0 conda
# keras 2.8.0 pipy
# opencv-python 4.5.4 pipy
# requests 2.26.0 pipy
# beautifulsoup4 4.10.0 pipy
# sqlalchemy 1.4.25 conda
# flask 2.1.0 pipy
# django 4.0.2 pipy
# '''


# with open("packages.txt", "r") as file:
#     for line in file:
#         list1 = line.strip().split()
#         if "pipy" in list1:
#             print(f"{list1[0]} == {list1[1]}")







#Write a program where school name will be common for all students, but name, roll
#will differ from student to student. 
#Example2 

# class Student:
#     college_name = "Charwaha Vidhyalay"
#     def __init__(self, n, r):
#         self.__name = n
#         self.__roll = r

#     def studentDetails(self):
#         print(f"{self.__name} - {self.__roll} - {Student.college_name}")

# std1 = Student("Ramu", 1001)
# std2 = Student("Manohar", 1002)

# std1.studentDetails()
# std2.studentDetails()



# #example 1

# class Circle:
#     pi = 3.147
#     def __init__(self, r):
#         self.__radious = r

#     def findArea(self):
#         area = Circle.pi*self.__radious**2 #area = pi*r*r
#         return area
    
# c1 = Circle(1.5)
# c2 = Circle(2.5)

# a1 = c1.findArea()
# a2 = c2.findArea()

# print(f"area of circle 1 : {a1:.2f}, area of Circle2:{a2:.2f} ")


#Instance Variable

#setter and getter
#Write a program to read n number of player's name and score , 
#and calculate total number of score. use class and object, 
#Demonstrate Getter and Setter concept

# class Player:
#     def __init__(self, n, s):
#         self.__name = n
#         self.__score = s

#     def getName(self):
#         return self.__name
    
#     def getScore(self):
#         return self.__score
    

# n =int(input("How many player you want to add :? "))

# #creating list of player object, having player name and score
# list1 = list()
# for i in range(n):
#     name = input(f"input player{i+1} Name: ")
#     score = int(input(f"input {name}'s score: "))
#     p = Player(name, score)
#     list1.append(p)

# total_score = 0
# print("--------SCORECARD-------")
# for p in list1:
#     print(f"{p.getName().upper()} ---> {p.getScore()}")
#     total_score = total_score+p.getScore()
# print(f"INDIA'S TOTAL SCORE: {total_score}")





# class Human:
#     def __init__(self):
#         self.hight = 0
#         self.hair=None
#         self.color=None

#     def set_values(self, ht, hr, clr):
#         self.hight=ht
#         self.hair=hr
#         self.color=clr

# ramu = Human()
# ramu.set_values(5, "black", "Fair")

# print(f"Ramu is {ramu.hight}ft Long, His Hair is {ramu.hair}, and Skin color is {ramu.color}")





# class Student:
#     def __init__(self):
#         self.rollno = 1001
#         self.course = "python"
#         self.fee = 4000.0

#     def display(self):
#         print(self.rollno, self.course, self.fee)

# std1 = Student()
# print(std1.rollno)
# std1.display()



# class Employee:
#     def create_instance_var(self):
#         self.rollno=101
#         self.name="suresh"

#     def printf(self):
#         print(self.rollno, self.name)

# emp1 = Employee()
# emp1.create_instance_var()
# emp1.printf()
# #print(emp1.rollno, emp1.name)



# class Robo:
#     def talk(self, msg):
#         print(f"Hi i can say {msg}")

# robo1 = Robo()
# robo1.x =100
# print(robo1.x)


# #students class

# class Calculator:
#     def __init__(self):
#         self.__num1 = 10
#         self.__num2 = 20

#     def add(self):
#         res1 = self.__num1 + self.__num2
#         return res1

# calc1 = Calculator()
# print(calc1.add())





# class Student:
#     def detail(self, r, n):
#         print(f"student detail..{r}  {n}")
#     def everageMarks(self, sub1, sub2, sub3):
#         totalMarks = sub1+sub2+sub3
#         print(self)
#         return totalMarks//3

# raj = Student()
# raj.detail(101, "rahul")
# everage = raj.everageMarks(33,45,55)
# print(everage)
# print(hex(id(raj)))













# # my first class
# class  Car:
#     def star(self):
#         print("Car starting...")
    
#     def stop(self):
#         print("Car Stoping...")

# audi = Car()
# audi.star()

# benz = Car()
# benz.stop()







# # Different Style of Importing Moudules From Package
# import package1.m1
# package1.m1.fun1()

# from package1 import m1
# m1.fun1()

# from package1.m1 import *
# fun1()





# #Write a program to import any module. 
# name = input("write module name to import: ")
# module = importlib.import_module(name)
# print(module.__name__)
# print(module.__file__)
# print(module.__doc__)

# # Import library Dinamically. math handles +ve numbers, and cmath handle -ve numbers.
# # so according to the input number this code calculates the sqrt.  
# m1 = importlib.import_module("math")
# x = m1.sqrt(44)
# print(x)

# n = eval(input("input any number +ve / -ve :"))
# if n>0:
#     m2 = importlib.import_module("math")
#     res1 = m2.sqrt(n)
#     print(res1)
# else:
#     m3 = importlib.import_module("cmath")
#     res2 = m3.sqrt(n)
#     print(res2)

# MODULE IN PYTHON
#print(module1.__name__)


# from module1 import *
# # print(module1.x)
# # print(module1.y)
# # print(module1.add(23,45))
# print(locals())
# print(sub(5,4))



#write a program to find factorial of input number using recursion means without using loop


# # finding factorial of given number without recursion
# num = int(input("Enter number to findout factorial: "))
# list1 = [i for i in range(1, num+1)]
# print(list1)
# a = functools.reduce(lambda x, y: x*y, list1)
# print(a)


# #write a program to print from n to 1 without using looping statements. 
# def func1(n):
#     if n>=1:
#         print(n)
#         func1(n-1)
# func1(5)

# write recursive func to print 1 to n. Showing Stack
# def func1(n):
#     if n>1:
#         func1(n-1)
#     print(n)
# func1(5)

# #write a program to print 1 to 10 without using looping statements. 

# n = 1
# def func1():
#     global n
#     if n<=10:
#         print(n)
#         n = n+1
#         func1()
# func1()


#recursion
# def func1():
#     print("hello")
#     func1()

# #main
# sys.setrecursionlimit(500)
# print(sys.getrecursionlimit())
# #func1()




# #functools.reduce()
# list1 = [10,20,30, 40]
# a = functools.reduce(lambda x,y:x+y, list1)
# b = functools.reduce(lambda x,y: x if x>y else y, list1) # 
# print(b)


## lambda functions

# #map function2 
# list1 = [10, 20, 30, 40]
# list2 = [20, 40, 60, 80, 100]
# a = map(lambda x,y: x+y, list1, list2)
# l1 = list(a)
# print(l1)


# #map function1. 
# list1 = ["10", "20", "30", "40"]
# a = map(int, list1)
# l1 = list(a)
# print(l1)





#filter function:

# #write a filter fucntion wich filter all the names starting with 'k', 
# # all the name wich ends with 'h'.

# namesList=["naresh", "suresh", "ramesh", "kishore", "rajesh", "kiran", "raman"]

# print("----names Ending with 'h'----")
# a = filter(lambda name:name[-1]=='h', namesList)
# nlist = list(a)
# for name in nlist:
#     print(name)

# print("----Name Starting with 'k'----")
# b = filter(lambda name:name[0]=='k', namesList)
# nlist1 = list(b)
# for name in nlist1:
#     print(name)



# #Even/odd number in list. 
# list1 = [1,2,3,4,5,6,7,8,9,10]
# a = filter(lambda n:n%2 == 0, list1)
# b = filter(lambda n:n%2!=0, list1)
# for i in a:
#     print(f"Even Number: {i}")
# for i in b:
#     print(f"Odd number: {i}")




#lambda with parameter/arguments

#wrtie a calculator. 
# def calulator(a,b, opr):
#     res = opr(a,b)
#     return res

# z = calulator(40,5, lambda x,y: x*y)
# print(z)



#passing lambda func to another  function
# def function1(func):
#     func()

# function1(lambda:print("hello pyton")) # this lambda will be passed in func and will be called.
# function1(lambda:print("my name is rahul"))


#write a lambda function ko add two numbers
# add = lambda x,y: x+y
# mul = lambda x,y: x*y
# sub = lambda x,y: x-y

# res1 = add(4,5)
# res2 = mul(4,5)
# res3 = sub(4,5)
# print(res1, res2, res3)

#lambda without parameter
# a = lambda: print("hi lambda")
# a()
# a()
# a()






#generator expression concept


# genrator = (value for value in range(1,11))
# for i in genrator:
#    print(i)





## Generator concepts. 

# def float_iter(a,b):
#     while a<=b:
#         yield(a)
#         a = a+.5  #each time 'a' me .5 add kar kar ke iterator object me value store kar raha hai. 


# f =float_iter(1.0, 10.0)
# for value in f:
#     print(value, end="")





# write a funciton to show the closure concept. 

# def msg_rec(msg):
#     def send_to(name):
#         print(f"Hi {name}, {msg}")
#     return send_to

# msg1 = msg_rec("Happy Holi")
# msg_withname= msg1("Suresh")





#-------------

# def find_power():
#     num =5
#     def power(p):
#         res = num**p
#         print(f"power of 5 to the power{p} = {res}")

#     return power

# pwr = find_power()
# pwr(2)






#decorators

# #write a program to present decorator chaining, multiple decorator on one function

# def draw_dollar(fun):
#     def update_fun():
#         print("$"*50)
#         fun()
#         print("$"*50)
#     return update_fun
# def draw_stars(fun):
#     def update_fun():
#         print("*"*50)
#         fun()
#         print("*"*50)
#     return update_fun

# @draw_dollar #2nd this decorator will apply on output of draw_stars
# @draw_stars #1st this decorator will apply on display()
# def display():
#     print("PYTHON LANGUAGE")


# display() # calling display function






# # # write a decorator which convert the name in upper case. 


# def display_upper(fun):
#     def update_fun(*data):
#         for name in data:
#             print(name.upper())
#     return update_fun


# @display_upper
# def display_name(*data):
#     for name in data:
#         print(name)

# name_list= ["rahul", "ramu", "raju"]
# display_name(*name_list)

# ##-----------------------

# def timer(fun):
#     def update_fun(x,y):
#         start_time = time.time()
#         fun(x,y)
#         end_time =time.time()
#         total_time = end_time-start_time
#         print(f"total time taken to run this fun {fun.__name__} : {total_time}")
#     return update_fun


# @timer
# def fun2(a,b):
#     print("app is running please wait...")
#     print(f" sum of two numbr is {a+b}")
#     time.sleep(2)

# fun2(10, 20)


# @timer
# def fun1():
#     print("test function")
#     time.sleep(5)

# fun1()

# #create a division funtion, which devide two interger, add extra funtionality
# # to this function that if devide by '0' is given, it should not through error
# # instead it should return 0



# def smart_div(fun):
#     def updated_fun(x,y):
#         if y == 0:
#             return 0
#         else:
#            return fun(x,y)
#     return updated_fun

# @smart_div
# def division(a,b):
#     c = a/b
#     return c

# n1 = int(input("enter enter integer no 1 :"))
# n2 = int(input("enter enter integer no 2 :"))
# n3 = division(n1, n2)

# print(f"division of {n1}/{n2} = {n3}")






# ## draw line decorator.

# def draw_line(a):
#     def wrapper():
#         print("**************")
#         a()
#         print("**************")

#     return wrapper

# @draw_line
# def fun1():
#     print("I love python")
# fun1()

# a = draw_line(fun1)
# a()




##--------------------
# def func1():
#     print("print inside fun1")

# def func2(a):
#    # print("inside func2")
#     def func3():
#         print("added functionality in func1")
#         func1()
#     return func3
    


# f3 = func2(func1)

# f3()


















# Functions

#Nested Functions









# **kwargs

# def func(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# func(a="apple", b="boy", c="cat")

# # just random question from students
# a = [0,1,2,3]
# for a[-1] in a:
#     print(a[-1])


# def func1(**kwargs):
#     mxsale= 0
#     sales_man = ""
#     for name, sale in kwargs.items():
#         if mxsale<sale:
#             mxsale=sale
#             sales_man = name
#         return name, mxsale

# dict1={"ramesh":5000, "rajesh":6000, "raju":70000}
# output=func1(**dict1)
# print(f"sale man {output[0]}, has sold mx {output[1]}")






# # Write a function to find the maximum of any lenth. 

# def max(*num):
#     mx = 0
#     for i in num:
#         if mx<i:
#             mx=i
#     print(f"max value is: {mx}")


# max(1,2,3,4,5)
# list1 = [89, 34, 34, 21, 333]
# max(*list1)




# def func1(*a):
#     print(a)

# list1 = [10,20,30,40,50]
# func1(*list1)



# # write a function to sort in assenening or decending order. 
# # if reverse will be False then accending if reverse=True Decending order. 

# def sort(list1, reverse=False):
#     if reverse:  # if in reverse True will be passed, this code will run, decending order
#         for i in range(len(list1)):
#             for j in range(len(list1)-1):
#                 if list1[j]<list1[j+1]:
#                     list1[j], list1[j+1]=list1[j+1], list1[j]
#     else: # if reverse = False, this code will run, accending order
#         for i in range(len(list1)):
#             for j in range(len(list1)-1):
#                 if list1[j]>list1[j+1]:
#                   list1[j], list1[j+1]=list1[j+1], list1[j]

# list1 = [40,50, 20, 30, 5, 9, 70]
# sort(list1, reverse=True)
# print(list1)


# write a function to calculate simple intereset 
# # will take two reqcuried arigument, and one optional / default argument. 

# def simple_int(amt, time, rate=1.5):
#     si = amt*time*rate
#     return si


# a = simple_int(1000, 2, 2.5)
# print(a)









# # write a function to find prime number. should retrun true or false.

# def is_prime(num):
#     c =0
#     flag = True
#     for i in range(1, num+1):
#         if num%i == 0:
#             c =c+1
#     if c>2:
#         flag = False
#     return flag


# def main():
#     a = is_prime(41)
#     print(a)

# main()



#There is no conpect of fucnion overloading in python
# def func1(x):
#     print(x)

# def func1():
#     print("java")
# def func1():
#     print("pyhon")


# func1()


# def draw_line(ch, lenth):
#     for i in range(lenth):
#         print(ch, end="")
#     print()

# draw_line("-", 80)
# print("Rahul Raj singh")
# draw_line("-", 80)


# x =100
# def func1():
#     x = 200
#     print(f"local x inside func1 {x} ")


# def func2():
#     global x
#     x += 300 # adding 300 in global x = 100, result will be = 400
#     print(f"global x inside func2 {x}")

# def func3():
#     x = 500
#     print(f"local x inside func3 {x}")
#     glob_x = globals()
#     print(f"global x inside func3 {glob_x['x']}")

# func1()
# func2()
# func3()








# x =100
# def func1():
#     print(x)


# def func2():
#     x = 300  # we can only acces the global varible, can not modify the g.v from inside any func(), x L.V will be created.
#     print(x)
#     print(locals()['x'])


# func1()
# func2()



# print(globals())
# print("locals",locals())




# x = 0
# def fun1():
#     x = 100
#     y = 200
#     dict1 = locals()
#     print(dict1)
# print(id(x),x)

# x = 1
# def fun2():
#     print(id(x),x)
#     g_dict = globals()
#     print(g_dict)
# fun1()
# fun2()