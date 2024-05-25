
#----------------------
#REGULAR EXPRESION
#----------------------
'''
import re

re.compile() - creates object pattern using given paterns
re.match() - matches only beggining of the string. r'p', 'python' -> start searching from first char of python, return match obj
re.search() - scan the whole string but returns 'match object' of only 1st occurence
re.findall() - scan all string, and retruns matching values as list
re.fullmatch() - patter should match exactly in search string. no other char shuld be there in string other than patern, it acts liek comparision operator e.g <seach-patern> == <search-string> if patrn matches, will return 'match object', if not reruns None
re.split() -
re.subn() -

Note: Repetaion charectors and its meaning
* -> 0 to n number of char repetation
+ -> 1 to n number of char repetation
? -> 0 to 1 number of repitation
{m} -> exactly m number of repetition
{m, n} -> from m minimum to n maximum number fo times of repetation
{m,n}? -> m minimum number of repetition
{m,n}+ -> n maximum number of repetaion


What is regular expression?
Regular expression is a special string which define search pattern or match pattern or split pattern.
Regular expression (regex), defines a pattern which is used to search or match with string.

Aplication of Regular Exprsion: 
1.input validation- password validatin, username, mobile number, emailid, etc.
2.parser-spliting the data form string based on given pattern
3.serach engines-
4.web scrapping-
5.chatboats-

regular expresino can be presented in two apporach.
1. string object - methods works as standalone funtions, we give two arument, pattern-string, and searh string
re.match(r'py', 'python')

2. pattern object - we create object of pattern, and use this pattern n number of times with different purposes
we use compile() for creating the object. 

ptrn_obj = re.compile(r'py')

ptrn_obj.match('search-string'), patrn_obj.search('search-string'), ptrn_obj.fullmath('search-string) etc method can be used with same patter only.

OBSERVE THE EXAMPLES TO UNDERSTAND

'''


#----------------------



#----------------------




#----------------------
# import re

# #(?=...)
# str1 = "IsaacAsimov Isaac Asimov isaacAsimov isaacObama IsaacObama isaacobama IsaacAsimov isaacasimov"
# m =re.findall(r'Isaac(?=Asimov)', str1)
# print(m)
# #Output:
# #['Isaac', 'Isaac']

# #(?!...)
# str2 = "IsaacAsimov Isaac Asimov isaacAsimov isaacObama IsaacObama isaacobama IsaacAsimov isaacasimov IsaacSingh"
# m =re.findall(r'Isaac(?!Asimov)', str2)
# print(m)
# #Output:
# #['Isaac', 'Isaac', 'Isaac']


#----------------------
# #VALIDATE ADDITION EXPRESION A+B

# import re
# expr = input("Enter Additional Expresion: ")
# m = re.search(r'[a-zA-Z]+[+][a-zA-Z]+', expr)
# if m != None:
#     print(f"{expr} ! Is Valid Addition EXpresion")
# else:
#     print(f"{expr}! is Invalid Addition Expresion")

# # output:
# # Enter Additional Expresion: A+B
# # A+B ! Is Valid Addition EXpresion

# # Enter Additional Expresion: AAAAAA+BBBBBBB
# # AAAAAA+BBBBBBB ! Is Valid Addition EXpresion

# # Enter Additional Expresion: abcd+420
# # abcd+420! is Invalid Addition Expresion



#----------------------
# # GIVING NAME TO THE GROUP 

# import re
# str1 = "rahul has joined the comapny on 12-12-2022"

# m = re.search(r'(?P<dd>[0-9]{2})-(?P<mm>[0-9]{2})-(?P<yyyy>[0-9]{4})', str1)

# print(m.group('dd'))
# print(m.group('mm'))
# print(m.group('yyyy'))

# #Accesing value using group number
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m.group(3))


# #Giving reference to the previous named group, this will match the the value which comes in resule at previous staage
# means, above dd was 12, now below we matching theat month also should be 12, giving 'dd' both in dd and mm positon.
# m2=re.search(r'(?P<dd>[0-9]{2})-(?P=dd)-(?P<yy>[0-9]{4})',str1)
# print(m2)

