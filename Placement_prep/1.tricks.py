#  get reminder 

import numpy as np


rem = 10 % 3   # 10 % 3 = 1 or 3 % 5 = 3

#  get quotient
quo = 10 // 3  # 10 // 3 = 3 or 5 // 7 = 0

#  get float quotient
quo = 10 / 3  # 10 / 3 = 3.33333 or 5 / 7 = 0.14285714285714285

#  join all elements of list in a string
l= ['f','o','o','b','a','r'] 
print("".join(l))

#  seperate all elements of string to list of characters

l = "foo"
l = list(l)    # ['f', 'o', 'o']
print(l)

#  seperate all elements of list of string to list of characters

l = ["foo", "bar"]  # [['f', 'o', 'o'], ['b', 'a', 'r']]
l = map(list, l)
print(list(l))

#  convert ND list to 1D list where each list in ND list have same length

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l = np.array(l).ravel()  # [1, 2, 3, 4, 5, 6, 7, 8, 9]



# ------------------------------------------------------------------------------------------------------------------------------------------
#  using itertools 

import itertools

#  counter 
#  counter can be used count sequence of elements

counter = itertools.count(10 , 100)  # start from 10 and increment by 100 , it has no end i.e. infinite number loop
#  itertools.count(start, step)  => step can be negetive or in decimal also

for i in counter:      # looping till infinity until if we stop it
    print(i)
    if i == 210:
        break

print(counter)      # prints counter object with next possible value

print(next(counter))  # get next value of counter , update value of counter in sequance



#  zip_longest
#  zip_longest can be used to zip two or more iterables(can be list) together
#  zip_longest will zip values until longest iterable is exhausted unlike normal zip where it will stop when shortest iterable is exhausted
#  fill value can be used to fill empty space in zip_longest if its iterable exhausted
p = itertools.zip_longest(['a', 'b', 'c', 'r' , 'h'], ['d', 'e', 'f'], fillvalue='x')

print(list(p))



#  cycle 

#  cycle can be used to loop through an iterable infinitely

p = itertools.cycle(['a', 'b', 'c'])

# for i in p:   # looping infinitely through ['a', 'b', 'c']
#     print(i)

print(next(p))  # get next value of cycle , update value of cycle in sequance
print(next(p))
print(next(p))
print(next(p))


# repeat
# repeat can be used to repeat an iterable infinitely but different from cycle

r = itertools.repeat('a', 3)   # repeat 'a' 3 times , after 3 times if tries to access next value it will raise error
#  if 3 is not given it will repeat infinitely





# permutations => every possible combination of the elements , can be repeated with value misplaced for e.g. A,B,C  and B,A,C   is possible 
for p in itertools.permutations('ABC'):
    print(p)
print("Total possible permuations are ", len(list(itertools.permutations('ABC'))))
#  another method
# list1,list2 = [1,2,3] , [5,6]
# p_list = [[x,y] for x in list1 for y in list2]
# print("plist :",p_list)

# combinations => every possible unique combination of the elements , can not be repeated with value misplaced for e.g. A,B,C  and B,A,C   is not possible
for c in itertools.combinations('ABCD', 3):   # list of elements , number of elements in the combination ;   [3,7,8] is also can be used 
    print(c)
print("Total possible combinations are ", len(list(itertools.combinations('ABCD', 3))))

#  both permutations and combinations does'nt allow even single duplicate element in combination formed

#  combination with replacement
# combination with replacement will allow duplicate element in combination formed
for c in itertools.combinations_with_replacement('ABCD', 3):    
    print(c)
print("Total possible combinations with_replacement are ", len(list(itertools.combinations_with_replacement('ABCD', 3))))

#  product
#  product can be used to get all possible combination of elements in list

for p in itertools.product([1, 2, 3], repeat=2):  # repeat is number of elements in the avialable combination
    print(p)





# chain : It is a function to which map passes each element of given iterable.
#  it can join multiple types of iterables

print(list(itertools.chain([1,5,9,7] , (8,7,5,3) , range(50,60))))   

l = [[1,2,3],[1,2,3]]
print(list(itertools.chain(*l)))   # * is used to unpack the list if single list is passed to chain lists inside that list


#  accumulate : It is a function which add the elements of iterable to a running total nad return a list of running total
#  e.g.  [1,2,3,4] => [1,3,6,10]

r = itertools.accumulate([1,2,3,4])

# for multiply instead of add in accumaute function

import operator
r = itertools.accumulate([1,2,3,4], operator.mul)    # e.g. [1,2,3,4,0] => [1,2,6,24,0]




# ------------------------------------------------------------------------------------------------------------------------------------------
#  using collection 

import collections   # contains specialized collection data types like deque, defaultdict, OrderedDict, Counter


