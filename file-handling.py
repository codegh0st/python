#----------------------
#FILE HANDLING
#----------------------

#----------------------

#----------------------
# #READING WRITING  DATA IN CSV FILE EXAMPLE 2



#----------------------
# #READING WRITING  DATA IN CSV FILE EXAMPLE 1
# import csv
# contacts = [["rahul", 9000000001],["ramu", 9000000002],["shiva", 9000000003],["bhola", 9000000004]] #nested list
# f = open("./files/contacts.csv", "w")
# writer_obj = csv.writer(f) #connection established between file object and csv reader object
# writer_obj.writerows(contacts)
# f.close()
# print("csv file created !")

# #Reading from CSV FILE

# f = open("contacts.csv", "w")
# reader_obj = csv.reader(f) #connection established between file object and csv reader object
# for row in reader_obj:
#     print(row)

#----------------------
# # READING WRITING DATA FROM FILE EXAMPLE 3
# #Write a program to store n number of student data, and calculate its evarage marks and dertermine Pass/Fail

# #Writing Student Data in students.txt
# f = open("./files/students.txt", "w")
# n = int(input("Enter How Many Data You Want To Enter: ? "))

# for i in range(1, n+1):
#     sid = input(f"Enter Student {i} ID: ")
#     sname = input(f"Enter Student {i} Name: ")
#     sub1 = input(f"Enter Student {i} Subject 1 Marks: ")
#     sub2 = input(f"Enter Student {i} Subject 2 Marks: ")
#     print(sid, sname, sub1, sub2, file=f)

# f.close()

# #Reading Student's Data to Calculate everage marks and to determine Pass/Fail
# f = open("./files/students.txt", "r")
# print("ID", "NAME", "SUB1", "SUB2", "EVG MARKS", "RESULT", sep="\t")
# while True:
#     line = f.readline()
#     if line=="":
#         break
#     id, name, su1, su2 = line.split()
#     sum1 = float(su1) + float(su2)
#     avg = sum1/2
#     result = "Pass" if float(su1)>=60 and float(su2)>=60 else "Fail"
#     print(id, name, su1, su2, avg, result, sep="\t")
# f.close()


#----------------------
# # READING DATA FROM FILE EXAMPLE 2
# # Write a program to read and count no of alphabet, digit, and special charector in given file.

# f = open("./files/employee.txt", "r")
# al, dg, sc = 0,0,0
# while True:
#     s = f.read(1) # everytime reading one charector from file
#     if s != "":
#         if s.isalpha():
#             al= al+1
#         elif s.isdigit():
#             dg = dg+1
#         else:
#             sc = sc+1

#     else:
#         break

# print(f"Total alpohabets: {al}")
# print(f"Total digits: {dg}")
# print(f"Total Special Chars: {sc}")




#----------------------
# # READING DATA FROM FILE EXAMPLE 1
# #There is two method to read form text file
# #1.read(<no of char to read>), if file empty, return empty string
# #2.readline(<no of char to read>) s=f.readline(10) will read 10 charector from file 

# f = open("./files/employee.txt", "r")
# s = f.read()
# print(s)
# f.close()



#----------------------

# #  WRITING INTO FILE EXAMPLE 3
# # Writing data into a file using writelines() function. 
# list1 = ["mango\n", "apple\n", "orange\n", "guava\n"]
# f = open("./files/fuites.txt", "w")
# f.writelines(list1)
# f.close()
# print("Fruit List has been created !")


#----------------------
# # WRITING INTO FILE EXAMPLE 2
# # Write program to wirte n number of employe details into employee.txt file using print()

# n = int(input("Enter How Many Data You Want To Save? "))
# f = open("./files/employee.txt", "w")
# for i in range(1, n+1):
#     ename = input(f"Enter Employee {i} Name: ")
#     eid = input(f"Enter Employee {i} id: ")
#     esal = input(f"Enter Employee {i} Salary: ")

#     print(eid, ename, esal, file=f) #print's defualt output is stdio(screen), with 'file=' we can change the output stream
# f.close()
# print("file created !")


#----------------------
# # WRITING INTO FILE EXAMPLE 1
# #There is Two type of files 1. is text file, it is defualt file type, specify it -> "wt"
# # 2. is binary file, specify it -> "wb", open the file to write binary data.
# f = open("./files/myfile1.txt", "w")
# f.write(str(1001 ))
# f.write("Rahul Love Pyhton ")
# f.write(" this string written by write() function")
# f.close()

#----------------------