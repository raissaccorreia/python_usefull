# Python Program for recursive binary search. 
# Returns index of x in arr if present, else -1

import math

def binarySearch (arr, l, r, x): 
    if r >= l: 
        mid = math.floor(l + (r - l)/2) 
        if arr[mid] == x:
            return mid         
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x) 
        else:
            return binarySearch(arr, mid+1, r, x) 
    else:
        return -1
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 3
 
result = binarySearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print ("Element is present at index %d" %result) 
else:
    print ("Element is not present in array")
