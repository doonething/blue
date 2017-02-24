'''
Created on 2017. 2. 24.

@author: bi
'''
import unittest
import threading
from slow import xor_test
from model.net import Net


class Test(unittest.TestCase):

    def test_multi_graph_xor (self):
        g1 = Net()
        g2 = Net()
        xor_test.make_net(g1)
        xor_test.make_net(g2)
        g1_loss = g1.run(g1.loss)
        g2_loss = g2.run(g2.loss)
        g1.fit()
        g1_loss_fit = g1.run(g1.loss)
        g2_loss_fit = g2.run(g2.loss)
        self.assertGreater(g1_loss, g1_loss_fit)
        self.assertEqual(g2_loss, g2_loss_fit)
        
    def test_run_in_two_thread(self):
        g1 = Net()
        g2 = Net()
        xor_test.make_net ( g1)
        xor_test.make_net ( g2)
        
        g1_loss = g1.run(g1.loss)
        g2_loss = g2.run(g2.loss)
        
        def r1(): g1.fit()
        def r2(): g2.fit()
        t1 = threading.Thread(target=r1)
        t2 = threading.Thread(target=r2)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        
        g1_loss_fit = g1.run(g1.loss)
        g2_loss_fit = g2.run(g2.loss)
        self.assertGreater(g1_loss, g1_loss_fit)
        self.assertGreater(g2_loss, g2_loss_fit)
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()