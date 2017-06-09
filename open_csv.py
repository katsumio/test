# -*- coding: utf-8 -*-
# CSVファイルの書き込みと読み込み
#
# 変数名 = open(ファイル名,モード)
# with構文（with ファイル読み込み as 変数）
#
# Create 2017/06/08
# update 2017/06/09
# Auther Katsumi.Oshiro

import csv                          # csvモジュールの読み込み

header = ['ID', 'name']             # ヘッダー
body = [                            # 内容
    [4023, '大城勝美'],
    [4024, '山田太郎'],
    [4025, '金城二郎']
]
with open('sample.csv', 'w') as f:  # ファイルを書き込みモードでオープン
    writer = csv.writer(f)          # writerオブジェクトを作成
    writer.writerow(header)         # ヘッダーを書き込む
    writer.writerows(body)          # 内容を書き込む

with open('sample.csv', 'r') as f:  # ファイルを読み込みモードでオープン
    reader = csv.reader(f)          # readerオブジェクトを作成
    header = next(reader)           # 最初の一行をヘッダーとして取得
    print (' '.join(header))        # ヘッダーをスペース区切りで表示
    for row1 in reader:             # 行ごとのリストを処理する
        print (' '.join(row1))      # 一行ずつスペース区切りで表示
