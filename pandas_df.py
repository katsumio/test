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
import datetime                              # datetimeモジュールの読み込み

today = datetime.date.today()
print (today)
first_month = datetime.date(day=1, month=today.month, year=today.year)
print (first_month)

# 10行だけ表示するおまじない
pd.options.display.max_rows = 10

# pandasのread_csvでファイルを読み込む
# そのまま read_csv とすると1行目を header として認識する
# ヘッダがない場合は header=None とする
# pandasでデータを読み場合、dtypeを指定した方が安全（dtypeを指定しないと勝手に型を判別）
# とりあえず最初は全てobjectで読み込む
df = pd.read_csv('../data/yyk.csv', encoding='euc_jp', parse_dates=[3], dtype = 'object')
df = df.dropna(subset=['YYKYMD'])                       # 欠損値は削除

#print(df [['YYKYMD', 'KEYYYKTIME']])                # 列の選択
#print(df.groupby('YYKYMD')['KEYYYKTIME'].mean())    # グループ化、集約（平均）

# 検索条件：予約年月日'YYKYMD' >= today and 予約件数'YYKCNT' > '000' and 予約時間'YYKTIME' == '0000'
df = df[(df['YYKYMD'] >= first_month) & (df['YYKCNT'] > '000') & (df['YYKTIME'] == '0000')]

#df = df[df['YYKCNT'] > '000']

df = df.sort_values(by=["YYKYMD", "KEYYYKTIME"])   # pandasでソート
print(df)

# csvでの書き出し（インデックスは保存したくない場合：index=False）
df.to_csv('../data/yyk2.csv', index=False)
