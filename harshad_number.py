num = int(input("Enter a number: "))

temp = num
digit_sum = 0

while temp > 0:
    digit_sum += temp % 10
    temp //= 10

if num % digit_sum == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")