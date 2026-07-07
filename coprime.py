a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b

while y:
    x, y = y, x % y

if x == 1:
    print("Coprime")
else:
    print("Not Coprime")
