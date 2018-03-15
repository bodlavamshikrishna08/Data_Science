# to print a text word using print. 
print("hello")

# Data Types In python

Python Numbers
Python List
Python Tuple
Python Strings
Python Set
Python Dictionary
Conversion between data types

Python Numbers:

Integers, floating point numbers and complex numbers falls under Python numbers category. They are defined as "int", "float" and "complex" class in Python.

# To store a value in a variable, here "a" is a variable and 10 is a value stored in the variable. 
a = 10
# We use print() function with a variable to print the value stored in the variable.
print(a)
# To know the type of value stored in a variable we use the Type() function.Here in this case it is "INT"
print(type(a))
# Similarly assigning a value to the varaible "b" of value 10.5 which is a float value.
b = 10.5
# Then print out the value stored in the variable.
print(b)
# To know and print the type of value that the variable holds.In this case the variable holds a "float"
print(type(b))
# To store a complex number "1+2j" in variable "c".
c = 1+2j
# To print the complex value stored in the variable.
print(a, "is complex number?", isinstance(1+2j,complex))
# isinstance() is a function to check if an object belongs to a particular class.
isinstance(1+2j,complex)
# To store a string in variable named as "my_string_var"
my_string_var = "hello"
# To print the variable that holds 
print(my_string_var)
# To print the type that is stored in the string variable "my_string_var".In this case the variable holds a "string".
print(type(my_string_var))
# Boolean value.
print(10 > 5) # comparing two elements results in a boolean value
Output:: True
#creating a boolean variable "bool_value"
bool_value = 100 < 50
# To print th boolean type "true" or "false"
print(bool_value)
output:: false
# To print the class type, we use type() function. 
print(type(bool_value))
output:: <class 'bool'>

Python List:

List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible. 
All the items in a list do not need to be of the same type.
Declaring a list is pretty straight forward. Items separated by commas are enclosed within brackets [ ].

# create a list named as "my_list1", that contains 3 elements in it enclosed by[]
my_list1 = [10,20,30]
# tp print the elements in the list.
print(my_list1)
# To know the class type we use type() function.
print(type(my_list1))

# create a list with elements containing different type of values or value that has different data types such as 
# "int,"float","stirng" and a "boolean"
my_list2 = [10, 20.5, "hello", True]
# to print th elements of the list.
print(my_list2)
# To know the class type we use type() function.
print(type(my_list2))

# create a list with repeated elements.
my_list3 = [1,2,3,1,2,3]
# to print th elements of the list.
print(my_list3)
#To know the class type we use type() function.
print(type(my_list3))

Indexing of list::

# To find out a value or element in list we used indexing possition of the value in the list created and it will be printed by using folowing syntax for a list
# from above my_list3 we can find the values in the list as follows 
my_list3[0] => for first element from the starting position in the list &&
# to find the end value or element in the list then we use
my_list3[-1]

To know the range in the list then we have to use 
my_list3[1:5]
It selects list values from the 1st value  to 4th value in the list.
=> Since the list starts from the cout of (0) and when we set the range of index to (1), then it displays the (0)th element of the list.

# To replace the list with a value then we use the following syntax 
my_list[0] = 100 => this syntax is used for the replacing the first value with "100" as the index is set to "ZERO"(0)
# So to replace a certain element in the list, set the index number to that position and assign the value to be replaced.

[[Python includes following list methods]]

my_list1 = [10,20,30]
my_list2 = [10, 20.5, "hello", True]
my_list3 = [1,2,3,1,2,3]

1.list.append(obj)
my_list1.append(2)
 Appends object 2 obj to list my_list1
 my_list1 = [10,20,30,2] #the list appends the obj value 2 to the list.

2.list.count(obj)
my_list3.count(2) #to know the occurance of element 2(object) in the list.i.e, how many times 2 is repeated in the list. 
# Returns count of how many times obj occurs in list
count of 2 in my_list3 is '2'

3.list.extend(seq)
my_list1.extend(my_list2)
# Appends the contents of seq to list
my_list1 = [10,20,30,10, 20.5, "hello", True] # my_list2 is extended to My_list1, by adding elements from list2 to list1.

4.list.index(obj)
my_list1.index(10) # In this command we provide the object of a list and asks for its position in the listi.i.e, index.
# Returns the lowest index in list that obj appears
The position of 10 in the list is(0)

5.list.insert(index, obj)
my_list1.insert(0,5.5) # In this we command the list to insert the value 5.5 at zero index.i.e, at first position in list.
# Inserts object obj into list at offset index
my_list1 = [5.5,10,20,30,10, 20.5, "hello", True]

