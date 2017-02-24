import unittest as u

import xor_test, mnist_test
import multi_graph_test


# creating a new test suite
tests = u.TestSuite()

# suite.addTest(u.makeSuite(xor_test.XorTest))

tests.addTest( u.makeSuite(xor_test.XorTest) )
tests.addTest( u.makeSuite(mnist_test.MnistTest) )
tests.addTest( u.makeSuite(multi_graph_test.Test) )
