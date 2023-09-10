class Solution:
    def alertNames(self,a,b):
        r=[[a[i],int(b[i][:2]+b[i][3:])] for i in range(len(a))]
        o={i:[] for i in set(a)}
        res=[]
        for i in r:
            o[i[0]].append(i[1])
        for i in o:
            o[i].sort()
            for j in range(len(o[i])-2):
                if o[i][j+2]-o[i][j]<=100:
                    res.append(i)
                    break
        return sorted(set(res))


s=Solution()

print(s.alertNames(["a","a","a","a","b","b","b","b","b","b","c","c","c","c"],["01:35","08:43","20:49","00:01","17:44","02:50","18:48","22:27","14:12","18:00","12:38","20:40","03:59","22:24"]))

print(s.alertNames(["a","a","a","a","a","b","b","b","b","b","b"],["23:20","11:09","23:30","23:02","15:28","22:57","23:40","03:43","21:55","20:38","00:19"]))