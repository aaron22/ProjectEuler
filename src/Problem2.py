'''
Created on Apr 6, 2011

@author: aaron
'''

import general_utilities

def solve():
    total = 0
    for i, val in enumerate(general_utilities.naive_fibonacci()):
        if val > 4000000:
            break;
        # every 3rd term in the sequence is even, so only count those
        if (i+1) % 3 == 0:
            total += val
    return total
        
if __name__ == '__main__':
    print(solve())