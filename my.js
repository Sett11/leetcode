const reverse=(x,t=+[...Math.abs(x)+''].reverse().join``)=>x<0&&-t>(-2)**31?-t:x>0&&t<2**31-1?t:0

console.log(reverse(123))
console.log(reverse(-123))