
#----------------------
#REGULAR EXPRESION
#----------------------
'''
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