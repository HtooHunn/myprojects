Sets&Dictionaries.py

includes a data type for sets.
Curly braces or the set() function can be used to create sets.

basket = {'apple',  'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

"orange" in basket
"crabgrass" in basket



 Demonstrate set operations on unique letters from two words

 a = set('abrabcadbra')
 b = set('alacazam')
 a 					# unique letters in a
 a - b 				# letters in a but not in b
 a | b 				#letters in a or b or both
 a & b 				#letters in both a and b
 a ^ b 				#letters in a or b  but not both


 x = set('23802348')
 y = set('57839012')
 x - y
 y - x
 x ^ y
 y | x
 x & y 
 x


 a = {x for x in 'abtacadabra' if x not in 'abc'}
 a

 -------

 fruits = {"apple", "banana", "cheery", "orange", "kiwi", "melon", "mango"}
 print("cheery" in fruits)

 fruits.add("cucumber")
 fruits
 fruits.update("grape") 
fruits
fruits.remove("banana")
fruits
fruits.discard("kiwi")
fruits


>>>Dictionaries

#Disctonaries

#Another useful data type built into Python is the dictionary

tel = {'jack': 4098, 'sape': 4139}
tel['sape']
tel['guido'] = 4127
tel


-----------


del tel['sape']
tel['irv'] = 4137
tel

list(tel) #Change to List

sorted(student) #Alphabet Sorting

'MgOo'

'MaMa' not in student


--------

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict(sape=4139, guido=4127, jack=4098)

{x: x**2 for x in (2, 4, 6)}

for x in 2, 4, 6:
	print(x, ':', x**2)

2 : 4
4 : 16
6 : 36

>>> for x in 2, 4, 6:
...		print(x, ':',x**2)
...		
2 : 4
4 : 16
6 : 36
>>>

{x: x**3 for x in (1, 2, 3, 4, 5)}

1 : 1
2 : 8
3 : 27
4 : 64
5 : 125


---------------

when looping through Dictionaries

knights = {'gallahad': 'the pure', 'robin': 'the brave', 'sape' : 4355}
for x, y in knights.items():
	print(x,y)


for x, y in enumerate(['tic', 'tac', 'toe']):
	print(x,y)


-------------

questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers, result):
	print('What is your {0}? It is {1}.'.format(q, a))

	#Sum

questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the holy grail' 'blue']
result = ['1', '2', '3']
for q, a, i in zip(questions, answers, result):


---------------

print('{0} and {1}, {2} and {3}'.format('spam', 'eggs', 'color', 'food'))

https://docs.python.org/3/tutorial/

=================

>>>If_Else_statement





















































