class Solution:
    def topKFrequent(self,a,n):
        s=set(a)
        a=sorted(a)
        if len(s)==len(a):
            return a[:n]
        return [j[1] for j in sorted([[a.count(i),i] for i in s],key=lambda e:(e[0],-ord(e[1][0]),-ord((e[1][0] if len(e[1])<2 else e[1][1])),-len(e)),reverse=True)[:n]]
            
    
s=Solution()

print(s.topKFrequent(["i","love","leetcode","i","love","coding"],2))
print(s.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"],4))
print(s.topKFrequent(["aaa",'aa',"a"],2))
print(s.topKFrequent(["rmrypv","zgsedk","jlmetsplg","wnfbo","hnnftqf","bxlr","sviavwoxss","jdbgvc","zddeno","rxgw","hnnftqf","hdmvplne","rlmdt","jlmetsplg","ous","rmrypv","fwxulnpit","dmhuq","rxgw","ledleb","bxlr","indbvb","ckqqibnx","cub","ijww","ehd","hfhlfqzkcn","sviavwoxss","rxgw","bxjxpfp","mgqj","oic","ptk","fwxulnpit","ijww","sviavwoxss","bgfvfa","zfkgsudxq","alkq","dmhuq","zddeno","rxgw","zgsedk","amarxpg","bgfvfa","wnfbo","sviavwoxss","sviavwoxss","alkq","nmclxk","zgsedk","bwowfvira","ous","bxlr","zddeno","rxgw","ous","wnfbo","rmrypv","sviavwoxss","ehd","zgsedk","jlmetsplg","abxvhyehv","ledleb","wnfbo","bgfvfa","bwowfvira","amarxpg","wnfbo","bwowfvira","dmhuq","ouy","bxlr","rxgw","oic","hnnftqf","ledleb","rlmdt","oldainprua","ous","ckqqibnx","dmhuq","hnnftqf","oic","jlmetsplg","ppn","amarxpg","jlgfgwb","bxlr","bwowfvira","hdmvplne","oic","ledleb","bwowfvira","oic","ptk","dmhuq","abxvhyehv","ckqqibnx","indbvb","ypzfk","rmrypv","bxjxpfp","amarxpg","dmhuq","sviavwoxss","bwowfvira","zfkgsudxq","wnfbo"],25))