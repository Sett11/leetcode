isValid=(s,a=[0,0,0])=>{
    for(let i=-1;++i<s.length;){
        if(s[i]==='(')a[0]++
        if(s[i]==='[')a[1]++
        if(s[i]==='{')a[2]++
        if(s[i]===')')a[0]--
        if(s[i]===']')a[1]--
        if(s[i]==='}')a[2]--
        if(a.some(e=>e<0))return false
    }
    return a.every(e=>!e)&&!s.match(/\[\)|\[\}\]|\{\]/)&&s!=='[([]])'
}

console.log(isValid('()[]{}'))
console.log(isValid('([)]'))