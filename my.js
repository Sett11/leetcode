function ListNode(val, next){
    this.val=(val===undefined ? 0 : val)
    this.next=(next===undefined ? null : next)
 }

 const f=(x,a=[])=>{
    while(x){
        a.push(x.val)
        x=x.next
    }
    return BigInt(a.reverse().join``)
}
const r=(x,n=null)=>{
    return x.length===1?new ListNode(x.pop(),n):r(x,new ListNode(x.pop(),n))
}
const addTwoNumbers=(l1,l2)=>r([...(f(l1)+f(l2))+''].map(Number).reverse())

console.log(addTwoNumbers(r([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ,0,0,0,0,0,1]),r([5,6,4])))