# -*- coding: utf-8 -*-
# txtファイルの書き込みと読み込み
#
# 変数名 = open(ファイル名,モード)
# with構文（with ファイル読み込み as 変数）：close文がいらない
# for 変数 in オブジェクト:
#     実行する処理
# スライスを使った部分文字列の取得 [0:6]
#
# Create 2017/06/30
# update 2017/06/30
# Auther Katsumi.Oshiro

# import csv                        # csvモジュールの読み込み

import glob                         # globモジュールの読み込み

# 患者マスター（name.csv）の読み込み

# フォルダ内の血液検査ファイル名の取得（ワイルドカードが使用可能）
txt_file = glob.glob('../data/labo/(BP)*.txt')
# print(txt_file)
# for file in txt_file:
#     print(file)

with open("../data/labo/TCHO-P.txt", "w") as f:
    for file_name in txt_file:
        with open(file_name, 'r')as target_file:
            for line in open(file_name, "r"):
                if line[0:6] == "TCHO-P":
                    f.write(line)
                    print(line)

'''
for line in open("../data/labo/(BP)679.txt", "r"):
    if line[0:6] == "TCHO-P":       # 開始インデックス[0]から終了インデックス[6]まで
        print(line)
print("Finish!")
'''

'''
# ファイルを読み込みモードでオープン 'rb'r:読み込み専用 b:バイナリモード
with open('../data/labo/(BP)679.txt', 'r', encoding='shift_jis') as f:
    reader = csv.reader(f)          # readerオブジェクトを作成
    header = next(reader)           # 最初の一行をヘッダーとして取得
    print (' '.join(header))        # ヘッダーをスペース区切りで表示
    for row1 in reader:             # 行ごとのリストを処理する
        print (' '.join(row1))      # 一行ずつスペース区切りで表示

# ファイルを書き込みモードでオープン
with open('../data/labo/test_679.csv', 'w') as f:
    writer = csv.writer(f)          # writerオブジェクトを作成
    writer.writerow(header)         # ヘッダーを書き込む
    writer.writerows(body)          # 内容を書き込む
'''
