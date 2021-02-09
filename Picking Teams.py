def solve(m, n):
    arr = [i for i in range(m)]
    new_arr = []
    i = -1
    
    count = 0
    
    while True:
        i += 1
        if i == m:
            i = -1
            continue
        
        if arr[i] != 'F':
            count += 1
        
        if count == n:
            new_arr.append(arr[i])
            arr[i] = 'F'
            count = 0
        
        if m - arr.count('F') < n:
            break
    
    idx = new_arr[-1]
    
    for i in range(idx, m):
        if arr[i] != 'F':
            new_arr.append(arr[i])
            arr[i] = 'F'
    
    for i in range(m):
        if arr[i] != 'F':
            new_arr.append(arr[i])
            arr[i] = 'F'

    return new_arr

print("10, 3", solve(10,3))
print("10, 4", solve(10,4))
print("5, 2", solve(5,2))
