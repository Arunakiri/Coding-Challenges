'''
A group of children are picking teams for a game of soccer.
The way they pick teams is to line up all the players and select one person at a time from that line.
Starting from the first player in line, the person to be selected will always be "X" people down the line from the last player picked.
When the end of the line is reached, counting resumes from the start of the line.

Write a program that will return a list of players in the order they get selected to play.

Input:
Your program should read a single line from standard input.
That line will contain two comma-separated positive integers X and Z, where X is how many people to count when selecting the next player and Z is the number of people in line.

Output:
Print out the index of all the players (0 to Z-1, space delimited) in the order they will be selected.

Test Input
10,3
Expected Output
2 5 8 1 6 0 7 4 9 3
'''

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
