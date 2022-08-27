counts = { 'chuck':1, 'fred':47, 'jan': 100}
for k in counts:
    print(k, counts[k])

print(list(counts))
print(counts.keys())
print(counts.values())
print(counts.items())

for a,b in counts.items():
    print(a, b)