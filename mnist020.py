# -*- coding: utf-8 -*-
# (ハッシュマーク)コメントアウト記号
# プログラミングの第一歩は"Hello World"を出力することですが
# 機械学習では"MNIST"(エムニスト)「手書き文字データ」です
#
# TensorBoard入門（計算グラフを書く）
#
# sess.run(tf.global_variables_initializer())
#
# summary_op = tf.summary.merge_all()
# summary_writer = tf.summary.FileWriter('data', graph=sess.graph)
# tf.summary.scalar('cross_entropy', cross_entropy)
#
# locolhost:6006 -> SCALARS -> cross_entropy
#
# Create 2017/06/21
# update 2017/06/21
# Auther Katsumi.Oshiro

import tensorflow as tf

# mnist手書きデータの用意
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# softmaxでgradient discentする簡易な記述
images = tf.placeholder(tf.float32, shape=[None, 784])
labels = tf.placeholder(tf.float32, shape=[None, 10])
weights = tf.Variable(tf.zeros([784,10]))
softmax = tf.nn.softmax(tf.matmul(images, weights))
cross_entropy = -tf.reduce_sum(labels * tf.log(softmax))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# sessionの用意
sess = tf.Session()
sess.run(tf.initialize_all_variables())

# summaryの設定
tf.summary.scalar('cross_entropy', cross_entropy)
summary_op = tf.summary.merge_all()
summary_writer = tf.summary.FileWriter('data', graph=sess.graph)

# 100回実行してcross_entropyのsummaryを記録
for step in range(100):
    batch_images, batch_labels = mnist.train.next_batch(100)
    feed_dict = {images:batch_images, labels:batch_labels}
    sess.run([train_step, cross_entropy], feed_dict=feed_dict)
    summary_str = sess.run(summary_op, feed_dict=feed_dict)
    summary_writer.add_summary(summary_str, step)
