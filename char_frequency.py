text = input("Enter a string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for key, value in frequency.items():
    print(key, ":", value)
