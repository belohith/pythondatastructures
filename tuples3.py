c = {'a':10, 'b': 1, 'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v, k))
print(tmp)

tmp1 = sorted(tmp, reverse=True)
print(tmp1)

#sort by values and not keys by reversing