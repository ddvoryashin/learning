#################
# Lists
#################
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list[::2]) # every item with step=2
print(my_list[::-1]) # in reverse order

new_list = my_list # if you change new_list, my_list will also change
new_list = my_list.copy() # if you change new_list, my_list will stay the same
new_list = list(my_list) # if you change new_list, my_list will stay the same
new_list = my_list[:] # if you change new_list, my_list will stay the same

#################
# Tuples
#################

# ways to create
my_tuple = (1, 2, 3, 4)
my_tuple = 1, 2, 3, 4
my_tuple = (1,)
my_tuple = tuple(my_list)

#my_tuple[0] = 'Other' # can't do this

i1, *i2, i3 = my_tuple
print(i1) # 1
print(i2) # [2, 3]
print(i3) # 4

# comparing speed of creating list vs tuple
import timeit
print(timeit.timeit(stmt='[0, 1, 2, 3, 4]', number=1000000))
print(timeit.timeit(stmt='(0, 1, 2, 3, 4)', number=1000000))

#################
# Dictionaries
#################

# ways to create
my_dict = {'name': 'Max', 'age': 28, 'city': 'New York'}
my_dict2 = dict(name='Max', age=28, city='Boston')

my_dict2['email'] = 'xyz@gmail.com'

# deletion
del my_dict2['email']
my_dict2.pop('name')
my_dict2.popitem() # last one

for key, value in my_dict.items():
    print(key + ' = ' + str(value))

# how to copy
my_dict_copy = my_dict.copy()
my_dict_copy = dict(my_dict)

my_dict.update(my_dict2) # adds non-existent keys and their values from my_dict_2

#################
# Sets
#################

my_set = {1, 2, 3, 2, 1} # 1, 2, 3
my_set = set([1, 2, 3])
my_set = set('Hello') # good for countig unique characters

my_set.add(4)
my_set.remove(4)
my_set.discard(4) # no error when there is no 4
my_set.clear()

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
u = odds.union(evens) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
i = odds.intersection(evens) # set()

setA = {0, 1, 2, 3, 4, 5}
setB = {0, 1, 2, 10, 11, 12}
diff = setA.difference(setB) # {3, 4, 5}
symm_diff = setA.symmetric_difference(setB) # {3, 4, 5, 10, 11, 12}

setA = {0, 1, 2, 3, 4}
setB = {0, 1, 2}
setC = {5, 6, 7}
print(setA.issuperset(setB)) # True
print(setB.issubset(setA)) # True
print(setA.isdisjoint(setC)) # True

setA = frozenset([1, 2, 3, 4])
#setA.add(5) # Error
#setA.remove(1) # Error

#################
# Strings
#################

var = 3.12345
var2 = 6
my_string = "var is %.2f" % var # var is 3.12
my_string = "var is {:.2f} and {}".format(var, var2) # var is 3.12 and 6
my_string = f"var is {var} and {var2}"

#################
# Collections
#################

from collections import Counter
a = 'aaaaabbbbccc'
my_counter = Counter(a) # {'a': 5, 'b': 4, 'c': 3}
print(my_counter.most_common(2)) # [('a', 5), ('b', 4)]
print(my_counter.most_common(2)[0][0]) # a
print(list(my_counter.elements()))

from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt) # Point(x=1, y=-4)

from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1
print(ordered_dict) # OrderedDict([('b', 2), ('c', 3), ('d', 4), ('a', 1)])

#from collections import defaultdict  # didn't get it
#default_dict = defaultdict('int')
#default_dict['a'] = 1
#default_dict['b'] = 2
#print(default_dict['c']) # 0

from collections import deque
d = deque()
d.append(1)
d.append(2) # [1, 2]

d.appendleft(3) # [3, 1, 2]
d.popleft() # [1, 2]

d.extendleft([4, 5, 6]) # [6, 5, 4, 1, 2]
d.rotate(-2) # [4, 1, 2, 6, 5]

#################
# Itertools
#################
# always print(list(itertool))
from itertools import product
a = [1, 2]
b = [3]
prod = product(a, b)
print(list(prod)) # [(1, 3), (2, 3)]
prod = product(a, b, repeat=2)
print(list(prod)) # [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]

from itertools import permutations
a = [1, 2, 3]
perm = permutations(a, 2) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
comb = combinations_with_replacement(a, 2) # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

from itertools import accumulate
import operator
a = [1, 2, 3]
acc = accumulate(a) # [1, 3, 6]
acc = accumulate(a, func=operator.mul) # [1, 2, 6]
acc = accumulate(a, func=max) # [1, 2, 3]

from itertools import groupby

a = [1, 2, 3, 4]
groupby_obj = groupby(a, key=lambda x: x<3)
for key, value in groupby_obj:
    print(key, list(value)) # True [1, 2]
                            # False [3, 4]

from itertools import count, cycle, repeat
# count from 10 to 15
for i in count(10):
    print(i)
    if i == 15: break

# cycle through a 3 times
a = [1, 2, 3]
k = 0
for i in cycle(a):
    print(i)
    k+=1
    if k == 3: break

# repeat 1 5 times
for i in repeat(1, 5):
    print(i)

#################
# Lambdas
#################

points2D = [(1, 2), (-1, 15), (4, 3), (7, 4)]
points2D_sorted = sorted(points2D) # sort by keys
points2D_sorted = sorted(points2D, key=lambda x: x[1]) # sort by values


a = [1, 2, 3, 4]
# map
b = map(lambda x: x*2, a)
b = [x*2 for x in a] # same
# filter
b = filter(lambda x: x%2==0, a)
b = [x for x in a if x%2==0] # same
# reduce
from functools import reduce
product_a = reduce(lambda x,y: x*y, a) # 720 - multiplies all elements

#################
# Enumerate
#################
names = ['John', "Jack", 'Will']
# prints all names
for i, name in enumerate(names):
    print(name)

#################
# Errors and Exceptions
#################

x = 5
if x < 0:
    raise Exception('x must be positive')

assert (x>=5), 'x is not positive'

try:
    a = 5 / 0
except Exception as e:
    print(e)

try:
    a = 5 / 0
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('fine')
finally:
    print('cleaning up...')

class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)

#################
# Logging
#################

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

logging.debug('some message')
logging.info('some message')
logging.warning('some message')
logging.error('some message')
logging.critical('some message')

import helper
