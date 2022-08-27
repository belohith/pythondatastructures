fruit = 'Banana'
#fruit[0] = 'b'

x = fruit.lower()
print(x)

lotto =[2,14,26,41,63]
print(lotto)

lotto[2] = 28
print(lotto)

print(len(lotto))
print(range(4))
print(range(len(lotto)))

friends = ['Nik','John','Bob']
for i in friends:
    print('Hey, ', i)

for j in range(len(friends)) :
    i = friends[j]
    print('Yo, ', i)

print(len(friends))
print(range(len(friends)))

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

d = [7,8,9,10]
print(d[1:3])

e = list()
print(type(e))
print(dir(e))

d.append(11)
print(d)

print(9 in d)
print(9 not in d)