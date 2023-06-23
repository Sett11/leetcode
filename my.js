class M{
    constructor(){
        this.s=''
        this.k=0
    }
    c(n){
        let t=this.k+1
        while(t<=n)this.s+=(t++ +'').replace(/[^1]/g,''),this.k=t
        return this.s.length
    }
}
const r=new M()
countDigitOne=n=>r.c(n)

console.log(countDigitOne(13))
console.log(countDigitOne(824883294))