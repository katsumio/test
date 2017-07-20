# -*- coding: utf-8 -*-
# (ハッシュマーク)コメントアウト記号
# randomモジュール入門（）
# random.pyの名前で保存したらエラーになるよ。ファイルの名前は「ユニーク」に！！！
#
# Create 2017/07/18
# update 2017/07/18
# Auther Katsumi.Oshiro

#
# import sys
import tkinter

'''
font=("Helevetica", 32)
var = tkinter.Label(text="Hello world!", font=font)

var.pack()
var.mainloop()
'''
root = tkinter.Tk()
root.title(u"ソフトウェア タイトル")
root.geometry("400x300")

'''
# ラベル
static1 = tkinter.Label(text=u'ラベル')
static1.pack()
'''

'''
# エントリー
editbox = tkinter.Entry(width=50)
editbox.insert(tkinter.END,"挿入する文字列")
editbox.pack()
# Entryの中身の取得
value = editbox.get()
'''

# ボタン
button = tkinter.Button(text=u'ボタンです', width=30)
button.pack()

root.mainloop()