6.list.pop(obj=list[-1])
my_list1.pop() # this command pops out an element from the list and it starts from the last element of the list
# Removes and returns last object or obj from list
my_list1 = [5.5,10,20,30,10, 20.5, "hello"] # the list is modified and the element True is popped out from list.

7.list.remove(obj)
my_list1.remove(5.5) # this command is used to remove the element 5.5 from the list.
# Removes object obj from list
my_list1 = [10,20,30,10, 20.5, "hello"] # now the list no longer contains the element 5.5 in it. 

8.list.reverse() # this command is used to reverese the elements in the list.
my_list3.reverse()
# Reverses objects of list in place
my_list3 = [3,2,1,3,2,1] # the elements are reveresed.

9.list.sort([func]) # this command is used to sort the elements in the list in an order.
my_list3.sort()
# Sorts objects of list, use compare func if given
my_list3 = [1, 1, 2, 2, 3, 3] # the elements are sorted in order.

Python Tuple:

'Tuples are sequences, just like lists, tuples use parentheses"()", whereas lists use square brackets "[]".'

# creating a tuple.
my_tuple = ("hi","Hello", "Python","Scala","big data","Map reduce")
# To print the elements of the tuple.
print(my_tuple)
# To know the class type we use type() function.
print(type(my_tuple))

Indexing of tuple::

# To find out a value or element in tuple we used indexing possition of the value in the tuple created.
# it will be printed by using folowing syntax for a tuple
# from above my_tuple we can find the values in the tuple as follows 
my_tuple[0] => for first element from the starting position in the tuple 
'prints "hi" in the output.'

# To find the end value/element in the tuple then we use
my_tuple[-1] # prints out the last element of the tuple.
"Map reduce"

'To know the range in tuple then we have to use' 
my_tuple[1:5]
# It selects tuple elements from the 1st first element to 4th value in the tuple.
# => Since the tuple starts from the count of (0) and when we set the range of index to (1), then it displays the 1at element of the tuple.
('Hello', 'Python', 'Scala', 'big data')

# To replace the tuple with a value. Replacing a value in tuple is not allowed as it is immutable(cannot be changed)
my_tuple[4] = "hadoop"=> 'this syntax is used for the replacing the first value with "100" as the index is set to "ZERO"(0)'
'It displays an error because replacing elements into the tuple is not allowed'

[Result:: 
---------------------------------------
TypeErrorTraceback (most recent call last)
<ipython-input-14-aa8375ac90a1> in <module>()
----> 1 my_tuple[4] = "hadoop"

TypeError: 'tuple' object does not support item assignment]

Python Set:

A set is created by placing all the items (elements) inside curly braces {}, separated by comma or by using the built-in function set()
# Sets are lists with no duplicate entries

# create a set.
my_set = {1,2,3,4,1,2,3,4}
# to print the set
print(my_set)
# to know the class type
print(type(my_set))

#set doesn't support indexing of elements.
my_set[0]
[---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-22-158c424478a1> in <module>()
----> 1 my_set[0]

TypeError: 'set' object does not support indexing]

list => mutable  => [] or list() => that can be changed 
tuple => immutable => () or tuple() => cannot be changed 
set => Wont allow duplicates => {} or set() 
dictionary(dict) => Key value pair {key:value,key:value} 

Conversion between data types:

# To convert tuple in to list 
my_tuple = (20,30,40,50,60,70)
type(my_tuple) => tuple
# changing tuple to list 
my_list_for_tuple = list(my_tuple) , then the tuple is modified as 
my_list_for_tuple = [20, 30, 40, 50, 60, 70] => tranformed from tuple to list
type(my_list_for_tuple) => list.
# now we can index and  replace the element in to the modified tuple which is in the form of list .
my_list_for_tuple[4] = 100
my_list_for_tuple = [20, 30, 40, 50, 100, 70]

#  to convert set into list 
my_set = {1,2,3,4,1,2,3,4} 
type(my_set) => set
# changing set to list 
my_set_list =list(my_set), then the set is modified as 
my_set_list = [1, 2, 3, 4] => tranformed from set to list
type(my_set_list) => list 
# now we can index and  replace the element in to the modified set which is in the form of list .
my_set_list[2] = 1
my_set_list = [1, 2, 1, 4], list is replaced with 1 in index 2

IF ElSE statements:

Input : num = int(input("enter a number: "))
output: enter a number: 10

Input:if num > 10 :
 	   	print("num is greater than 10")
	elif num > 20 :
    		print("num is greater than 20")
	elif num > 30:
    		print("num is greater than 30")
	else:
    		print("other num")

OUTPUT : Other num.





