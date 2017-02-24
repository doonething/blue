'''
Created on 2017. 2. 24.

@author: bi
'''

import unittest as u

import slow 
import fast

suite = u.TestSuite()
 
suite.addTests(slow.tests)
suite.addTests(fast.tests)

def do_test():
    u.TextTestRunner().run(suite)