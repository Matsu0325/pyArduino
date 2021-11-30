import serial
import serial.tools.list_ports as stlp
import sys
import re

slist = stlp.comports()

print('接続先を選択してください')
print('0 を入力するとプログラムを終了します\n')
for i in range(len(slist)):
    print(str(i+1) +':'+ str(slist[i][1]))
n = int(input())

if n == 0:
    print('プログラムを終了します')
    sys.exit()
elif n > len(slist):
    print('存在しないポートです')
    sys.exit()


with serial.Serial(str(slist[n-1][0]), 115200, timeout=0.0001) as s:
    while 1:
        print('\n数字を入力してください(endで終了)')
        txt = input()
        if 'k' in txt:
            txt = str(int(float(txt[:-1])*1000))
            print(txt)
        pat = re.compile('[0-9]+')
        if pat.fullmatch(txt):
            s.write((txt+'\n').encode())
        elif txt == 'end':
            break
        else:
            print('数字ではありません')