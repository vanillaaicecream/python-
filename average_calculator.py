n = int(input("How many numbers? "))

total = 0

for i in range(n):
    num = float(input("Enter number: "))
    total += num

print("Average:", total / n)
