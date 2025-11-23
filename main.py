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
