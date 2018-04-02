"""
Simple examples of convolution to do some basic filters
Also demonstrates the use of TensorFlow data readers.

We will use some popular filters for our image.
It seems to be working with grayscale images, but not with rgb images.
It's probably because I didn't choose the right kernels for rgb images.

kernels for rgb images have dimensions 3 x 3 x 3 x 3
kernels for grayscale images have dimensions 3 x 3 x 1 x 1

"""


import sys
sys.path.append('..')

from matplotlib import gridspec as gridspec
from matplotlib import pyplot as plt
import tensorflow as tf

import kernels

def read_one_image(filename):
    ''' This method is to show how to read image from a file into a tensor.
    The output is a tensor object.
    '''
    image_string = tf.read_file(filename)
    image_decoded = tf.image.decode_image(image_string)
    image = tf.cast(image_decoded, tf.float32) / 256.0
    return image

def convolve(image, kernels, rgb=True, strides=[1, 3, 3, 1], padding='SAME'):
    images = [image[0]]
    for i, kernel in enumerate(kernels):
        filtered_image = tf.nn.conv2d(image, 
                                      kernel, 
                                      strides=strides,
                                      padding=padding)[0]
        if i == 2:
            filtered_image = tf.minimum(tf.nn.relu(filtered_image), 255)
        images.append(filtered_image)
    return images

def show_images(images, rgb=True):
    gs = gridspec.GridSpec(1, len(images))
    for i, image in enumerate(images):
        plt.subplot(gs[0, i])
        if rgb:
            plt.imshow(image)
        else: 
            image = image.reshape(image.shape[0], image.shape[1])
            plt.imshow(image, cmap='gray')
        plt.axis('off')
    plt.show()

def main():
    rgb = False
    if rgb:
        kernels_list = [kernels.BLUR_FILTER_RGB, 
                        kernels.SHARPEN_FILTER_RGB, 
                        kernels.EDGE_FILTER_RGB,
                        kernels.TOP_SOBEL_RGB,
                        kernels.EMBOSS_FILTER_RGB]
    else:
        kernels_list = [kernels.BLUR_FILTER,
                        kernels.SHARPEN_FILTER,
                        kernels.EDGE_FILTER,
                        kernels.TOP_SOBEL,
                        kernels.EMBOSS_FILTER]

    kernels_list = kernels_list[1:]
    image1 = read_one_image('data/friday.jpg')
    
    if not rgb:
        image2 = tf.image.rgb_to_grayscale(image1)
        
    image3 = tf.expand_dims(image2, 0) # make it into a batch of 1 element
    images4 = convolve(image3, kernels_list, rgb)
    
    with tf.Session() as sess:
        # print(sess.run([image1.get_shape(),image2.get_shape(),image3.get_shape()]))
        i_4 = sess.run(images4) # convert images from tensors to float values
        show_images(i_4, rgb)
        print(sess.run(image1).shape,sess.run(image1),"image1")
        print(sess.run(image2).shape,sess.run(image2),"image2")
        print(sess.run(image3).shape,sess.run(image3),"image3")


if __name__ == '__main__':
    main()