Array.prototype.snail=function(r,c){
    if(r*c!=this.length)return []
    const a=[]
    for(let i=0;i<this.length;i+=r)a.push(this.slice(i,i+r))
    return a.map((e,i)=>i&1?e.reverse():e)[0].map((_,i)=>a.map((u,j)=>u[i]))
}

console.log([19, 10, 3, 7, 9, 8, 5, 2, 1, 17, 16, 14, 12, 18, 6, 13, 11, 20, 4, 15].snail(5,4))

console.log([1,2,3,4].snail(1,4))