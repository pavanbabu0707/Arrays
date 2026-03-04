# Return he count of even numbers in the given array

arr = [1, 2, 3, 4, 6]

def count_even_num(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        if arr[i] % 2 == 0:
            count += 1
    return count

print(count_even_num(arr))