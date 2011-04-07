'''
Created on Apr 6, 2011

@author: aaron
'''

def solve():
    res = 0
    for i in range(0,1000):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res

if __name__ == '__main__':
    print(solve())
        