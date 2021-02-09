def check(string):
    stack = []
    for i in string:
        if i in open_:
            stack.append(i)
        elif i in close_:
            idx = close_.index(i)
            if len(stack) > 0 and open_[idx] == stack[len(stack)-1]:
                stack.pop()
            else:
                return 'Unbalanced'
    if stack == []:
        return 'Balanced'
    else:
        return 'Unbalanced'
    


open_ = ['[','(','{']
close_ = [']',')','}']

string = input()
# '{[]{()}}' '{[]{()}}}' '[{}{})(]'

print(check(string))
