import random
from sort import *
import timeit
import pylab as py
import sys

def sort_simulator(n):
    test = random.sample(range(n),n)
    time1 = timeit.default_timer()
    merge_sort(test)
    time2 = timeit.default_timer()
    item_sort(test)
    time3 = timeit.default_timer()
    time_merge = time2 - time1
    time_item = time3 - time2
    return time_merge, time_item

random.seed(1009) #for (some) reproducibility

time_merge = []
time_item = []
n = 500
for i in range(1,n):
    times = sort_simulator(i)
    time_merge.append(times[0])
    time_item.append(times[1])

py.rcParams['legend.loc'] = 'best'
def fig(x1,y1,x2,y2,label1,label2):
    py.plot(x1, y1, label = label1)
    py.plot(x2, y2, label = label2)
    py.ylabel('time in secs')
    py.xlabel('size of data')
    py.legend()

fig(range(1,n), time_merge, range(1,n), time_item, 'merge sort', 'item sort')
py.show()



