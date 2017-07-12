# -*- coding: utf-8 -*-
# (ハッシュマーク)コメントアウト記号
# TensorFlow入門
# 線形回帰
# データ型
# →整数（符号付き）：int8：8ビット、int16：16ビット、int32：32ビット、int64：64ビット
# →浮動小数点数　　：float16：16ビット、float32：32ビット、float64：64ビット
#
# Create 2017/07/11
# update 2017/07/11
# Auther Katsumi.Oshiro

import tensorflow as tf
import numpy as np

# トレーニングデータの準備
# xの点をnumpyのrandom関数を使って100個生成しx_dataとする
# astypeメソッド（numpyのデータ型変換）
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

# 線形回帰のモデル定義（上記データをトレーニングデータとしてTensorFlowで線形回帰する）
# random_uniform：Tensorを一様分布なランダム値で初期化する（-1.0〜1.0）
w = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = w * x_data + b

# コスト関数の定義
# loss：線形回帰のコスト関数
# ある点の誤差は、予測データyと実データy_dataの差の二乗で定義し、全ての点の誤差の平均をlossとして定義
# optimizerの定義：最急降下法（引数の0.5は学習率←本来はいろいろな値を試すべき
# 最後に、このoptimizerでlossを最小化（minimize）するように指示
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 実行前の初期化
init = tf.global_variables_initializer()

# 実行フェイズ
sess = tf.Session()
sess.run(init)

# summaryの設定
# ある値を可視化したいときはサマリーと呼ばれるデータをログファイルに書き出します
# 可視化したい値がスカラー値の場合はtf.summary.scalarという関数でスカラー値をサマリーに追加
# 'cross_entropy'という名前のグラフをlossという変数の値で作成
tf.summary.scalar('cross_entropy', loss)
summary_op = tf.summary.merge_all()
summary_writer = tf.summary.FileWriter('data', graph=sess.graph)

# iteration回数を200回として、予めtrainに設定したコスト関数の最小化処理を繰り返し実行
# 20stepずつ、コンソールへの出力を行い、状況を確認
for step in range(201):
	sess.run(train)
# SummaryWriterで計算グラフを書く
#	summary_writer = tf.summary.FileWriter('data', graph=sess.graph)
#	tf.summary.scalar('one_plus_one_summary', train)
# stepが20の倍数の時だけ表示する
	if step % 20 == 0:
		summary_writer.add_summary(summary, step)
#		summary_str = sess.run(summary_op, feed_dict=dict_data)
#		summary_writer.add_summary(summary_str, step)
#		summary_writer.flush()
		print(step, sess.run(w), sess.run(b))

sess.close


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
