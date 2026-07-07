num = int(input("Enter a number: "))

root = int(num ** 0.5)

if root * root == num:
    print("Perfect Square")
else:
    print("Not a Perfect Square")
