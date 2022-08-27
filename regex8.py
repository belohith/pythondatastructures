import re

lin = 'write a line'
y = re.findall('^From .*@([^ ]*', lin)
print(y)