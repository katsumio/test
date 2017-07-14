'''
NumPy(数値計算・科学技術計算用ライブラリ)の使い方
Python v3.6.1 : TensorFlow v1.1.0
（２クラス）ロジスティック回帰モデル
　 →被説明変数が「買った」「買っていない」か、すなわち「0-1」になるような場合に用いられる
・TensorBoardの起動
　　tensorboard --logdir=log
・TensorBoardのWeb画面にアクセス
　　http://localhost:6006
Create 2017/07/13 : Update 2017/07/13 : Auther Katsumi.Oshiro
'''

import os
import numpy as np          # 数値計算ライブラリ
import tensorflow as tf

'''
a = [1, 2, 3]
print('a = [1, 2, 3] -> ',a)
b = [[4, 5, 6], [7, 8, 9]]
print('b = [[4, 5, 6], [7, 8, 9]] -> ', b)
'''

'''
NumPy配列(2 x 3 : 2行3列)
'''
i = np.array([[0, 1, 2], [3, 4, 5]])
c = np.array([[3, 4, 5], [6, 7, 8]])
print('i -> \n', i)
print('c -> \n', c)
print('i + c -> \n', i + c)
