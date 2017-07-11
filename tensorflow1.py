# -*- coding: utf-8 -*-
# (ハッシュマーク)コメントアウト記号
# TensorFlowの計算グラフ内の変数 tf.Variable の使い方
#
# Create 2017/06/19
# update 2017/06/19
# Auther Katsumi.Oshiro

import tensorflow as tf

x = tf.Variable(3, name='x')
y = x * 5

sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())
print(sess.run(y))

v = tf.Variable(3, name='v')
v2 = v.assign(5)
sess = tf.InteractiveSession()
sess.run(v.initializer)
print(sess.run(v))
print(sess.run(v2))


'''
with tf.name_scope('add_scope'):
	x = tf.constant(1, name='x')
	y = tf.constant(2, name='y')
	z = x + y

with tf.name_scope('multiply_scope'):
	zz = y * z

with tf.name_scope('division_scope'):
	yy = y / z

with tf.Session() as sess:
	with tf.name_scope('init_scope'):
		sess.run(tf.initialize_all_variables())
	sess.run(zz)
	# SummaryWriterで計算グラフを書く
	summary_writer = tf.summary.FileWriter('data', graph=sess.graph)
	tf.summary.scalar('one_plus_one_summary', zz)
'''
