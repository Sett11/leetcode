class Solution:
    def categorizeBox(self,l,w,h,m):
        v=l*w*h>=1e9 or (l>=1e4 or w>=1e4 or h>=1e4)
        q=m>=100
        return 'Both' if v and q else 'Neither' if not v and not q else 'Bulky' if v else 'Heavy'

s=Solution()

print(s.categorizeBox(1000,35,700,300))