num = int(input("Enter a number: "))

power = len(str(num))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
