# Sum of all elements in an array

arr = [1, 2, 3, 4, 5]

def sum_array(arr):
    n = len(arr)
    total = 0

    for i in range(n):
        total += arr[i]
    return total

print(sum_array(arr))
