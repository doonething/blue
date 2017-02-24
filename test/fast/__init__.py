import unittest as u

import conv_test
import model_test

tests = u.TestSuite()

tests.addTest( u.makeSuite(conv_test.Test) )
tests.addTest( u.makeSuite(model_test.Test) )