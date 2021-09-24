import sys
import csv
#from itertools import cycle

input_data = sys.argv[1]
key_now = sys.argv[2]
key_new = sys.argv[3]
output_data = input_data[:-4] + "_" + key_now + "_to_" + key_new + ".csv"

sounds = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

if key_now not in sounds :
    print('key_now not in souds')
    exit()

if key_new not in sounds :
    print('key_now not in souds')
    exit()

diff = sounds.index(key_new) - sounds.index(key_now)
print('diff=',diff)

with open(input_data, mode="r", encoding="utf-8") as rf:
    reader = csv.reader(rf)
    with open(output_data, mode="w", encoding="utf-8") as wf:
        writer = csv.writer(wf)
        for line in reader:
            new_line=[]
            for i in range(len(line)):
                print('line[',i,']=',line[i])
                if (len(line[i])>1) and (line[i][1] == '#'):
                    first = line[i][:2]
                    latter = line[i][2:]
                else:
                    first = line[i][:1]
                    latter = line[i][1:]
                new_line.append(sounds[(sounds.index(first) + diff)%12]+latter)
            writer.writerow(new_line)






