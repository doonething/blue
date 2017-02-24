'''
Created on 2017. 2. 24.

@author: bi
'''
import unittest
import numpy as np
import tensorflow as tf
from model.net import Net


class Test(unittest.TestCase):

    def setUp(self):
        self.mock = Net()

    def tearDown(self):
        self.mock.close()

    def test_add_layer(self):
        mock = self.mock
        mock.add_layer(3)
        
    def test_add_layer_shape(self):
        mock = self.mock
        mock.add_layer( shape= [None,12*12, 5])
    
    def test_for_features_net(self):
        mock = self.mock
        width = 12
        size  = 3
        mock.add_layer(shape=[None, width*width* size])
        mock.add_layer(100)
        mock.add_layer(width * width)
        
    def test_reshape(self):
        width = 12
        size  = 40
        features = np.random.rand(width, width, size)
        features = features.reshape ( [ width*width * size])
        
    def test_tf_reduce_mean_of_boolean_list (self):
        x = [True, True, True, False]
        try :
            with tf.Session() as s :
                acc = tf.reduce_mean ( tf.cast(x, tf.float32 ) )
                self.assertEquals (.75, s.run(acc))
        finally :
            s.close()
    
    def test_acc(self):
        out    = np.zeros([ 5, 3 ])
        target = np.zeros([ 5, 3 ])
        out    [:5,0] = 1
        target [:4,0] = 1
        target [4,1] = 1
        try :
            with tf.Session() as s :
                acc = self.mock.get_acc(out, target) 
                self.assertAlmostEquals ( .8, acc  )
        finally : s.close()
