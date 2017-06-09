# -*- coding: utf-8 -*-
#
# 変数名 = open(ファイル名,モード)
# readline()メソッド：先頭から１行だけ読み込み
# readlines()メソッド：複数行の読み込み
# strip()メソッド：改行コードを取り除く
#
# バックスラッシュの入力方法（Mac）：option + ¥
# Create 2017/06/08
# update 2017/06/09
# Auther Katsumi.Oshiro

# sample.txtが存在しない場合は、自動的に新規作成される。
f = open('sample.txt','w')      # 'w'：上書きモード

sample_str = 'Pythonは素晴しい言語です。\nTnsorFlowは素晴しい機械学習ライブラリです。'

#
# テキストファイルに書き込む
#
f.write(sample_str)
f.flush()
f.close()

#
print ('ー読み込み例（１）ーreadlines()メソッドによる読み込み')
#
r = open('sample.txt','r')      # 'r'：読み込みモード
sentence_list = r.readlines()
r.close()

for sentence in sentence_list:
    print(sentence)
#
print ('ー読み込み例（２）ーstrip()メソッドによる改行コードの取り除き')
#
r = open('sample.txt','r')      # 'r'：読み込みモード
sentence_list = r.readlines()
r.close()

for sentence in sentence_list:
    print(sentence.strip())     # strip()：改行コードを取り除く
#
print ('ー読み込み例（３）ー実は最も簡単な読み込み')
#
r = open('sample.txt','r')      # 'r'：読み込みモード
for line in r:
    print(line.strip())
r.close()
