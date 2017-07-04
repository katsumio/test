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

import csv                          # csvモジュールの読み込み

import glob                         # globモジュールの読み込み

# 辞書（患者ID、生年月日）を初期化
birth = {}
# 患者マスター（name.csv）の読み込み
with open('../data/name.csv', 'r')as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0],row[1],row[2],row[3])
        birth.update({row[0]:row[3]})

print(birth["679"])

'''
dict = {}
for row2 in kanjya:
    print(row2)
    dict.update({row2[0]:row2[3]})
f.close()
'''

# フォルダ内の血液検査ファイル名の取得（ワイルドカードが使用可能）
txt_file = glob.glob('../data/labo/(BP)*.txt')
# print(txt_file)
# for file in txt_file:
#     print(file)

'''
with open("../data/labo/TCHO-P.txt", "w") as f:
    for file_name in txt_file:
        with open(file_name, 'r')as target_file:
            for line in open(file_name, "r"):
                if line[0:6] == "TCHO-P":
                    f.write(line)
                    print(line)

'''
