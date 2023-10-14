const inorderTraversal = function*(a){
    a=a.flat(100000)
    for(let i=-1;++i<a.length;)yield a[i]
}

const g=inorderTraversal([[[6]],[1,3],[]])

console.log(g.next().value)
console.log(g.next().value)
console.log(g.next().value)
console.log(g.next().value)