n = int(input("Enter the limit: "))

total = 0

for i in range(2, n + 1, 2):
    total += i

print("Sum of Even Numbers:", total)
