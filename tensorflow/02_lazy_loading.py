"""
Example of lazy vs normal loading
Created by uni xu (uniwow@sina.com) 2017/10/09
tensorflow research
"""
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf 


#Normal Loading
x = tf.Variable(5, name='x')
y = tf.Variable(10, name='y')
z = tf.add(x, y,name='z')


with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	writer = tf.summary.FileWriter('graphs/normal_loading', sess.graph)
	for _ in range(10):
		sess.run(z)
	print(tf.get_default_graph().as_graph_def())
	writer.close()


#Lazy loading
x = tf.Variable(10, name='x')
y = tf.Variable(20, name='y')

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	writer = tf.summary.FileWriter('graphs/lazy_loading', sess.graph)
	for _ in range(10):
		sess.run(tf.add(x, y,name='z'))
	print(tf.get_default_graph().as_graph_def()) 
	writer.close()