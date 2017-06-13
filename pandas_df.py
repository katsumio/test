# -*- coding: utf-8 -*-
# pandas（Python用データ分析モジュール）でCSVファイルの読み込みと書き込み
#
# read_csv()メソッド：csvファイルをロードする関数
# with構文（with ファイル読み込み as 変数）：close文がいらない
# ../data/yyk,csv 22,459件
# Create 2017/06/13
# update 2017/06/13
# Auther Katsumi.Oshiro

import pandas as pd                          # pandasモジュールの読み込み

# pandasのread_csvでファイルを読み込む
# そのまま read_csv とすると1行目を header として認識する
# ヘッダがない場合は header=None とする
#f3 = '%Y%m%d'
#my_parser = lambda date: pd.datetime.strptime(date, f3)
#df3 = pd.read_csv('../data/yyk.csv', encoding='euc_jp', parse_dates='YYKYMD', date_parser=my_parser)
#df3.head()
df = pd.read_csv('../data/yyk.csv', encoding='euc_jp', parse_dates=[3])
df = df.dropna(subset=['YYKYMD'])                       # 欠損値は削除

print(df [['YYKYMD', 'KEYYYKTIME']])                # 列の選択
#print(df.groupby('YYKYMD')['KEYYYKTIME'].mean())    # グループ化、集約（平均）

#print(dates_pd)

#pd.to_datetime(['YYKYMD'], format='%Y%m%d')

#print(pd.to_datetime(['YYKYMD'], format='%Y%m%d'))

#df = df.sort_values(by=["YYKYMD"])   # pandasでソート

#print(df.loc[(csv_data["YYKYMD"] > 20170709)])

# csvでの書き出し（インデックスは保存したくない場合：index=False）
#df.to_csv('../data/yyk2.csv', index=False)
