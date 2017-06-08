# -*- coding: utf-8 -*-
# (ハッシュマーク)コメントアウト記号
# randomモジュール入門（while文によるループ処理）
# while(条件式):
#   繰り返したい処理
# random.pyの名前で保存したらエラーになるよ。ファイルの名前は「ユニーク」に！！！
#
# Create 2017/06/08
# update 2017/06/08
# Auther Katsumi.Oshiro

import random

cnt = 0

while(cnt < 10):
    print(random.randint(1,1000))
    cnt = cnt + 1
