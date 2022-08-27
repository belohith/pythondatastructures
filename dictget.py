counts = dict()
names = ['csev', 'cwen', 'csev', 'zqain', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

if name in counts:
    x = counts[name]
else :
    x = 0

x = counts.get(name, 0)