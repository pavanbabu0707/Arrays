# Return the index of the target value

arr = [4, 2, 7, 1]

def tar_val(arr):
    n = len(arr)
    target = 7

    for i in range(n):
        if arr[i] == target:
            return i
       
    return [-1]
    
print(tar_val(arr))
    


