hand = open('clown.txt')

for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)