import re

hand = open('clown.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)