import math

def calculate_stats(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = math.sqrt(variance)
    return mean, variance, std_dev

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
mean, variance, std_dev = calculate_stats(numbers)
print(f"Mean: {mean}, Variance: {variance}, Standard Deviation: {std_dev}")
