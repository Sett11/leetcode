Array.prototype.last=function(){return !this.length?-1:this[this.length-1]}

console.log([1,2,3].last())
console.log([0].last())