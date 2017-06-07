# -*- coding: utf-8 -*-
# (ハッシュマーク)コメントアウト記号
# TensorBoard入門（Theanoライブラリの使用）
#
# Create 2017/06/07
# update 2017/06/07
# Auther Katsumi.Oshiro

#import tensorflow as tf
import numpy as np
import theano				# テアノ 行列演算用ライブラリ
import theano.tensor as T

#自動微分
def f(x):
	return x ** 2

def f_deriv(x):
	return 2 * x
