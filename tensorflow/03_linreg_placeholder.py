""" 
Solution for simple linear regression using placeholders
Created by uni xu (uniwow@sina.com) 2017/10/16
"""

import time

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

import utils

DATA_FILE = 'data/birth_rate.txt'

# Step 1: 读取数据
data, n_samples = utils.read_birth_life_data(DATA_FILE)

# Step 2: 创建占位符变量
X = tf.placeholder(tf.float32, name='X')
Y = tf.placeholder(tf.float32, name='Y')

# Step 3: 生成权重及偏移变量
w = tf.get_variable('weights', initializer=tf.constant(0.0))
b = tf.get_variable('bias', initializer=tf.constant(0.0))

# Step 4: 建立线性模型
Y_predicted = w * X + b 

# Step 5: 确定损失函数(这里使用平方差最小，也可以用胡波损失)
loss = tf.square(Y - Y_predicted, name='loss')
# loss = utils.huber_loss(Y, Y_predicted)

# Step 6: 使用梯度下降法优化损失函数
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)


start = time.time()
writer = tf.summary.FileWriter('./graphs/linear_reg', tf.get_default_graph())
with tf.Session() as sess:
	# Step 7: 初始化变量
	sess.run(tf.global_variables_initializer()) 
	
	# Step 8: 遍历100次
	for i in range(100): 
		total_loss = 0
		for x, y in data:
			# 查看每次遍历后的平均损失
			_, l = sess.run([optimizer, loss], feed_dict={X: x, Y:y}) 
			total_loss += l
		print('epoch {0}: {1}'.format(i, total_loss/n_samples))

	# 关闭文件
	writer.close() 
	
	# Step 9: 取出权重变量值
	w_out, b_out = sess.run([w, b]) 

print('Took: %f seconds' %(time.time() - start))

# 绘制图形

plt.plot(data[:,0], data[:,1], 'bo', label='真实数据')
plt.plot(data[:,0], data[:,0] * w_out + b_out, 'r', label='预测数据')
plt.legend()
plt.show()