Type function
It is library function of python used to check datatype of any reference (variable).
syntax
returns datatype=type(reference_name)

input():- it is library function of python used to take input from user at runtime(dynamically).
syntax
return stringvalue=input("statement")

Type casting
it is mechanism by which we can convert from one datatype to another datatype
for type casting python provides function.
1. int():- numerical string/float to int
2. float():-numerical string/int to float
3. str():-int/float to string

Operators:-
3. relational or comparison operator
<,>,>=,<=,==,!=

4. logical operator
1. and :- minimum 2 condition must be given and all the given condition must be true
2. or:- minimum 2 condition must be given and from all the given condition only one must be true
3. not:- minimum 1 condition must be given and it set true to false and false to true

id():- its predefined function or python. it returns unique memory address of given reference(variable)
id values always unique during the lifecycle of program.
syntax
return address=id(reference_name)

5. identity operator
identity operator used to compare address of given references.
1. is
if both references addresses are same it return true otherwise false
2. is not
if both references addresses are different it return true otherwise false

6. Membership operator
it is used to search given data in a collection.
1. in:- if search data is exists it return true otherwise false.
2. not in:- if search data does not exist it return true otherwise false.

7.Bitwise operator
& bitwise and
| bitwise or
^ bitwise xor
<< bitwise left shift
>> bitwise right shift
~ bitwise not

2.Assignment + Bitwise operator
&= bitwise and assign
|= bitwise or assign
^= bitwise xor assign
<<= bitwise left shift assign
>>= bitwise right shift assign
note:- bitwise not assign is not in python

Control Structure:-
it shows execution flow of program.
types of control structure
1.conditional control structure
1 if statement:- 
sytax
   if(conditions):
	#logic statement

ladder if 
syntax
if(condition):
#Logic or statements
elif(conditions):  -> can be repeated depends program need
#logic or statements
else: ->write one time
#logic or statements


3.loop or repetative control structure
1. while loop
syntax
start value/initialization
while(condition):
#logic or statement
increment/decrement


2 for in loop
syntax
1.for reference in collection:
   #logic or statement
2.for reference in range(start,stop-1,step):
	#Logic or statement
range() is a predefined function in python.
1.start default value is 0
2. stop runs n-1
3.step default value is increment by 1

Break Statement:
break statement is used to terminate a process when the given condition is satisfied

continue statement :- only skip the value from the process when the given condition is satisfied and rest of the process will run as same as

exit function:-
it is a predefined function of python which terminate a program with or without passing condition for using this function use the module - sys module for using this function first input sys module

fabonacci series
0 1 1 2 3 5............n


ASCII
Ord() it returns ascii value of given character or symbol
print(ord("a"))

chr() it return char value of given ascii code
print(chr("30"))

pass statement:-
if you dont wont to right any logic then use pass as a null statement inside the indented block 
ex.
for i in range(97,123):
    pass
print("hi")

nested for in loop
a loop within a loop is called nested for in loop.
syntax
#outer loop->for rows
for references in range(start,stop-1,step):
#inner loop->fpr columns
for refernces in range(start,stop-1, step):
#logic or statement
==================================================================================================================
02 November

List:-
python lists are just like dynamically sized arrays declared in ohter languages.in simple langauge, a python list is a collection of data enclosed in [] and separated by commas.
1.python list define in [] brackets.
2.list is collection of similar+different-different data type values
3.list is mutable(changeble)in nature.
4.list is ordered(default index start with0)
5.it allow duplicate elements.
6.list isalso a constuctor in python
7.its dybnamic in nature. no need to defined size in prior 
 syntax
  ref_var_name=[value1,value2,valueN........]
  exp. a=[11,12,13]
==============================================================================================
methods:-

1.append()



2.pop()
  this method remove the element from the list at the end/last position.
  its use with or without passing arguments.
  syntax listname.pop()or llistname.pop(index)
3.remove()
for remove an element from the list.
syntax
listname.remove(value)

4.sort()
arrange list element in ascending order.
syntax
listname.sort()
for descending order write
listname.sort(reverse=True)

5.reverse()
arrange list element in reverse order.
syntax
listname.reverse()

insert()
this method insert new element at specified index position.
syntax
listname.insert(index,value)

note:- if the given index is not found it will not generate exception, it will add the element at the end of the list.

count()
this function count duplicate element in a given list.
return intformat=listname.count(value)

clear()
for clear an existing list data.after clear list structure will be exists.
syntax
listname.clear()

copy()
it will create a new list form the existing list data.
syntax
varname=listname.copy()

index()
return index of specified value.
syntax
return index=listname.indes(value)

extend()
add elements from another list.
syntax
listname1.extend(listname2)


del 
del is a reserve word or keyword for delete any reference(or de-allocate an existing reference from memory permanently).
syntax
del ref_var_name
