numbers = [1, 2, 3, 5, 6]

n = len(numbers) + 1

expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)

print("Missing Number:", expected_sum - actual_sum)