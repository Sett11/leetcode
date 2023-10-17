const once = function(f){
  let c=1
	return function(...a){
        return c--===1?f(...a):undefined
    }
}


let fn = (a,b,c) => (a + b + c)
 let onceFn = once(fn)

  console.log(onceFn(1,2,3))
  console.log(onceFn(2,3,6))
 