# -*- coding: utf-8 -*-
# (ハッシュマーク)コメントアウト記号
# プログラミングの第一歩は"Hello World"を出力することですが
# 機械学習では"MNIST"(エムニスト)「手書き文字データ」です
# MNIST:手書き文字の画像データセット
# 28X28(784ユニット)のピクセルデータを入力して、10クラスの分類問題を解く
# 訓練データ　：55,000（mnist.train）
# テストデータ：10,000（mnist.test）
# 検証データ　：5,000（mnist.validation）
#
# Create 2017/06/23
# update 2017/06/23
# Auther Katsumi.Oshiro

# mnist手書きデータの用意（インポート）
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# TensorFlowのインポート
import tensorflow as tf

# 入力データの次元をセット[入力データ：数は任意,：784次元]
x = tf.placeholder(tf.float32, [None, 784])

#ニューラルネットのパラメータをセット
w = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# 出力の設定
y = tf.nn.softmax(tf.matmul(x, w) + b)

# 正解ラベルの次元をセット
y_ = tf.placeholder(tf.float32, [None, 10])

# 損失関数の定義
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# 学習方法を決定
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# 初期化
init = tf.global_variables_initializer()

# 初期化の実行
sess = tf.Session()
sess.run(init)

# 学習を実行
for i in range(1000):
	batch_xs, batch_ys = mnist.train.next_batch(100)
	sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# 制度の確認
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))

# 出力と正解を調べた結果を獲得します
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# 最後にテストデータでニューラルネットを評価
print('ー正解ラベルとニューラルネットの予測を比較し正解率を表示ー')
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
