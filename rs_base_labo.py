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

import csv                  # csvモジュールの読み込み（CSVファイルの読み書き）
import glob                 # globモジュールの読み込み（ファイル名のパターンマッチング）
import pandas as pd         # pandasモジュールの読み込み

print('RS_Base血液検査CSVデータの取込（START）')
# 辞書（患者ID、生年月日）を初期化
birth = {}
# 患者マスター（name.csv）の読み込み
with open('../data/name.csv', 'r')as f:
    reader = csv.reader(f)
    for row in reader:
#       print(row[0],row[1],row[2],row[3])
        birth.update({row[0]:row[3]})

# 辞書(birth)：生年月日の検索テスト（患者ID:679）
print('患者ID:679の生年月日->', birth["679"])

# 年齢計算テスト（患者ID:679）
today = int(pd.to_datetime('today').strftime('%Y%m%d'))
birthday = int(pd.to_datetime(birth["679"]).strftime('%Y%m%d'))
print('患者ID:697の年齢->', int((today - birthday)/ 10000))

# フォルダ内の血液検査ファイル名の取得（ワイルドカードが使用可能）
txt_file = glob.glob('../data/labo/*.txt')

# 検査結果の出力
# 元データ：low[0]生年月日,low[1]患者ID,low[2]氏名,low[3]性別,low[5]検査項目名,low[6]判定,low[10]結果値）
with open("../data/labo/GLU-P.csv", "w") as f:
    for file_name in txt_file:
        with open(file_name, 'r')as f2:
            reader = csv.reader(f2)
            for low in reader:
                if low[5] == "GLU-P":
                    writer = csv.writer(f, lineterminator='\n')
                    listdata = []
                    listdata.append(low[1])
                    today = int(pd.to_datetime(low[0]).strftime('%Y%m%d'))
                    birthday = int(pd.to_datetime(birth[low[1]]).strftime('%Y%m%d'))
                    listdata.append(int((today - birthday)/ 10000))
                    if low[1] == "679":
                        listdata.append('')
                        listdata.append('')
                        listdata.append('')
                        listdata.append(low[10])
                    elif low[6] == "H":
                        listdata.append('')
                        listdata.append('')
                        listdata.append(low[10])
                    elif low[6] == "L":
                        listdata.append('')
                        listdata.append(low[10])
                    else:
                        listdata.append(low[10])
                    listdata.append('')
                    writer.writerow(listdata)

print('RS_Base血液検査CSVデータの取込（END）')
