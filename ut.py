arr = [10, 5, 8, 15, 3]
max_value = arr[0]
max_index = 0

for i in range(1, len(arr)):
    if arr[i] > max_value:
        max_value = arr[i]
        max_index = i

print(f"Maximum value {max_value} found at index {max_index}")
