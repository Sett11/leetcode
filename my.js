const compose=a=>x=>a.reverse().map(e=>x=e(x)).reverse()[0]||x

f=compose([x=>x+1,x=>x**2,x=>x*2])

console.log(f(4))