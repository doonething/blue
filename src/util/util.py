'''
Created on 2017. 2. 23.

@author: bi
'''
import sys

def printr ( s):
    sys.stdout.write("%s\r" % (s) )
    sys.stdout.flush()