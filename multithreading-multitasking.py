

#----------------------
# MULTITHREADING - MULTITASKING APPLICATION
#----------------------
'''
#----------------------
INTERNAL STRUCTURE OF THREAD CLASS
class Thread:
def __init__(self, group= None, target=None, name= None, args= (), kwargs={}, *,dem=None):
    self.group 
    self.target 
    self.name 
    self.args 
    self.kwargs 
    self.dem 

def run(self):
    self.target()

def start(self):
    self.run()

t1 = threading.Thread(target=even, args(1,21)) -> this thread will invoke even function. 
t1.start()
NOTE: when we start the t1 thread by t1.start() method, it invokes the run() method, then run() method invokes
our target functions whatever we give. hence our logic is executed as a thread. 
#----------------------
OBSERVE BELOW CODE:
run() method is defined without args in parent class, so we cant pass value to it directly, instead we can 
create constructor and initialise its value while creating the object itself. 

import threading

# Creating a custom class by inheriting the Thread class
class evenThread(threading.Thread): 
    # Overriding __init__ method to accept parameters
    def __init__(self, a, b):
        threading.Thread.__init__(self)
        self.a = a
        self.b = b

    # Overriding run method of the Thread class
    def run(self):
        for i in range(self.a, self.b):
            if i % 2 == 0:
                print(f"{i} EVEN")

class oddThread(threading.Thread):
    # Overriding __init__ method to accept parameters
    def __init__(self, x, y):
        threading.Thread.__init__(self)
        self.x = x
        self.y = y

    # Overriding run method of the Thread class
    def run(self):
        for i in range(self.x, self.y):
            if i % 2 != 0:
                print(f"{i} ODD")

# Creating Thread objects using custom classes
even1 = evenThread(1, 21)
odd1 = oddThread(1, 21)

# Starting threads
even1.start()
odd1.start()

# Wait for both threads to complete
even1.join()
odd1.join()

'''



#----------------------
# INTER THREAD COMMUNICATIONS- EXAMPLE OF PATIENT AND DOCTOR, APPOINTMENT IS SHARED RESOUCE
'''
one patient thread is already waiting in memory for a notify, once doctor given notify statement patient thread
cathes that and execute rest of statment defined inside the patent function. appointment is shared resouce
being accesed by both patient and doctor but one at any single point of time.
'''

# import time
# from threading import *
# import random



# class appointment:

#     def patient(self):
#       condition_object.acquire()
#       print('patient john waiting for appointment') #till here code will run, and  in next statement thread will go in waiting state, once doctor give 'notify', from condition_object.wait() onward code will start executing. 
#       condition_object.wait() # Thread is in waiting state, aftter receiving notify stament from doctor code will execute next stament.
#       print('successfully got the appointment')
#       condition_object.release()

#     def doctor(self):
#       condition_object.acquire()
#       print('doctor jarry checking the time for appointment')
#       time=0
#       time=random.randint(1,13)
#       print('time checked')
#       print('appointed time is {} PM'.format(time))
#       condition_object.notify()
#       condition_object.release()


# condition_object = Condition() #Creating Condition object, Gloabl object, thats why accesible within the class
# class_obj=appointment() # Creating appointment obect

# T1 = Thread(target=class_obj.patient)
# T2 = Thread(target=class_obj.doctor)

# T1.start()
# T2.start()

# # OUTPUT:
# # patient john waiting for appointment
# # doctor jarry checking the time for appointment
# # time checked
# # appointed time is 9 PM
# # successfully got the appointment



#----------------------
# # is_alive() 
# # Return whether the thread is alive.

# # ident
# # The ‘thread identifier’ of this thread or None if the thread has not been started. This is a nonzero integer.

# import threading
# def mesg():
#     for i in range(5):
#         print("Hello Rahul !")

# t1 = threading.Thread(target=mesg)
# t1.start()

# print(t1.is_alive()) # Returns bool wether Tread is alive or dead
# print(t1.ident) # Retruns Thread identity ID. 

