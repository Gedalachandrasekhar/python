#WAP to check whether a number is positive. If Positive, print a message Positive.
a=1
if a>0: print('positive')

positive
#WAP to display hello world if the number is greater than 1 and lesser than 5
a=4
if 1<a<5:
    print('helloworld')

    
helloworld
#WAP to check whether the given number is divisible by 3 or not if print fizz
a=99
if a%3==0:
    print('fizz')
    
    
fizz
#WAP to check whether given input is divisible by 2 and 6. If the condition is satisfied,convert the given number into a complex number
a=12
if a%2==0 and a%6==0:
    print(complex(a))

    
(12+0j)
# WAP to check whether a given input is divisible by 3 or 5. If the condition is satisfied,the number is converted to a list.
a=30
if a%3==0 and a%5==0:
    print(list(str(a)))

    
['3', '0']
#Write a program to check whether a given number is multiple of 5 or not
a=25
a%5==0
True
#WAP to check whether the given input is 0 or not if 0 prints 0
a=0
if a==0:
    print("0")

    
0
#WAP to check whether a number is negative. If negative, print a message negative
a=-1
if a<0: print('negative')

negative
#WAP to check whether a number is even or not. If even, store the value inside the list.
a=44
b=[10,20,30]
if a%2==0:
    b=b+[a]

    
b
[10, 20, 30, 44]
#WAP to check whether a number is odd or not. If odd, store the value inside the tuple.
a=45
b=(10,25,35)
if a%2!=0:
    b=b+(a,)
    print(b)

    
(10, 25, 35, 45)

#WAP to check whether a given value is divisible by 5 and 7. If the value is divisible, todisplay the square of the values
a=35
if a%5==0 and a%7==0:
    print(a**2)

    
1225
#WAP to check whether the given value's last digit is greater than 5 or not. If greater, toperform the bitwise right shift operator (skipping value is 2
a=156
b=str(a)
c=int(b[2])
if c>5:
    print(a>>2)

    
39
#WAP to check whether a given value is divisible by 3 and less than 30. If the value isdivisible, to display the square of the values
a=24
if a%3==0 and a<30:
    print(a**2)

    
576
#WAP to check whether a given value is an even number and divisible by 4. If satisfied,to display the cube of the values.
a=44
if a%2==0 and a%4==0:
    print(a**3)

    
85184

#WAP to check whether given value is even value or not. If the even number stores thevalue inside the list.
a=44
b=[10,20,30]
if a%2==0:
    b=b+[a]

    
b
[10, 20, 30, 44]
#WAP to check whether a given value is a negative or even number. If satisfied ,todisplay the last digit of the values.
a=-44
str(a)
'-44'
a=-44
if a<0 and a%2==0:
    b=str(a)
    print(b[2])

    
4
# WAP to check whether a given value is a negative or odd number and divisible by 4.If satisfied ,to display the cube of the values.
a=24
a=-24
if a<0 or a%2!=0 and a%4==0:
    print(a**3)

    
-13824
#WAP to check whether a given ascii value is divisible by 4 and even value. If satisfied,to display the ascii character
a='@'
b=ord(a)
if b%4==0 and b%2==0:
    print(b)

    
64
#WAP to check whether a given value is present in between 45 to 125 and the numbershould be divisible by 4 and 5 and even value. If satisfied ,to display the ascii character.
a=120
if 45<a<125 and a%4==0 and a%5==0 and a%2==0:
    print(chr(a))

    
x
#WAP to check whether a given value is present in between 25 to 100 and the numbershould be divisible by 4 and 5. If satisfied, to display multiplication of given value with5
a=80
if 25<a<100 and a%4==0 and a%5==0:
    print(a*5)

    
400

#WAP to check whether a given number is an integer and odd number. If the conditionis satisfied, the integer is divisible by 5 and displays the result.
a=25
if a%2!=0 and a>0:
    print(a%5==0)

    
True
#WAP to check whether a given value is an integer or not. If integer, the given value isconverted to string and displays the result.
a=25
if  a>0:
    str(a)

    
'25'
#WAP to check whether a given value is less than 125 and greater than 60 or not. If thecondition is satisfied, take the name and extract the middle character and display it.
a='chandu'
b=100
if 60<b<125:
 print(a[len(a)//2])

 
n
#WAP to check whether a given two integers are equal or not. If both are equal, toperform addition and display the result.


a=10
b=10
if a==b:
    a+b

    
20
#WAP to check whether two values are equal or not if equal to perform multiplicationand division by 3 and display the value.
a=30
b=30
if a==b:
    a*3
    a//3

    
90
10
#WAP to check whether a character is in the alphabet or not. If the alphabet, store thevalue inside the dictionary(key as a character and value as an ascii value).
