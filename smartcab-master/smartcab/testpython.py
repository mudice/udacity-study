import numpy as np

i = float(1000000000)
for t in range(1000000):
    i + 0.000001

print i - 1000000000

print 
print [None] + list((1,2,3,4))
xx = np.array([1,2])
yy = np.array([3,4])
dot = np.dot(yy, xx)
print dot

test_dict = dict({'a':1, 'b':5, 'c':3, 'd':4})
result = [action for action, value in test_dict.items() if value == max(test_dict.values())]
print result[0]

valid_actions = [None, 'forward', 'left', 'right']

import random
i = 0
while i < 10:
    probabity = random.random()
    print probabity
    if random.random() < 0.3:
        print 'OO:right'
    else:
        print 'OO:left'
    i +=1

i = 0
while i < 100:
    print random.choice(valid_actions)
    i += 1
    print "ok" if i % 2 == 0 else "nok"

print result[0]