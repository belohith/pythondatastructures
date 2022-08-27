import re

lin = 'write a line'
y = re.findall('@([^]*', lin)
print(y)