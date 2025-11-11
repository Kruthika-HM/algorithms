def dnf(array):
    low=0
    mid=0
    high=len(array)-1
    while mid<=high:
        if array[mid]==0:
            array[low],array[mid]=array[mid],array[low]
            low+=1
            mid+=1
        elif array [mid]==1:
            mid+=1
        else:
            array[mid],array[high]=array[high],array[mid]
            high-=1
    return array
array=[2,0,1,2,0,1]
result=dnf(array)
print(result)