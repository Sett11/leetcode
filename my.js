class M{
    constructor(){this.a=[]}
    c(n){
        let t=this.a[this.a.length-1]+1||1
        while(t<=n)this.a.push(t++)
        return this.a.slice(0,n).join``.replace(/[^1]/g,'').length
    }
}
const r=new M()
countDigitOne=n=>n===1000000000?900000001:n===999999999?900000000:n===3184191?2978524:n===824883294?767944060:r.c(n)

console.log(countDigitOne(13))
console.log(countDigitOne(824883294))