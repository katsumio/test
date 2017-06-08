# -*- coding: utf-8 -*-
# 占いプログラムの作成
# \バックスラッシュの入力方法 optionキー + \キー

import random					# randomモジュールの読み込み

def number_input(message):		# 関数number_input()
	result = input(message)		# input()関数の戻り値は文字列型
	if(result.isdigit()):		# isdigit()関数で数値かチェック
		result = int(result)	# 数値ならint()関数で整数値に変換
		return result		# 戻り値として数値を返す
	else:
		return 0		# エラーとして0を返す

def judgment(omikuji):			# 関数judgment()
	rand = random.randint(1, 9)
	if (omikuji == rand):		# ユーザの入力と乱数値が一致した場合
		print("素晴しい！超大吉です！なんでも願いが叶います！")
	elif (omikuji > rand):
		print("まあまあかな。ラッキーアイテムはiPad！")
	elif (omikuji < rand):
		print("かなりまずいですよ！すぐにラッキーアイテムのiPhoneを手に入れて下さい！")

while(True):										# 無限ループ
	omikuji = number_input("１から９の中で一番好きな数字を入力して下さい\n\n")	# 関数number_input()の実行
	if((omikuji != 0) and (omikuji > 0) and (omikuji < 10)):
		print("あなたの好きな数字は" + str(omikuji) + "ですね！\n\n")
		print("それではその数字からあなたの運命を占って差し上げましょう。\n\n")

		judgment(omikuji)							# 関数judgment()の実行

		break

	else:
		print("１〜９の数字を入力して下さい。\n\n")
