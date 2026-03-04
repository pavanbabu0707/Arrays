# Return the occurences of a number in an array

arr = [1, 2, 3, 2, 2, 4]

def count_occur(arr, x):
    n = len(arr)
    count = 0

    for i in range(n):
        if arr[i] == x:
            count += 1

    return count

print(count_occur(arr, 2))