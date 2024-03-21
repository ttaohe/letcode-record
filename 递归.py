
def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    def digui(s):
        if s==1:
            return 1
        if s==2:
            return 2
        return digui(s-1)+digui(s-2)
    return digui(n)

# 当递归容易超时时，用列表加递归

def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    s=[1,2]
    if n<=2:
        return s[n-1]
    while len(s)<n:
        s.append(s[-1]+s[-2])
    return s[-1]