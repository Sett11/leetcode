lengthOfLongestSubstring=s=>{
    if(s.length===[...new Set(s)].length)return s.length
    let a=[]
    for(let i=-1;++i<s.length;){
        for(let j=i;++j<=s.length+1;){
            let t=s.slice(i,j)
            if(t.length!==[...new Set(t)].length){
                a.push(t.slice(0,-1))
                break
            }
            if(j===s.length){
                a.push(t.slice(0,j))
                break
            }
        }
    }
    return !s||a.length==0?0:a.sort((a,b)=>b.length-a.length)[0].length
}

console.log(lengthOfLongestSubstring('abcabcbb'))
console.log(lengthOfLongestSubstring('aab'))