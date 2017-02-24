'''
Created on 2017. 2. 24.

@author: bi
'''
import unittest
from model.net import Net


class XorTest(unittest.TestCase):

    def setUp(self):
        self.mock = Net()

    def tearDown(self):
        self.mock.close()

    def test_xor(self):
        make_net(self.mock)
        mock = self.mock
        first_loss = mock.run(mock.loss)
        mock.fit()
        trained_loss = mock.run(mock.loss)
        self.assertTrue( first_loss > trained_loss)
        self.assertGreater(first_loss,   trained_loss)
        self.assertTrue( .005 > trained_loss, msg= 'trained_loss=%3.5f'%trained_loss)
        
def make_net(mock):
    mock.add_layer(2);
    mock.add_layer(2);
    mock.add_layer(1);
    mock.loop_cnt = 5000
    input = [ [0,0], [0,1], [1,0], [1,1]]
    target= [ [0], [1], [1], [0]]
    mock.init(input, target, save_dir= 'save/xor')
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()