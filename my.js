largestNumber=a=>a.sort((a,b)=>(b+''+a)-(a+''+b)).join``.replace(/^0+$/,'0')

console.log(largestNumber([0,0]))
console.log(largestNumber([1000,999,808,89700]))