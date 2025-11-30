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

