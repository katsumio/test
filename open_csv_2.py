# -*- coding: utf-8 -*-
# CSVファイルの書き込みと読み込み
#
# 変数名 = open(ファイル名,モード)
# with構文（with ファイル読み込み as 変数）：close文がいらない
#
# Create 2017/06/08
# update 2017/06/09
# Auther Katsumi.Oshiro

import csv                          # csvモジュールの読み込み

# ファイルを読み込みモードでオープン 'rb'r:読み込み専用 b:バイナリモード
with open('../data/yyk.csv', 'r', encoding='euc_jp') as f:
    reader = csv.reader(f)          # readerオブジェクトを作成
    header = next(reader)           # 最初の一行をヘッダーとして取得
    print (' '.join(header))        # ヘッダーをスペース区切りで表示
    for row1 in reader:             # 行ごとのリストを処理する
        print (' '.join(row1))      # 一行ずつスペース区切りで表示

# ファイルを書き込みモードでオープン
with open('../data/yyk2.csv', 'w') as f:
    writer = csv.writer(f)          # writerオブジェクトを作成
    writer.writerow(header)         # ヘッダーを書き込む
    writer.writerows(body)          # 内容を書き込む
