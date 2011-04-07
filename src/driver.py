'''
Created on Apr 6, 2011

@author: aaron
'''

import inspect
import src


def run_solvers():
    for name, obj in inspect.getmembers(src):
        if inspect.ismodule(obj) and name != 'os' and name != 'driver':
            if 'solve' in obj.__dict__:
                solver = obj.__dict__['solve']
                print(name, ': ', solver.__doc__, "\nanswer: ", solver(), "\n\n", ''.join(['*'] * 50), "\n")

if __name__ == '__main__':
    run_solvers()
    
