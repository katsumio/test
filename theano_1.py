# -*- coding: utf-8 -*-
# 数値計算ライブラリTheano（テアノ）の使い方：行列演算ができる（数式そのものを記述）
# Theanoはスカラー、ベクトル、行列、テンソルを表す変数をシンボルとして扱う
#
# numty：Pythonにおける標準的数値計算ライブラリ（計算手続きを記述）
#
# 変数名 = open(ファイル名,モード)
# with構文（with ファイル読み込み as 変数）
#
# Create 2017/06/08
# update 2017/06/09
# Auther Katsumi.Oshiro

import numpy as np                 # numpyモジュールをnpという名前で読み込み
import theano                      # 数値計算を高速化してくれるライブラリ
import theano.tensor as T          # tensorサブモジュールはTという名前で読み込み

x = T.dscalar('x')                 # スカラーを表すシンボルxを宣言
y = x**2

f = theano.function(inputs=[x], outputs=y)
