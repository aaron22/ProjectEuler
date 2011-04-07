'''
Created on Apr 6, 2011

@author: aaron
'''

def naive_fibonacci():
    a, b = 0, 1
    while(True):
        a, b = b, a + b
        yield a