
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
import re

names = ["rahul", "ramu", "ramesh", "suresh", "indran"]

for name in names:
    m = re.findall(r'^[rs].*h$', name) # name starting with r or s, followed by any char any number of times in between, but should end with h.
    if m!= []: #if m is not empty means if there is value in 'm' then print 'm'
        print(m)

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