import re

x = 'From: Using the : character'
y = re.findall('\S+@\S+',x)
print(y)