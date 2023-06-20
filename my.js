const isMatch=(s,p)=>RegExp(`^${p}$`).test(s)

console.log(isMatch('aa','a*'))