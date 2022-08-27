d = {'a': 10, 'b': 2, 'c':33}
print(d.items())
print(sorted(d.items()))

for k,v in sorted(d.items()):
    print(k, v)