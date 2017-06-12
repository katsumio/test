# -*- coding: utf-8 -*-
# pandasでCSVファイルの書き込みと読み込み
#
# read_csv()メソッド：csvファイルをロードする関数
# with構文（with ファイル読み込み as 変数）：close文がいらない
#
# Create 2017/06/12
# update 2017/06/12
# Auther Katsumi.Oshiro

import pandas as pd                          # pandasモジュールの読み込み

# pandasのread_csvでファイルを読み込む
# そのまま read_csv とすると1行目を header として認識する
# ヘッダがない場合は header=None とする
csv_data = pd.read_csv('../data/yyk.csv', encoding='euc_jp')

print(len(csv_data))                        # 行数
print(csv_data.shape)                       # (行数,列数)
#print(csv_data.info())                      # カラム情報の一覧
#print(csv_data.head(10))                    # 先頭10行を確認
#print(csv_data.tail(10))                    # 後頭10行を確認

#csv_data.sort("YYKYMD")

csv_data = csv_data.sort_values(by=["YYKYMD"])   # pandasでソート

#csv_data[csv_data.YYKYMD > 20170709]
#csv_data['YYKYMD'] >= 20170710
#print(csv_data)

# csvでの書き出し
csv_data.to_csv('../data/yyk2.csv')
#df[csv_data.YYKYMD > 20170709]
#df.to_csv('../data/yyk2.csv')
