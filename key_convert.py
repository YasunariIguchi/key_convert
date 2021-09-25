#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
#from itertools import cycle

input_data = sys.argv[1]#第一引数；入力csvデータ
key_now = sys.argv[2]#第二引数；今のキー
key_new = sys.argv[3]#第三引数；新しいキー
output_data = input_data[:-4] + "_" + key_now + "_to_" + key_new + ".csv"#出力csvデータ

sounds = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']#キーのリスト

if key_now not in sounds :#第二引数が異常な場合はエラー文を返して終了
    print('key_now not in souds')
    exit()

if key_new not in sounds :#第三引数が異常な場合はエラー文を返して終了
    print('key_new not in souds')
    exit()

diff = sounds.index(key_new) - sounds.index(key_now)#新旧キーの差分
#print('diff=',diff)

with open(input_data, mode="r", encoding="utf-8") as rf:#入力csvデータを読み込む
    reader = csv.reader(rf)
    with open(output_data, mode="w", encoding="utf-8") as wf:#出力csvデータを開く
        writer = csv.writer(wf)
        for line in reader:#入力csvデータを一行読む
            new_line=[]#変換後のデータを格納
            for i in range(len(line)):#一行を更に一つずつ読む
                if(line[i][0][0]=='♪'):#歌詞はそのまま
                    new_line=line
                else:
                    #print('line[',i,']=',line[i])
                    if (len(line[i])>1) and (line[i][1] == '#'):#シャープがあるか判別
                        first = line[i][:2]
                        latter = line[i][2:]
                    else:
                        first = line[i][:1]
                        latter = line[i][1:]
                    new_line.append(sounds[(sounds.index(first) + diff)%12]+latter)#新しいキーでのコードを作成
            writer.writerow(new_line)#新しいコードを書き込み
        writer.writerow(['(capo:'+str(-diff%12)+')'])#ギターcapoの位置
print('(capo:'+str(-diff%12)+')')
#writer.writerow(['capo: ',-diff%12])






