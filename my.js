const map = function(a,f){
    r=[]
    a.forEach((e,i)=>r.push(f(e,i)))
    return r
}

console.log(map([1,2,3,4],e=>e+1))