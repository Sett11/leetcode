const w={'0':'zero','1': 'one',
'2': 'two',
'3': 'three',
'4': 'four',
'5': 'five',
'6': 'six',
'7': 'seven',
'8': 'eight',
'9': 'nine'}
const o={
  '1': 'one',
  '2': 'two',
  '3': 'three',
  '4': 'four',
  '5': 'five',
  '6': 'six',
  '7': 'seven',
  '8': 'eight',
  '9': 'nine',
  '10': 'ten',
  '11': 'eleven',
  '12': 'twelve',
  '13': 'thirteen',
  '14': 'fourteen',
  '15': 'fifteen',
  '16': 'sixteen',
  '17': 'seventeen',
  '18': 'eighteen',
  '19': 'nineteen',
  '20': 'twenty',
  '30': 'thirty',
  '40': 'forty',
  '50': 'fifty',
  '60': 'sixty',
  '70': 'seventy',
  '80': 'eighty',
  '90': 'ninety',
  '100': 'hundred',
  '1000': 'thousand',
  '1000000':'million',
  '1000000000':'billion',
  '1000000000000':'trillion',
  '1000000000000000':'quadrillion'
}
const k={
  one: '1',
  two: '2',
  three: '3',
  four: '4',
  five: '5',
  six: '6',
  seven: '7',
  eight: '8',
  nine: '9',
  ten: '10',
  eleven: '11',
  twelve: '12',
  thirteen: '13',
  fourteen: '14',
  fifteen: '15',
  sixteen: '16',
  seventeen: '17',
  eighteen: '18',
  nineteen: '19',
  twenty: '20',
  thirty: '30',
  forty: '40',
  fifty: '50',
  sixty: '60',
  seventy: '70',
  eighty: '80',
  ninety: '90',
  hundred: '100',
  thousand: '1000',
  million: '1000000',
  billion: '1000000000',
  trillion: '1000000000000',
  quadrillion: '1000000000000000'
}
const f=n=>{
  const a=Object.entries(o).reverse().map(e=>[+e[0],e[1]]),r=[]
  for(let i=-1;++i<a.length;){
    let t=[]
    while(n>=a[i][0]&&n)n-=a[i][0],t.push(a[i][1])
    if(t.length)r.push([t.length,t[0]])
  }
  return r
}
function numberToWords(n,q=Number.isInteger(n),z=0,m=0){
if(w[n+''])return w[n+''][0].toUpperCase()+w[n+''].slice(1)
n=Math.abs(n)
if(!q){
  n=(n).toFixed(5)
  z=n.slice(0,n.indexOf('.'))
  m=[...n.slice(n.indexOf('.')+1)].map(e=>w[e])
  while(m[m.length-1]==='zero')m=m.slice(0,m.length-1)
  m=m.join` `
  n=+z
}
let r=f(n),a=['hundred','thousand','million','billion']
for(let i=-1;++i<r.length;){
  if(a.includes(r[i][1]))r[i][0]=f(r[i][0])
  else r[i].splice(0,1)
}
let res=r.flat(2).map(e=>Array.isArray(e)&&a.includes(e[1])?[o[e[0]],e[1]]:Array.isArray(e)?e[1]:e).flat()
res=res.map(e=>e[0].toUpperCase()+e.slice(1)).join` `
return !q?res+' point '+m:res
}

console.log(numberToWords(1234567))
console.log(numberToWords(0))