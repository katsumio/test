# -*- coding: utf-8 -*-
#
# 変数名 = open(ファイル名,モード)
# readline()メソッド：先頭から１行だけ読み込み
# readlines()メソッド：複数行の読み込み
# strip()メソッド：改行コードを取り除く
#
# Create 2017/06/08
# update 2017/06/08
# Auther Katsumi.Oshiro

# sample.txtが存在しない場合は、自動的に新規作成される。
f = open('sample.txt','w')      # 'w'：上書きモード

sample_str = 'Pythonは素晴しい言語です。'

# テキストファイルに書き込む
f.write(sample_str)
f.flush()
f.close()

# sample.txtを読み込みprintする
r = open('sample.txt','r')      # 'r'：読み込みモード

readme = r.readline()           # readline()メソッドは１行だけ読み込み
r.close

print(readme)
