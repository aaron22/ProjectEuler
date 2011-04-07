'''
Created on Apr 6, 2011

@author: aaron
'''

def solve():
    '''
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    '''
    num = 600851475143
    # take care of 2; it's a special case
    while (num % 2 == 0):
        num /= 2
        
    for i in range(3,600851475143,2):
        while (num % i == 0):
            num /= i
        if num == 1:
            return i
        
if __name__ == '__main__':
    print(solve())