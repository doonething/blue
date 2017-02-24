'''
Created on 2017. 2. 24.

@author: bi
'''
import unittest
from model.net import Net

import tensorflow as tf

class MnistTest(unittest.TestCase):

    def setUp(self):
        self.mock = Net()
    
    def tearDown(self):
        self.mock.close()
            
    def test_mnist(self):
        mock = self.mock #= Deco()
        make_net(mock)
        test(mock, self)

def make_net( mock):
    width = 28
    height = width
    input_channel_size  = 1
    output_channel_size = 7
    filter_size = 5
    mock.add_conv2d(filter_size, output_channel_size, width,height, input_channel_size)
    mock.add_pool()
    mock.add_conv2d(filter_size, output_channel_size)
    mock.add_pool()
    mock.add_layer(1024, stddev=.01)
    mock.add_layer(10, act_func= tf.nn.softmax, stddev=.01)
        
def test(mock, tester):
    mnist = get_mnist()
    b = mnist.train.next_batch(100)
    mock.init(b[0], b[1], 'save/mnist')
    
    mock.is_check_loss_threshold = True
    mock.loss_threshold = .285
    mock.fit()
    tester.assertGreater(mock.get_acc(), .94)
    
    b = mnist.test.next_batch(200)
    out = mock.eval(b[0])
    tester.assertGreater(mock.get_acc(out, b[1]), .65)

from tensorflow.examples.tutorials.mnist import input_data

def get_mnist():
    return input_data.read_data_sets("data/", one_hot=True)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()