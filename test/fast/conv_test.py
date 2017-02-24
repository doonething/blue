'''
Created on 2017. 2. 24.

@author: bi
'''

import unittest as ut
from model.net import Net

class Test(ut.TestCase):
    
    def setUp(self):
        ut.TestCase.setUp(self)
        self.mock = Net()
    
    def tearDown(self):
        ut.TestCase.tearDown(self)
        self.mock.close()
    
    # width == height
    def test_add_conv2d_square(self):
        mock = self.mock
        width = 10
        height = width
        input_channel_size = 3
        # 10 * 10 * 3 
        # width = 10 = height 
        # input channel size = 3
        mock.add_layer ( width  * height * input_channel_size )
        
        filter_size = 5
        output_channel_size = 64
        mock.add_conv2d(filter_size, output_channel_size, width,height, input_channel_size)
        
    def test_make_auto_normal_layer(self):
        mock = self.mock
        width = 28
        height = width
        input_channel_size = 5
        output_channel_size = 7
        filter_size = 5
        mock.add_conv2d(filter_size, output_channel_size, width,height, input_channel_size)
        self.assertEquals ( [None,width*height*input_channel_size]
                            , mock.layers[0].get_shape().as_list())
    
        
    def test_add_conv2d_on_conv2d (self):
        mock = self.mock
        width = 28
        height = width
        input_channel_size = 5
        output_channel_size = 7
        filter_size = 5
        mock.add_conv2d(filter_size, output_channel_size, width,height, input_channel_size)
        mock.add_conv2d(filter_size, output_channel_size)
        mock.add_layer(5)
    
    def test_pool(self):
        mock = self.mock
        width = 28
        height = width
        input_channel_size = 5
        output_channel_size = 7
        filter_size = 5
        mock.add_conv2d(filter_size, output_channel_size, width,height, input_channel_size)
        mock.add_pool()
        mock.add_conv2d(filter_size, output_channel_size)
        mock.add_pool()
        mock.add_layer(7)
        
    def test_get_width_height_for_convolution_layer(self):
        mock = self.mock
        width = 28
        height = width
        input_channel_size = 5
        output_channel_size = 7
        filter_size = 5
        mock.add_conv2d(filter_size, output_channel_size, width,height, input_channel_size)
        width_, height_, output_channel_size_ = mock.get_width_height_input_channel_size()
        self.assertEquals(  [width , height , output_channel_size]
                          , [width_, height_, output_channel_size_])
    
        
    def test_add_second_conv2d_layer_without_width_height_input_channel_size(self):
        mock = self.mock
        width = 28
        height = width
        input_channel_size = 5
        output_channel_size = 7
        filter_size = 5
        mock.add_conv2d(filter_size, output_channel_size, width,height, input_channel_size)
        mock.add_conv2d( filter_size, output_channel_size )
