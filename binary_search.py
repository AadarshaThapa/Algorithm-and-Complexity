import math

def binary_search(low,high,values,target):
    mid=((high -1)+low)//2
    if high-low == 0:
        return -1
      

    if target<values[mid]:
        high=mid
    return binary_search(low,high,values,target)
    elif target>values[mid]:
    low= mid+1
    return binary_search(low,high,values,target)

    elif target==mid[values]:
    return mid


    