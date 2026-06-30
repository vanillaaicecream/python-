text = input("Enter text: ").lower().replace(" ", "")
print("Palindrome" if text == text[::-1] else "Not a palindrome")
