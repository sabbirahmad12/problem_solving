""" Even Or Odd Number Ber korar program"""
n = int(input("Enter Number: ").strip())
print("Even" if n % 2 == 0 else "Odd")

""" Positive or Negetive and Zero Number ber korar Program"""
n = int(input("Enter Number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negetive")
else:
    print("Zero")

""" 3ti Number er vitore Large Number Ber Korar Program"""
a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
c = float(input("Enter Third Number: "))

if (a > b) and (a > c):
    print("A is Big")
elif b > c :
    print("B is Big")
else:
    print("C is big")

""" 3ti Number er vitore Small Number Ber Korar Program"""
a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
c = float(input("Enter Third Number: "))

if (a < b) and (a < c):
    print("A is small")
elif b < c :
    print("B is Small")
else:
    print("C is small")


#-----------------------------------------

"""Pattern Programme"""

n = int(input("Enter the Number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)


n = 4
for i in range(1, n+1):
    print('*' * i)

n = 5
for i in range(n, 0, -1):
    print('*' * i)


n = 5    #int(input("Enter Number: "))

for i in range(1, n + 1):
    for j in range(1, i+1):
        print(j, end="")
    print()

    # Output:
            # 1
            # 12
            # 123
            # 1234


for i in range (1, n+1):
    print(str(i)*i)

    # output:
    #         1
    #         22
    #         333
    #         4444
    #         55555


for i in range (1, n+1):
    print(" " * (i - 1) + "*" * i)

    # output:
    #         *
    #          **
    #           ***
    #            ****
    #             *****

#---------------------------------

# """ Palindrome Number Ber Korar Program"""
n = int(input("Enter a number: "))

if n == n[::-1]:
    print(f"{n} is a Palindrome")
else:
    print(f"{n} is not a palindrome")

# """ Armstrong Number Ber Korar Program"""
temp = n
digits = len(str(n))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")

# """ Factors of a /বিভাজক Number Ber Korar Program"""
for i in range(1, n + 1):
    if n % i == 0:
        print("the result is: "+ str(i))

#---------------------------------

n = int(input("Enter a Number: "))

# """ Prime Number Ber Korar Program"""
if n < 2:
    print("it is not Prime Number")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime =False
            break
    print("Prime" if is_prime else "Not Prime")


# """ First N Prime Numbers Ber Korar Program"""
primes = []
number = 2

while len(primes) < n:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
        
    if is_prime:
        primes.append(number)
    
    number += 1
print(primes)


# """ Fibonacci Series Ber Korar Program"""
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a+b


# """ Nth Fibonacci Number Ber Korar Program"""
if n <= 0:
    print('Invalid input! Please enter a positive integer.')
elif n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a+b
    print(b)


# """ Area of Triangle Ber Korar Program"""
base  = float(input("Enter base: "))
height  = float(input("Enter height: "))

area = 0.5 * base * height
print("area of traiangle is:", area)
#----------- / ----------------------
import math
def triangle_area(a, b, c):
    if (a+b)>c and (b+c)>a and (c+a)>b:
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("Area of triangle is:", area)
    else:
        print("Triangle is not possible")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

tarea = triangle_area(a, b, c)


# """ Area of Circle Ber Korar Program"""
r = float(input("Enter a Number: "))

pi = 3.1416
area = pi *(r**2) #--- pi * r squared
print("Area of Circle is:", area)


# """ Area of Rectangle Ber Korar Program"""
lenght = float(input("Enter lenght: "))
width = float(input("Enter width: "))

area = lenght * width
print("Area of Rectangle is:", area)


# """ Remove Duplicates from a List Ber Korar Program"""

my_List = [1,2,2,3,4,5,5,5,6,7,7,8,9,9,0]

# n = input("Enter number of elements in the list: ")
# my_list = [int(x.strip()) for x in n.split(",")]

unique_list = []
seen = set()
for item in my_list:
    if item not in seen:
        unique_list.append(item)
        seen.add(item)
print("Unique List is:", unique_list)

#------------------------------------


