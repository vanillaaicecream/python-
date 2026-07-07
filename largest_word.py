sentence = input("Enter a sentence: ")

words = sentence.split()

largest = max(words, key=len)

print("Largest Word:", largest)
