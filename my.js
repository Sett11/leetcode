const sortBy = (arr, fn) => arr.sort((a,b)=>fn(a)-fn(b))

console.log(sortBy([1,2,3,4,5],x=>-x))
 