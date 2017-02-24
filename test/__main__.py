'''
Created on 2017. 2. 24.

@author: bi
'''

import sys

import all

if '__main__' == __name__ :
    argv = sys.argv
    if argv.__len__() > 1 :
        try :
            loop = int ( argv[1] )
            for _ in range(loop) :
                all.do_test()
        except ValueError : pass
    else : all.do_test()
