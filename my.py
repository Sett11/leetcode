class Solution:
    def convertTemperature(self,n):
        return [round(n+273.15,5),round(n*1.80+32,5)]
    
s=Solution()

print(s.convertTemperature(36.50))