# # Output:
# # 12
# # 12
# # 2022

# # 12-12-2022
# # 12
# # 12
# # 2022

# # <re.Match object; span=(32, 42), match='12-12-2022'>



#----------------------
# #USERNAME VALIDATION:
# '''
# Username should start with alphabet uppercase/lowercase both ok, should conatain digits, on underscore or one dot,
# Other than this it should not accept any symbols as username. 
# '''
# import re

# usrname = input("Enter your username: ")
# m = re.fullmatch(r'^[a-zA-Z][a-zA-Z0-9]*[_\.]?[a-zA-Z0-9]*$', usrname)
# if m != None:
#     print(f"{usrname} is Valid Username !")
# else:
#     print(f"'{usrname}' is Invalid Username !")

# # ^[a-zA-Z]    -> insures username starting with alphabet, Match only one Charector from a to z
# # [a-zA-Z0-9]* -> 0 or more than 0 alphanumeric char is allowed
# # [_\.]?       -> 0 or 1, '_' or '.' is allowed, 
# # [a-zA-Z0-9]*$ -> make sures username is ending with alphnumeric char, 0 or more than 0 char is allowed at end

# #OUTPUT:
# # Enter your username: rahul.rajisngh011
# # 'rahul.rajisngh011' is Valid username !

#----------------------
# #SPECIAL CHAR INSIDE PARENTHESIS WILL ACT AS NORMAL SYMBOLS
# '''
# Special characters lose their special meaning inside sets. 
# For example, [(+*)] will match any of the literal characters '(', '+', '*', or ')'.
# '''

# import re
# str1 = "abcdd abc abcd+dcef hello*hello = hellohellohello Ok (Thank you)"

# m = re.findall(r'[(*+)]',str1)
# print(m)
# # OUTPUT:
# # ['+', '*', '(', ')']

# #SPLITING STRING
# m1 = re.split(r'[*+=(]', str1) #we can split the word from 'space' also. give like space in set [ *=()]
# print(m1)

# # OUTPUT:
# # ['+', '*', '(', ')']
# # ['abcdd abc abcd', 'dcef hello', 'hello ', ' hellohellohello Ok ', 'Thank you)']

#----------------------

# #GROUPING THE REGEX WITH PARENTHESIS AND ACCESING IT
# import re

# str1 ='''rahul joining date in new company is 20-02-2020 at 10:00:00 and he resingned on 23.06.2024 at 05:20:30 pm 
# due to health issue, his primary email id is : singh.rahulraj011@gmail.com, and secondary email id is abc@abc.com'''

# d = re.findall(r'([0-9]{2})-([0-9]{2})-([0-9]{4})', str1)
# print(d)
# # output:
# # [('20', '02', '2020')]

# str2 = input('Input any date in any format, but i am  verifying dd-mm-yyyy: ')
# d1 = re.fullmatch(r'([0-9]{2})-([0-9]{2})-([0-9]{4})', str2) #retuns 'match object'
# if d1 != None:
#     print(d1.group(0)) #prints dd-mm-yyyy
#     print(d1.group(1)) #prints dd
#     print(d1.group(2)) #prints mm
#     print(d1.group(3)) #prints yyyy

# else:
#     print(f"{str2} is invalid format, i was expecting : 'dd-mm-yyyy ")

# # OUTPUT:
# # Input any date in any format, but i am  verifying dd-mm-yyyy: 12.12.2012
# # 12.12.2012 is invalid format, i was expecting : 'dd-mm-yyyy 

# # Input any date in any format, but i am  verifying dd-mm-yyyy: 12-12-2012
# # 12-12-2012
# # 12
# # 12
# # 2012

#----------------------
# # DATE, TIME, EMAIL EXTRACTION FROM STRING 

# import re

# str1 ='''rahul joining date in new company is 20-02-2020 at 10:00:00 and he resingned on 23.06.2024 at 05:20:30 pm 
# due to health issue, his primary email id is : singh.rahulraj011@gmail.com, and secondary email id is abc@abc.com'''