#OUTPUT:
# Hello Rahul !
# Hello Rahul !
# Hello Rahul !
# Hello Rahul !
# Hello Rahul !
# True
# 6138572800

#----------------------
# # SYNCRONYSING TREAD - ONE THREAD WILL RUN AT A TIME.

# import threading

# class Bus():
#     def __init__(self):
#         self.seat = 40

#         self.lock = threading.Lock() # crating Lock object and storing in instance variable 'self.lock'

#     def reserve(self, bus, name, no_of_seat):
#         self.lock.acquire() #acuireing lock by thread
#         for i in range(no_of_seat): 
#             self.seat = self.seat -1 #in each iter 1 seat is booked, hence 1 seat will minus from total seat
#         print(f"{name} has booked {no_of_seat} seat in {bus}. Available seat {self.seat}")
#         self.lock.release()


# class ReserveThread(threading.Thread): #inhariting Trhead class
#     def __init__(self, bus_obj, n, s):
#         super().__init__() #calling Thread class constructor(Thread is parent of ReseveThread class)
#         self.bus = bus_obj
#         self.name =n
#         self.seat= s

#     def run(self):
#         self.bus.reserve(self.bus, self.name, self.seat)

# bus1 = Bus()
# t1 = ReserveThread(bus1, "Rahul", 20 ) #bus1 has total 40 seat out of which Rahul booked 20 seat
# t2 = ReserveThread(bus1, "bhola", 10)  #and bhola has booked 10 seat. so still 10 seat availble in bus1 

# t1.start()
# t2.start()

#Output:
# Rahul has booked 20 seat in <__main__.Bus object at 0x102211850>. Available seat 20
# bhola has booked 10 seat in <__main__.Bus object at 0x102211850>. Available seat 10


#----------------------
# import threading


# def eat():
#     for i in range(5):
#         print("Roti")

# def drink():
#     for i in range(5):
#         print("Water")

# #Creating Thread
# t1 = threading.Thread(target=eat)
# t1.start() #mainthread calling t1 thread, t1 thread calling eat() method, 
# t1.join() # main thread calls join mehtod of t1, so t1 will complete frist, then mainthread will start executing.
# drink()

# #Output:
# # Roti
# # Roti
# # Roti
# # Roti
# # Roti
# # Water
# # Water
# # Water
# # Water
# # Water    

#----------------------

# # CLASS BASED THREADING
# import threading

# #Creating custome class by Inhariting Thread class
# class evenThread(threading.Thread):
#     #Overriding run method of class Thread
#     def run(self):
#         for i in range(1, 21):
#             if i %2 == 0:
#                 print(f"{i} EVEN")

# class oddThread(threading.Thread):
#     #Overriding run method of class Thread
#     def run(self):
#         for i in range(1, 21):
#             if i%2 != 0:
#                 print(f"{i} ODD")

# # Creating Thread object using custome class
# even1 = evenThread()
# odd1 = oddThread()

# # Calling thread 
# even1.start()
# odd1.start()


#----------------------
# FUNCTION BASED THREADING - This approach is widely used because we just have to just make changes in 
# in our fucntion , so wherever this function may have been used, changes will be reflected everywhere. 
# we dont need to make changes in  thread class. e.g: overriding the run() method. 

# import threading

# # Defining Functions even() and odd()
# def even(a, b):
#     for i in range(a, b):
#         if i%2 == 0:
#             print(f"{i} EVEN")

# def odd(x, y):
#     for i in range(x, y):
#         if i%2 != 0:
#             print(f"{i} ODD")

# # Creating threads for above functions
# t1 = threading.Thread(target=even, args=(1, 21)) #giving function name in target and its args
# t2 = threading.Thread(target=odd, kwargs={'x': 1, 'y':21}) #giving fucntion name in target and its args

# #Starting the Thread
# t1.start()
# t2.start()

#----------------------