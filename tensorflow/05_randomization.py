""" Examples to demonstrate ops level randomization
Created by uni xu (uniwow@sina.com) 2017/11/5
"""
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf

c = tf.random_uniform([], -10, 10, seed=2)

with tf.Session() as sess:
    print(sess.run(c)) 
    print(sess.run(c))

c = tf.random_uniform([1,3], -10, 10, seed=2)

with tf.Session() as sess:
    print(sess.run(c)) 

with tf.Session() as sess:
    print(sess.run(c)) 

c = tf.random_uniform([], -10, 10, seed=2)
d = tf.random_uniform([], -10, 10, seed=2)

with tf.Session() as sess:
    print(sess.run(c)) 
    print(sess.run(d)) 


tf.set_random_seed(2)
c = tf.random_uniform([], -10, 10)
d = tf.random_uniform([], -10, 10)

with tf.Session() as sess:
    print(sess.run(c)) 
    print(sess.run(d)) 


    