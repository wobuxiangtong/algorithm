"""
Example of tensorboard visualizer 
Created by uni xu (uniwow@sina.com) 2017/10/17
tensorflow research
"""
import matplotlib.pyplot as plt 
import tensorflow as tf 
import numpy as np 
import os 
from tensorflow.contrib.tensorboard.plugins import projector 
from tensorflow.examples.tutorials.mnist import input_data 


LOG_DIR='graphs/mnist'
NAME_TO_VISUALISE_VARIABLE= 'MNIST'
TO_EMBED_COUNT = 500
METADATA_PATH = os.path.join(LOG_DIR, 'metadata.tsv')
SPRITES_PATH = os.path.join(LOG_DIR, 'mnistdigits.png')

# 转换为图形矩阵
def vector_to_matrix_mnist(mnist_digits):
    return np.reshape(mnist_digits,(-1,28,28))

#灰度反转
def invert_grayscale(mnist_digits):
    return 1-mnist_digits

#生成 sprite 图片
def create_sprite_image(images):
    if isinstance(images, list):
        images = np.array(images)
    img_h = images.shape[1]
    img_w = images.shape[2]

    n_plots = int(np.ceil(np.sqrt(images.shape[0])))
    
    
    spriteimage = np.ones((img_h * n_plots ,img_w * n_plots ))

    for i in range(n_plots):
        for j in range(n_plots):
            this_filter = i * n_plots + j
            if this_filter < images.shape[0]:
                this_img = images[this_filter]
                print(img_h,img_w,n_plots,this_filter,images.shape[0])
                spriteimage[i * img_h:(i + 1) * img_h,
                  j * img_w:(j + 1) * img_w] = this_img
    return spriteimage


#定义变量
mnist = input_data.read_data_sets("data/mnist", one_hot=False)
X, Y = mnist.train.next_batch(TO_EMBED_COUNT)
embedding_var = tf.Variable(X, name=NAME_TO_VISUALISE_VARIABLE)

# 定义LOGGOR
summary_writer = tf.summary.FileWriter(LOG_DIR)

#初始化配置并绑定LOG
config = projector.ProjectorConfig()
embedding = config.embeddings.add()
embedding.tensor_name = embedding_var.name
embedding.metadata_path = 'metadata.tsv'
embedding.sprite.image_path = 'mnistdigits.png'
embedding.sprite.single_image_dim.extend([28,28])
projector.visualize_embeddings(summary_writer, config)

sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())
saver = tf.train.Saver()
saver.save(sess, os.path.join(LOG_DIR, "model.ckpt"), 1)








X = vector_to_matrix_mnist(X)
X= invert_grayscale(X)

sprite_image = create_sprite_image(X)
print(sprite_image[:3])

plt.imsave(SPRITES_PATH,sprite_image[:20],cmap='gray')
plt.imshow(sprite_image[:20],cmap='gray')

with open(METADATA_PATH,'w') as f:
    f.write("Index\tLabel\n")
    for index,label in enumerate(Y):
        f.write("%d\t%d\n" % (index,label))

