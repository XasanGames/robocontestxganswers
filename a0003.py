numbers = list(map(int, input().split()))

total_sum = sum(numbers)
min_val = min(numbers)
max_val = max(numbers)
min_sum = total_sum - max_val
max_sum = total_sum - min_val

print(min_sum, max_sum)