# -*- coding: utf-8 -*-
# 検体検査結果データ（患者ごと）の読み込みと検体検査結果データ（検査項目ごと）の出力
# └→RS_Base_laboファイル
#
# 入力ファイル
# └→患者マスターファイル　　　：name.csv
# └→検体検査結果データファイル：患者ID.txt（例：101.txt,102.txt,103.txt・・・）
#
# Create 2017/07/09 : Update 2017/07/09
# Auther Katsumi.Oshiro

import csv                  # csvモジュールの読み込み（CSVファイルの読み書き）
import glob                 # globモジュールの読み込み（ファイル名のパターンマッチング）
import pandas as pd         # pandasモジュールの読み込み
import os                   # osモジュールの読み込み

print('# RS_Base_laboデータによる検体検査データの作成（START）')
# 辞書（患者ID、生年月日）の作成
birth = {}
# 患者マスター（name.csv）の読み込み
count = 0
with open('../data/name.csv', 'r')as f:
    reader = csv.reader(f)
    for row in reader:
#       print(row[0],row[1],row[2],row[3])
        birth.update({row[0]:row[3]})
        count += 1
print('# 患者マスター読み込み件数--------->', count)

# 辞書(birth)：生年月日の検索テスト（患者ID:679）
print('# 辞書テスト：患者ID:679の生年月日->', birth["679"])

# 年齢計算テスト（患者ID:679）
today = int(pd.to_datetime('today').strftime('%Y%m%d'))
birthday = int(pd.to_datetime(birth["679"]).strftime('%Y%m%d'))
print('# 年齢テスト：患者ID:697の年齢----->', int((today - birthday)/ 10000))

# フォルダ内の検体検査ファイル名の取得（ワイルドカードが使用可能）
txt_file = glob.glob('../data/labo/*.txt')

blood = input('# 検体検査名を入力して下さい：')

count = 0
# 検体検査結果ファイル（検査項目ごと）の作成
# 元データ：low[0]生年月日,low[1]患者ID,low[2]氏名,low[3]性別,low[5]検査項目名,low[6]判定,low[10]結果値）
with open("../data/labo/" + blood + ".csv", "w") as f:
    writer = csv.writer(f, lineterminator='\n')
    header = []
    header.append('患者ID')
    header.append('年齢')
    header.append('基準値（男）')
    header.append('基準値（女）')
    header.append('基準値以下（男）')
    header.append('基準値以下（女）')
    header.append('基準値以上（男）')
    header.append('基準値以上（女）')
    header.append('私')
    writer.writerow(header)
    for file_name in txt_file:
        with open(file_name, 'r')as f2:
            reader = csv.reader(f2)
            for low in reader:
                if low[5] == blood:
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
                        listdata.append('')
                        listdata.append('')
                        listdata.append('')
                        listdata.append(low[10])
                    elif low[6] == "H":
                        if low[3] == "男性":
                            listdata.append('')
                            listdata.append('')
                            listdata.append('')
                            listdata.append('')
                            listdata.append(low[10])
                        else:
                            listdata.append('')
                            listdata.append('')
                            listdata.append('')
                            listdata.append('')
                            listdata.append('')
                            listdata.append(low[10])
                    elif low[6] == "L":
                        if low[3]  == "男性":
                            listdata.append('')
                            listdata.append('')
                            listdata.append(low[10])
                        else:
                            listdata.append('')
                            listdata.append('')
                            listdata.append('')
                            listdata.append(low[10])
                    else:
                        if low[3] == "男性":
                            listdata.append(low[10])
                        else:
                            listdata.append('')
                            listdata.append(low[10])
                    listdata.append('')
                    writer.writerow(listdata)
                    count += 1

print('# 検体検査データ出力件数----------->', count)
if count == 0:
    os.remove("../data/labo/" + blood + ".csv")
else:
    print('# ' + blood + '.csv ファイルを作成しました')
print('# RS_Base_laboデータによる検体検査データの作成（END）')