#  counter makes dict from list of elemrents with key as unique element and value as count of element , used to count hashable elements(unique)
#  it is in decscending order of count
c= collections.Counter([8,9,8,9,5,6,2,36,5 , 5])   # key : set(list) , value : count of set(list)
print(c)   # Counter({5: 3, 8: 2, 9: 2, 6: 1, 2: 1, 36: 1})
print(list(c.elements()))   # return list of elements in counter  => [8, 8, 9, 9, 5, 5, 5, 6, 2, 36]
print(c.most_common(2))   # return list of most common elements in counter for first 2 entries => [(5, 3), (8, 2)]   (element, count)
print(c.most_common())   # return list of most common elements in counter for all entries => [(5, 3), (8, 2), (9, 2), (6, 1), (2, 1), (36, 1)]   (element, count)
sub = {5:1}      # subtract 5 1times from counter
c.subtract(sub)   # subtract sub from counter
print(c)  # Counter({8: 2, 9: 2, 5: 2, 6: 1, 2: 1, 36: 1})


#  namedtuple : It is a tuple with named fields

n =collections.namedtuple('my_touple', ('x', 'y' , 'z'))   #  2 arguments : name of tuple , list of fields
a = n(1,2,3)          # assign values to fields , requires exact number of arguments mentioned in list of fields
print("namedtuple :", a)          # my_touple(x=1, y=2, z=3)


# deque : It is a double-ended queue , it can be used to add or remove elements from both sides of the queue , 
#         it is actually a list which is optimized for adding and removing elements from both sides

d = collections.deque(['a', 'b', 'c'])

d.append('d')      # add element to right side of deque
d.appendleft('e')  # add element to left side of deque
d.pop()           # remove element from right side of deque
d.popleft()       # remove element from left side of deque


# chainmap : It is a class which can be used to chain multiple mappings together , it is single view for multiple mappings , it does not perform any operation on mappings having same keys
dic1 = {'a': 1, 'b': 2}
dic2 = {'a': 3, 'c': 4}

c = collections.ChainMap(dic1 , dic2)

print("chainmap :", c)   # ChainMap({'a': 1, 'b': 2}, {'a': 3, 'c': 4})



#  ordereddict : It is a class which can be used to create an ordered dictionary , it is a dictionary which keeps the order of keys as they are added

o = collections.OrderedDict()

o['a'] = 1
o['b'] = 2
o['c'] = 3
print("ordereddict :", o)   # OrderedDict([('a', 1), ('b', 2), ('c', 3)])
o['b'] = 4
print("ordereddict :", o)   # OrderedDict([('a', 1), ('b', 4), ('c', 3)])   if it is not ordered then it will be in order i.e a,c,b



#  defaultdict : It is a class which can be used to create a dictionary with default values , it is a dictionary which has default values for keys which are not present in dictionary
#  i.e. if key is not present in dictionary then it will return default value for that key

d = collections.defaultdict(lambda: 'default')

d[0] = 'a'
d[1] = 'b'

print("defaultdict :", d)   # defaultdict(<function <lambda> at 0x000002A8F8F8F8F8>, {0: 'a', 1: 'b'})

print(d[2])   #  default   , default value for key 2 is returned i.e. "default"


#  userlist : It is a class which can be used to create a list which can be modified by user , it is a list which can be modified by user
class my_custom_list(collections.UserList):

    def my_first_element(self):      # method to return first element of list , custom method
        print("my_first_element :", self[0])



l = my_custom_list([1,2,3])

print("userlist :", l)   # [1, 2, 3]

l.my_first_element()   # my_first_element : 1   , from above class 



# ------------------------------------------------------------------------------------------------------------------------------------------

#  using ZIP            , can be used to transpose matrix if n*n size

# zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in
#          each passed iterator are paired together etc.
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

a = [1,2,3,4,5]
b = [6,7,8,9,10 , 78 , 4785]
c = [11,12,13,14]

z = zip(a,b,c)   # only 4 items are paired together cause minimum number of items in the iterators i.e. c has only 4 items

#  2 methods to access the zip object value

for i in z:     # using iterator returned by zip  , once value iterated it get removed from zip object
    print("i =",i)

print(list(z))  # using list function to convert zip object to list 

s = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

z = zip(*s)
print(list(z))



# map()
# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable 
# map(fun, iter)

# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.
def double(n):
    return n + n
m = map(double , [1,2,3,4,5] )  # it passes iterable values to function as parameter

print(list(m))


# filter(): Returns all elements of an iterable for which a function is true.

f = filter(lambda n: n%2 != 0 , [1,2,3,4,5,6,7,8,9,10])       # fun , iter

print(list(f))