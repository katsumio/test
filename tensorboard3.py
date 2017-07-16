'''
TensorFlowの可視化ツール（TensorBoard）の使い方
Python v3.6.1 : TensorFlow v1.1.0
（２クラス）ロジスティック回帰モデル
　 →被説明変数が「買った」「買っていない」か、すなわち「0-1」になるような場合に用いられる
・TensorBoardの起動
　　tensorboard --logdir=log
・TensorBoardのWeb画面にアクセス
　　http://localhost:6006
Create 2017/07/13 : Update 2017/07/16 : Auther Katsumi.Oshiro
'''

import os
import numpy as np          # 数値計算ライブラリ
import tensorflow as tf

# 乱数シード（seed:種）を設定（グラフを作成する前に乱数シードを設定）
tf.set_random_seed(0)

'''
ログファイル用設定（TensorBoard用）
'''
LOG_DIR = os.path.join(os.path.dirname(__file__), 'log')

if os.path.exists(LOG_DIR) is False:
    os.mkdir(LOG_DIR)

'''
データの生成（numpyの配列）
'''
# ORゲート（論理和）
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([[0], [1], [1], [1]])

'''
1.モデルの定義
'''
# ロジスティック回帰のパラメータ：重み'w'とバイアス'b'（ y = σ(wx + b) ）
# 入力：2次元 出力：1次元
# 変数の宣言
w = tf.Variable(tf.zeros([2, 1]), name='w')
b = tf.Variable(tf.zeros([1]), name='b')

# プレースホルダーの宣言：データが格納される予定地
# モデルの出力：y=・・・
x = tf.placeholder(tf.float32, shape=[None, 2], name='x')
t = tf.placeholder(tf.float32, shape=[None, 1], name='t')
y = tf.nn.sigmoid(tf.matmul(x, w) + b, name='y')

'''
2.誤差関数の定義
'''
# 名前スコープ定義（name_scopeを付けることで可視化する領域をまとめてわかりやすくする）
# 学習の過程の可視化
# 交差エントロピー誤差関数を求める
# tf.reduce_sum：総和
with tf.name_scope('loss'):
    cross_entropy = \
        - tf.reduce_sum(t * tf.log(y) + (1 - t) * tf.log(1 - y))
tf.summary.scalar('cross_entropy', cross_entropy)  # TensorBoard 用に登録

'''
3.最適化手法の定義
'''
# 勾配降下法のOptimizerを指定し、引数として学習率(0.1)を与えている
with tf.name_scope('train'):
    train_step = \
        tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

# モデルの出力yは確率となっているので、y>=o.5かどうかでニューロンが発火するか決まります
with tf.name_scope('accuracy'):
    correct_prediction = tf.equal(tf.to_float(tf.greater(y, 0.5)), t)
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

'''
4.セッションの初期化
'''
init = tf.global_variables_initializer()
sess = tf.Session()

file_writer = tf.summary.FileWriter(LOG_DIR, sess.graph)  # TensorBoardに対応
summaries = tf.summary.merge_all()  # 登録した変数をひとまとめにする

sess.run(init)

'''
5.学習
'''
# range(始まりの数値, 最後の数値, 増加する量)　[始まりの数値]と[増加する量]は省略可能
# sess.run(train_step)は勾配降下法による学習 feed_dictによりx,tに値を代入
for epoch in range(200):
    sess.run(train_step, feed_dict={
        x: X,
        t: Y
    })
    print('x= \n', x)
    print('t= \n', t)

    summary, loss = sess.run([summaries, cross_entropy], feed_dict={
        x: X,
        t: Y
    })
    file_writer.add_summary(summary, epoch)  # TensorBoard に記録
