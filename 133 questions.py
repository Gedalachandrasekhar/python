Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Write a statement(WAS) to print “Hello World” by using shell
>>> a='Hello World'
>>> a
'Hello World'
>>> #WAS to print “Hello world” by using python print function
>>> a='Hello World'
>>> print(a)
Hello World
>>> #WAS to initialize variable and value as 50.
>>> v=50
>>> #WAS to initialize multivariable value are 150,120,250(take your own variable names
>>> a,b,c=150,120,250
>>> #WAS to print the type of the data in the given value.
>>> a=50
>>> type(a)
<class 'int'>
>>> #WAS to print the address of the memory block in given value.
>>> a=10
>>> id(a)
140715878769736
SyntaxError: invalid syntax
#WAS to print your details, first store your details, extract the values and display it.
a='chandu
SyntaxError: incomplete input
a='chandu'
print(a)
chandu
#WAS to swap the two values. With a temp variable.
a=10
b=20
a=c
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a=c
NameError: name 'c' is not defined
c=a
b=a
b=c
a
10
b
10
a=10
b=20
c=b
b=a
c=a
a
10
b
10
a=c
a
10
a=10
b=20
c=b
b
20
c
20
b=a
b
10
c
20
a=c
a
20
b
10
#WAS to swap the two values without temp variable
a=10
>>> b=20
>>> a=a-b
>>> b=a+b
>>> a
-10
>>> b
10
>>> a=20b=10
SyntaxError: invalid decimal literal
>>> a=20
>>> b=10
>>> a=a-b
>>> b=a+b
>>> a
10
>>> b
20
>>> #WAS to initialize a value and print the value, after print then reinitialize the new value
>>> a=10
>>> a
10
>>> a=20
>>> a
20
>>> #WAS to convert single to multi value data type
... I/p ⇒ a=10
... o/p ⇒ [‘1’,’0’]
SyntaxError: invalid character '⇒' (U+21D2)
>>> #WAS to convert single to multi value data type
... #I/p ⇒ a=10
... #o/p ⇒ [‘1’,’0’]
>>> a='10'
>>> list(a)
['1', '0']
>>> #WAS to concat the two multi value data types(str , list, tuple, dict).
>>> a='str'
>>> a+='ing
SyntaxError: incomplete input
>>> a+='ing'
>>> a
'string'
>>> b=[10,20,30]
>>> b+=[40,50]
>>> b
[10, 20, 30, 40, 50]
>>> #In tuple we cant concat into tuple because it is a immutable data type
>>> c={'a':10,'b':20}
>>> c={'d':30}
>>> c
{'d': 30}
>>> c={'a':10,'b':20}
>>> c['d']=30
>>> c
{'a': 10, 'b': 20, 'd': 30}
>>> #WAC to perform the length of the collection.
>>> a=[10,20,30,40,50]
>>> len(a)
5
>>> #WAC to perform the length of the collection.
>>> a=[10,20,30,40,50]
b=(len(a)+1)/2
b
3.0
b[(len(a)+1)/2-1]
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    b[(len(a)+1)/2-1]
TypeError: 'float' object is not subscriptable
b[(len(a)+1)//2-1]
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    b[(len(a)+1)//2-1]
TypeError: 'float' object is not subscriptable
#WAS to concat the new string into the starting of the given string.
a='spiders'
a='py'+
SyntaxError: incomplete input
a='py'+a
a
'pyspiders'
#WAS to concat the new string into the ending of the given string.
a='py'
a=a+'spiders'
a
'pyspiders'
#WAS to concat the new string into the middle of the given string.
a='pyspers'
a=a[:3]+'id'+a[3:]
a
'pysidpers'
#WAS to replace the old character into a new character of the given string.
#we cant replace the character in the string because it is a immutable  data type
a='pyspiders'
a[0]='q'
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a[0]='q'
TypeError: 'str' object does not support item assignment
#WAS to delete the specific character in the given string.#we cant replace the character in the string because it is a immutable  data type
#we cant delete the character in the string because it is a immutable  data type
a='pyspiders'
del a[0]
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    del a[0]
TypeError: 'str' object doesn't support item deletion
#WAS to concat the new string into the specific position of the given string.
a='pyspers'
a=a[:3]+'id'+a[3:]
a
'pysidpers'
#WAS to concat the new value into the starting of the given list.
a=[10,20]
a=[30,40]+a
a
[30, 40, 10, 20]
#WAS to concat the new value into the ending of the given list.
a=[10,20]
a=a+[30,40]
a
[10, 20, 30, 40]
#WAS to concat the new value into the middle of the given list.
a=[10,20]
a[1]+=[50,60]
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    a[1]+=[50,60]
TypeError: unsupported operand type(s) for +=: 'int' and 'list'
a=[10,20]
a=a[:1]+[50,60,70]+a[1:]
a
[10, 50, 60, 70, 20]
#WAS to modify the new value into the specific position of the given list.
a=[10,20]
a[1]=300
a
[10, 300]
#WAS to modify the new value into the starting of the given list.
a=[10,20]
a[0]=200
a
[200, 20]
#WAS to modify the new value into the ending of the given list.
a=[10,20,50,60,70]
a[4]=50
a
[10, 20, 50, 60, 50]
#WAS to modify the new value into the middle of the given list.
a=[10,20,50,60,70]
a[2]=800
a
[10, 20, 800, 60, 70]
#WAS to modify the first 4 positions values into a given list.
a=[10,20,50,60,70]
a[:5:1]=[500,600,700,800]
a
[500, 600, 700, 800]
#WAS to delete the value in the specific position of the given list.
a=[10,20,50,60,70]
del a[0]
a
[20, 50, 60, 70]
#WAS to delete the new value into the ending of the list.
a=[10,20,50,60,70]
del a[4]
a
[10, 20, 50, 60]
#WAS to delete the new value into the middle of the list.
a=[10,20,50,60,70]
del a[2]
a
[10, 20, 60, 70]
#WAS to concat the new value into starting of the tuple.
#we cannot concat the new value into the tuple because it is a immutable data type
a=(10,20,30)
a=a+(40,50)
a
(10, 20, 30, 40, 50)
a=(10,20,30)
a=(40,50,60)+a
a
(40, 50, 60, 10, 20, 30)
a=(10,20,30)
a=a[:1]+(60,50)+a[1:]
a
(10, 60, 50, 20, 30)
#WAS to concat the new value into the set.
a={10,20,30}
a=a+{40,50}
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    a=a+{40,50}
TypeError: unsupported operand type(s) for +: 'set' and 'set'

#we cannot concat the new value into the set because it is a immutable data type and it doest support indexing value but we can perform only set operations
#
KeyboardInterrupt
#WAS to concat the new key and value into the dict.
a={'a':1,'c':2}
a['b']=3
a
{'a': 1, 'c': 2, 'b': 3}
#WAS to delete the specific key and value in the given dict.
a={'a':1,'c':2}
del a['c']
a
{'a': 1}
#WAS to delete the set value.
#we cannot del value into the set because it is a immutable data type and it doest support indexing value and it stores the value in random memory
a={10,20,30}
del a
a
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    a
NameError: name 'a' is not defined
#WAS to modify the specific value in the given dict.
a={'a':1,'c':2}
a['a]=100
  
SyntaxError: incomplete input
a['a']=100
  
a
  
{'a': 100, 'c': 2}
#WAS to concat the list value and tuple value by using type casting.
  
a=[10,20,30]
  
b=(100,200,300)
  
a=tuple(a)+b
  
a
  
(10, 20, 30, 100, 200, 300)
#WAS to concat the list value and tuple value without using type casting.
  
#WAC to the given number is divisible by 3.
  
a=9
  
a%3 is o
  
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    a%3 is o
NameError: name 'o' is not defined
a%3 is 0
  
True
a%3 is 0
  
True
a=7
  
a%3 is 0
  
False
#WAC to the given number is divisible by 2 and 6.
  
a=12
  
a%2 and a%6 is 0
  
0
a%2 and a%6 ==0
  
0
a%2 =0=a%6
  
SyntaxError: cannot assign to expression
a%2==0 and a%6==0
  
True
a=5
  
a%2==0 and a%6==0
  
False
#WAC to the given number, the last digit is divisible by 3.
  
a=[123]
  
#WAC to the given number, the last digit is divisible by 3.
  
a=123
  
list[a]
  
list[123]
a
  
123
a=123
  
str(a)
  
'123'
a
  
123
a=123
  
b=str(a)
  
b
  
'123'
int(b[2])%3==0
  
True
#WAC to the given number is greater than 150.
  
a=149
  
a>150
  
False
#WAC to the given number is greater than or equal to 100.
  
a=100
  
a>=100
  
True
#WAC to the given number is less than 150, print the result.
  
a=eval(input("enter the value")
       150
       
SyntaxError: incomplete input
a=eval(input("enter the value")
       aa
       
SyntaxError: incomplete input
a=150
       
a<150
       
False
#WAC to the given number is less than or equal to 100.
       
a=99
       
a<=100
       
True
#WAC to the given number is greater than 15 & less than 24
       
a=30
       
15>a<24
       
False
#WAC to the given number is even.
       
a=24
       
a%2==0
       
True
#WAC to the given number is odd.
       
a=24
       
not(a%2==0)
       
False
a='str'
       
a=a*6
       
a
       
'strstrstrstrstrstr'
#WAC to the given number is divisible by 3 and also the number should be greater than 22
       
a=27
       
a%3==0 and a>22
       
True
#WAC to perform the length of the collection is even or not.
       
a=[10,20,30]
       
len(a)%2==0
       
False
#WAC to perform the length of the collection is less than 55 and greater than 16.
       
a=[10,20,30,40,50]
       
16>a<55
       
Traceback (most recent call last):
  File "<pyshell#257>", line 1, in <module>
    16>a<55
TypeError: '>' not supported between instances of 'int' and 'list'
16>len(a)<55
       
True
#WAC to perform the length of the collection is divisible by 5 and odd.
       
a=[10,20,30,40,50]
       
len(a)%5==0 and not(len(a)%2==0)
       
True
#WAC to extract the middle position of a given collection.(str, lis, tuple)
       
a=[10,20,30,60,70]
       
n=int(len(a))
       
p=(n-1)/2
       
p
       
2.0
#WAC to the given number is greater than 20 and less than 30 and it should be even.
       
a=30
       
20>a<30 and a%2==0
       
False
#WAC to the given number is even and it should be less than 120.
       
a=100
       
a<120 and a%2==0
       
True
#WAC to the given number is even and it should be less than 120.
       
#WAC to the given number is even and present from 40 to 70
       
a=50
       
40<a<70 and a%2==0
       
True
#WAC to the given number is odd and it should be greater than 97.
       
a=101
       
a>97 and not(a%2==0)
       
True
#WAC to the given number is less than 122 and greater than 48 and the numbershould be divisible by 4.
       
a=124
       
48>a<122 and a%4==0
       
False
#WAC to the given number is divisible by 3 or 5, displaying the value.
       
a=15
       
a%3==0 and a%5==0
       
True
a%3 and a%5
       
0
a/3 and a/5
       
3.0
#WAC to the given number is between 100 to 200 including the limit.
       
a=102
       
100<a<200
       
True
a=102
       
100<=a<=200
       
True
#WAC to the given number is present between 60 to 130 and the number should be divisible by 3 and 4 and the last digit should be greater than 9.
       
a=134
       
60<a<130 and a%3==0 and a%4==0
       
False
60<a<130 and a%3==0 and a%4==0
       
False
b=str(a)
       
int(b[2])%9==0
       
False
#WAC to the given number is even or less than 25.
       
a=24
       
a%2==0 and a<24
       
False
a%2==0 and a<25
       
True
#WAC to the given number is even or greater than 25.
       
a=24
       
a%2==0 and a>25
       
False
#WAC to the given number is divisible by either 3 or 5.
       
a=24
       
a%3==0 or a%5==0
       
True
#WAC to the given number is not an even number.
       
a=2
       
not(a%2==0)
       
False
#WAC to the given number is not a odd number
       
a=2
       
(a%2==0)
       
True
#WAC to the given number is not a divisible by 3
       
a=44
       
not(a%3==0)
       
True
#WAC to the given number is not a divisible by 3 and 5
       
a=44
       
not(a%3==0) and not(a%5==0)
       
True
#WAC to the given character is uppercase or not.
       
a='A'
       
'A'<a<Z
       
False
'A'<a<'Z'
       
False
'A'<=a<='Z'
       
True
a='b'
       
not(0<a<9)
       
Traceback (most recent call last):
  File "<pyshell#327>", line 1, in <module>
    not(0<a<9)
TypeError: '<' not supported between instances of 'int' and 'str'
'A'<=a<='Z' and 'a'<=a<='z'
       
False
#WAC to find out the ascii character in a given number.
       
ch='a'
       
0<ch<9
       
Traceback (most recent call last):
  File "<pyshell#331>", line 1, in <module>
    0<ch<9
TypeError: '<' not supported between instances of 'int' and 'str'
'0'<ch<'9'
       
False
#WAC to the given character is lowercase.
       
c='a'
       
'a'<=c'z'
       
SyntaxError: invalid syntax
'a'<=c<='z'
       
True
#WAC to the given character is the special character.
       
c='a'
       
not('A'<=c<='Z' or 'a'<=c<='z' or '0'<=c<='9')
       
False
#WAC to the given character should not be uppercase.
       
c='z'
       
not('a'<=c<='z')
       
False
#WAC to the given character should not be lowercase.
       
c='Z'
       
not('A'<=c<='Z')
       
False
#WAC to the given character should not be the alphabet.
       
a='1'
       
not('A'<=c<='Z' or 'a'<=c<='z' )
       
False
#WAC to the given character should not be an ascii number.
       
a=' '
       
not(' '0'<=c<='9')
    
SyntaxError: unterminated string literal (detected at line 1)
not('0'<=a<='9')
    
True
#WAC to the given character is the special character.
    
a=' '
    
not('A'<=a<='Z' or 'a'<=a<='z' or '0'<a<'9')
    
True
#WAC to the given character is a vowel.
    
a='e'
    
a in 'AEIOUaeiou'
    
True
#WAC to the given character is a consonant.
    
a='e'
    
a not in 'AEIOUaeiou
    
SyntaxError: incomplete input
a not in 'AEIOUaeiou'
    
False
#WAC to check if the first and second characters are sequence or not in a given string.
    
a='pyspiders'
    
'py' in a
    
True
#WAC to the given number is increased by 1.
    
a=10
    
a+True
    
11
#WAC to the given number is increased by 2.
    
a=10
    
a+2
    
12
#WAC to the given number is decreased by 1.
    
a=10
    
a-True
    
9
#WAC to the given number is decreased by 3.
    
a=10
    
a-3
    
7
#WAC to the given integer number is present in the collection.
    
a=10
    
a=[10,20,30,40]
    
10 in a
    
True
#WAC to perform the addition operation on A value and B value and final result should be updated to A.
    
a=10
    
b=20
    
a=a+b
    
a
    
30
#WAC to the given list is present in the list.
    
a=[10,20,30,[200,300]]
    
[10,20,30] in a
    
False
#WAC to the given dict value is present in tuple.
    
a={'a':10,'c':20}
    
b=(10,20,30,40)
    
a['a'] in b
    
True
#WAC to the check given value is integer value or not.
    
a=10
    
a is int
    
False
a is type(int())
    
False
a is type(int)
    
False
a=10
    
a is type(int)
    
False
type(a) is type(int)
    
False
type(a) in type(int)
    
Traceback (most recent call last):
  File "<pyshell#402>", line 1, in <module>
    type(a) in type(int)
TypeError: argument of type 'type' is not iterable
type(a) in [int]
    
True
#WAC to the check given value is string value or not.
    
a=10
    
type(a) in [str]
    
False
#WAC to the check given value is single value or not.
    
a=100
    
len(a)
    
Traceback (most recent call last):
  File "<pyshell#409>", line 1, in <module>
    len(a)
TypeError: object of type 'int' has no len()
len(str(a))
    
3
len(str(a))==1
    
False
#WAC to the check given value should not be a single value.
    
a=100
    
not(len(str(a))==1)
    
True
#WAC to the check given value is multi value or not.
    
a=10
    
type(a)in [bytes,str]
    
False
#WAC to the check given value is a mutable value or not.
    
a=10
    
type(a)not in [int,bytes,complex,bool, str]
    
False
#WAC to the check given value is an immutable value or not.
    
a=10
    
type(a) in [int,bytes,complex,bool, str]
    
True
#WAC to the check given value should be an immutable value.
    
a=10
    
type(a) in [int,bytes,complex,bool, str]
    
True
#WAC to check if a given value is divisible by 6 as well as that value present in the collection or not.
    
a=60
    
b=[10,50,20,30,60]
    
a%6==0 and a in b
    
True
#WAC to perform the bitwise and operation given values are 15 and 19.
    
a=15
    
b=19
    
a &b
    
3
#WAC to perform the bitwise or operation given values are 115 and 79.
    
115|79
    
127
#WAC to perform the bitwise xor operation given values are 56 and 22.
    
56^22
    
46
#WAC to perform the bitwise xor operation given values are 56 and 22.
    
a=25
    
#WAC to perform the bitwise not operation given values are 15.
    
a=25
    
a~15
    
SyntaxError: invalid syntax
~15
    
-16
#WAC to perform the bitwise left shift with 32 and skipping value is 3.
    
3<<3
    
24
32<<3
    
256
#WAC to perform the bitwise right shift with 25 and skipping value is 2.
    
25>>2
    
6
#To find out the output of a given condition.
    
(10+20*60 and 10**3) or ({10,20} or not ([15-16]))
    
1000
#WAC to check if the first and last characters are the same or not in the given list.
    
a='pyspiders'
    
a[0]=a[8]
    
Traceback (most recent call last):
  File "<pyshell#454>", line 1, in <module>
    a[0]=a[8]
TypeError: 'str' object does not support item assignment
a[0]==a[8]
    
False
#WAC to check if a given key is present in a dict.
    
a={'p':10,'o':52,'r':20}
    
a[p] in a
    
Traceback (most recent call last):
  File "<pyshell#458>", line 1, in <module>
    a[p] in a
KeyError: 2.0
a['p'] in a
    
False
'p' in a
    
True
#WAC to check if value is present in the dict.
    
a={'p':10,'o':52,'r':20}
    
20 in a
    
False
#in dict values are stored in value layers but the value layer is invisible layers so we can extract or any identification can done by using keys
    
#WAC to check if the key is not present in a dict.
    
a={'p':10,'o':52,'r':20}
    
'a' in a
    
False
#WAC to check if two values are pointing to the same address or not
    
a=10
    
b=20
    
a is b
    
False
a=10
    
b=10
    
a is b
    
True
#
    
#WAC to check both the values should be integer and both the values are pointing to the same address.
    
a=10
    
b=10
    
type(a) and type(b) in [int] and a is b
    
True
