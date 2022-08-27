friends = ['Nik', 'Rox', 'Pad']
friends.sort()
print(friends)
print(friends[1])

portal = [12,24,35,56,78]
print(len(portal))
print(max(portal))
print(min(portal))
print(sum(portal))
print(sum(portal)/len(portal))

total = 0 #less memory
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1

average = total/count
print('Average: ', average)

numlist = list()  #more memory
while True:
    inp1 = input('Enter a number: ')
    if inp1 == 'done': break
    value1 = float(inp1)
    numlist.append(value1)

average1 = sum(numlist) / len(numlist)
print('Average: ', average1)