# #Extracting Date
# d = re.findall(r'[0-9]{2}\.[0-9]{2}\.[0-9]{4} | [0-9]{2}-[0-9]{2}-[0-9]{4}', str1)
# print(d)

# #Extracting time
# t = re.findall(r'[0-9]{2}:[0-9]{2}:[0-9]{2}', str1)
# print(t)

# #Extracting Email
# e = re.findall(r'[a-zA-Z]+[0-9]*@[a-z]{2,12}\.[a-z]{2,3}', str1)
# print(e)


# # #OUTPUT:
# # [' 20-02-2020', '23.06.2024 ']
# # ['10:00:00', '05:20:30']
# # ['rahulraj011@gmail.com', 'abc@abc.com']

#----------------------
# # NAME VALIDATION: name should start with aphabet min 3 char max 10 char should be allowed

# import re

# name = input("Enter name to check if its valid or not?: ")
# m = re.fullmatch(r'^[a-zA-Z]{3,10}', name)#should starts with alphabet and should conatain minimum 3 char max 10 char
# if m!=None:
#     print("This Name is valide Returning 'match object' ", m)
# else:
#     print(f"'{name}' is invalid name !")


# #OUTPUT:
# # Enter name to check if its valid or not?: Rahul
# # This Name is valide Returning 'match object'  <re.Match object; span=(0, 5), match='Rahul'>

# # Enter name to check if its valid or not?: f@x
# # 'f@x' is invalid name !

#----------------------
# import re

# names = ["rahul", "ramu", "ramesh", "suresh", "indran"]

# for name in names:
#     m = re.findall(r'^[rs].*h$', name) # name starting with r or s, followed by any char any number of times in between, but should end with h.
#     if m!= []: #if m is not empty means if there is value in 'm' then print 'm'
#         print(m)

# # output:
# # ['ramesh']
# # ['suresh']

#----------------------
# #{m,n}? - returns minimum number of occurence
# import re

# list1 = re.findall(r'a{2,5}?', "aaab a aaaaab aabaaaaaab")
# list2 = re.findall(r'a{2,5}+', "aaab a aaaaab aabaaaaaab")
# print(list1)
# print(list2)

# # OUTPUT:
# # ['aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa']
# # ['aaa', 'aaaaa', 'aa', 'aaaaa']


#----------------------
# #{m, n} -> exact range of charetor
# import re
# str1 = "aab ab aaab aaaaab aaabaabaa aaaabaaabaaaaab"

# list1 = re.search(r'a{4,}', str1)
# print(list1)


#----------------------
# #re.fullmatch()
# import re

# m = re.fullmatch(r'py.*', "python")
# print(m.group(0))

#----------------------
# import re
# courses = ["python", "java", "cnn", "jython"]
# for course in courses:
#     m = re.fullmatch(r'.{3,}n$', course) #any char with 3 char minimum, should ends with n
#     if m!=None:
#         print(m.group(0))

# #output:
# #python
# #c+nn
# #jython


#----------------------
# import re

# #re.match() - search only beggining of the string, retuns the starting and ending index, if not found returns 'None'
# m = re.match(r'pyt', 'python')
# print(m)

# #re.search(r'search-pattern', 'search-string') - search from beggining to the end of the string but retruns index of 1st occurence
# m1 = re.search(r'py', 'hi python pypython rahulpy')
# print(m1)

# #re.findall(r'search-pattern', 'search-string')-search whole string and returns all occurence actual values in form of list or tuple
# m2 = re.findall(r'py', 'hi python pypython rahulpy')
# print(m2)

# #re.fullmatch(r'py', 'hi python pypython rahulpy')-its like comparision operator x == y -> True,
# #this method exactly maches the search-pattern with search string. if matches returns match object(span(index, index) otherwie 'None"
# m3 = re.fullmatch(r'rahul', 'rahul') # retruns 'match object'
# m4 = re.fullmatch(r'rahul', 'suresh') # retruns 'None'

# #re.spli()

# #re.subn()

#----------------------