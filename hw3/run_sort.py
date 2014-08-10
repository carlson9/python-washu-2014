import random
from sort import *
import timeit
import pylab as py
import sys

def sort_simulator(n,iters):
    time_merge = []
    time_quick = []
    time_item = []
    for k in range(iters):
        test = random.sample(range(n),n)
        time1 = timeit.default_timer() #time before start
        merge_sort(test)
        time2 = timeit.default_timer() #time after merge_sort runs
        quicksort(test, 0, n-1)
        time3 = timeit.default_timer() #time after quicksort runs
        item_sort(test)    
        time4 = timeit.default_timer() #time after they've all run
        time_merge.append(time2 - time1)
        time_quick.append(time3 - time2)
        time_item.append(time4 - time3)
    return sum(time_merge)/len(time_merge), sum(time_item)/len(time_merge), sum(time_quick)/len(time_quick) #return the means

random.seed(1009) #for (some) reproducibility

time_merge = []
time_item = []
time_quick = []
n = 500
for i in range(2,n):
    times = sort_simulator(i,20) #run random data of size 2 - 500, 20 times and find mean
    time_merge.append(times[0])
    time_item.append(times[1])
    time_quick.append(times[2])

py.rcParams['legend.loc'] = 'best' #auto place the legend
def fig(x1,y1,x2,y2,x3,y3,label1,label2,label3):
    py.plot(x1, y1, label = label1)
    py.plot(x2, y2, label = label2)
    py.plot(x3, y3, label = label3)
    py.ylabel('average time in secs')
    py.xlabel('size of data')
    py.legend()

fig(range(2,n), time_merge, range(2,n), time_item, range(2,n), time_quick, 'merge sort', 'item sort', 'quick sort')
#py.show() #can be used instead of savefig if wish to show it in a GUI
py.savefig('sort_graph.png')


