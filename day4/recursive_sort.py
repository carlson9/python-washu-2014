def merge_sort(m):
    if len(m)<=1: return m
    left = m[:len(m)/2]
    right = m[len(m)/2:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    i = 0
    j = 0
    merged = []
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    if i == len(left):
        for x in range(j,len(right)):
            merged.append(right[x])
    if j == len(right):
        for y in range(i,len(left)):
            merged.append(left[y])
    return merged

