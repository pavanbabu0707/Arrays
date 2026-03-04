# Return the largest number in an array

arr = [10, 5, 8, 20, 3]

def largest_num(arr):
    n = len(arr)
    largest = arr[0]

    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]

    return largest

        
print(largest_num(arr))