'''
Created on Apr 6, 2011

@author: aaron
'''

import inspect
import src


def print_classes():
    for name, obj in inspect.getmembers(src):
        if inspect.ismodule(obj) and name != 'os' and name != 'driver':
            if 'solve' in obj.__dict__:
                solver = obj.__dict__['solve']
                print(name, ': ', solver())

if __name__ == '__main__':
    print_classes()
    
