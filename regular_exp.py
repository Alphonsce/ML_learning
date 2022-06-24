a = 'hello world'
b = 'hello мир'
c = 'hello 123'

l = (a, b, c)

r = r'hello\ ([0-9]*|[a-z]*)$'

import re

for i in l:
    print(re.findall(r, i))
    # re.split()