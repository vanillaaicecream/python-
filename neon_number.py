num = int(input("Enter a number: "))

square = num * num
total = 0

while square > 0:
    total += square % 10
    square //= 10

if total == num:
    print("Neon Number")
else:
    print("Not a Neon Number")