# 二分查找模版
def binarySearch (arr, l, r, x): 
            mid = l + (r-l)//2
            if r>=l:
                if arr[mid]==x:
                    return mid
                elif arr[mid]>x:
                    return binarySearch(arr, l, mid-1, x)
                elif arr[mid]<x:
                    return binarySearch(arr, mid+1, r, x)
            else:
                return mid+1