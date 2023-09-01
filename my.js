largestNumber=(n,a=[...Math.abs(n)+''])=>a.sort((a,b)=>(a+''+b)-(b+''+a))

console.log(largestNumber(310))
console.log(largestNumber(-3799649188))