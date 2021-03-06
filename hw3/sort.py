def merge_sort(m):
    if len(m)<=1: return m
    left = m[:len(m)/2] #split the array
    right = m[len(m)/2:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    i = 0
    j = 0
    merged = []
    while i<len(left) and j<len(right): #while haven't reached end of one side
        if left[i] < right[j]: #if left is smaller append it
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    if i == len(left): #this means that the end of the left was reached, so just append the rest of the right
        for x in range(j,len(right)):
            merged.append(right[x])
    if j == len(right): #end of right was reached
        for y in range(i,len(left)):
            merged.append(left[y])
    return merged

def item_sort(m):
    output = []
    for i in range(len(m)):
        output.append(min(m)) #append the minimum
        m.remove(min(m)) #and remove it
    return output

def quicksort(myList, start, end): #borrowed from www.pythonschool.net/algorithms_quickSort/
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList

def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right
