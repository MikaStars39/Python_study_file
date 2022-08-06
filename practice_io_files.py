text = '''1997年，我学会了开汽车
上坡，下坡，压死一千多
警察来追我，我跑到……
……的灯，没有开'''

f = open('read.txt', 'w')
f.write(text)
f.close()

f = open('read.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    else:
        print(line, end='')

f.close()
