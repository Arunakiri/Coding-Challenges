'''
A thief trying to escape from a jail. He has to cross N walls each with varying heights (every height is greater than 0). 
He climbs X feet every time. But, due to the slippery nature of those walls, every time he slips back by Y feet. 
Now the task is to calculate the total number of jumps required to cross all walls and escape from the jail.
'''

def jumps(x,y,walls):
    count = 0
    for i in walls:
        temp = i
        if temp <= x:
            count += 1
            continue
        else:
            while temp > 0:
                temp -= (x-y)
                count += 1
    return count 

x = 10
y = 1
# walls = [ 11, 10, 10, 9 ] 
# walls = [11, 34, 27, 9]
# walls = [11, 11]
walls = [50]
print(jumps(x,y,walls))
