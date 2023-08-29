longestPalindrome=s=>{
    let a=[]
    for(let i=-1;++i<s.length;){
        for(let j=i;++j<=s.length;){
            let t=s.slice(i,j)
            if(t===[...t].reverse().join``)a.push(t)
        }
    }
    return a.sort((a,b)=>b.length-a.length)[0]
}

console.log(longestPalindrome('babad'))
console.log(longestPalindrome('cbbd'))