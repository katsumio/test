# -*- coding: utf-8 -*-
# (ハッシュマーク)コメントアウト記号
# TensorBoard入門（計算グラフを書く）
#
# Create 2017/06/05
# update 2017/06/05
# Auther Katsumi.Oshiro

import tensorflow as tf

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
		sess.run(tf.global_variables_initializer())
	sess.run(zz)
	# SummaryWriterで計算グラフを書く
	summary_writer = tf.summary.FileWriter('data', graph=sess.graph)
	tf.summary.scalar('one_plus_one_summary', zz)
