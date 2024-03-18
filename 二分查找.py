# 二分查找模版
# 递归写法
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
    
# 循环写法 （求算数平方根）
def binarySearch (l, r, x): 
    l, r, ans = 0, x, -1
    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans