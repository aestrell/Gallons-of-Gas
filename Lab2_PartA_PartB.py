Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> pi = 3
>>> pi
3
>>> radius = 2
>>> radius
2
>>> area = pi * radiyus **2

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    area = pi * radiyus **2
NameError: name 'radiyus' is not defined
>>> area = pi * radius ** 2
>>> area
12
>>> radius=3
>>> radius
3
>>> area
12
>>> area = pi * (radius**2)
>>> area
27
>>> area = pi * radius ** 2
>>> area
27
>>> radius=3
>>> radius
3
>>> area
27
>>> area = pi * radius ** 2
>>> area
27
>>> 3 ** 2
9
>>> 3*2
6
>>> 3**2
9
>>> 3 * 2
6
>>> n = raw_input('Enter an int: ')
Enter an int: 3
>>> print type(n)
<type 'str'>
>>> n * 4
'3333'
>>> n ** 4

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    n ** 4
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> 
