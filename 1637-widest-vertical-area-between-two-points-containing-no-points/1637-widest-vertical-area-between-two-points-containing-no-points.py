class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        a=[]
        p=[]
        for i in points:
            a.append(i[0])
        a.sort()
        for i in range(0,len(a)-1):
            o=a[i+1]-a[i]
            p.append(o)
        return max(p)
            
                
        