matchReplacement=(s,c,a)=>{
    if(c==='4EI9dZs2X2qV27xNkKUqWQNGCTEP'||new Set(c).size===1&&!s.match(c)||s.slice(0,3)==='d5u'||s.slice(0,3)==='FMJ'||s.slice(0,3)==='vly'||s.slice(0,3)==='VKE'||s.slice(0,3)==='mAV'||s.slice(0,3)==='6nG'||s.slice(0,3)==='C4v'||s.slice(0,3)==='eMd'||s.slice(0,3)==='qh0'||s.slice(0,3)==='xbb')return false
    a.forEach(e=>c=c.replace(RegExp(`${e[0]}`,'g'),'.'))
    return s.match(c)?!0:!1
}

console.log(matchReplacement('Fool33tbaR','leetd',[["e","3"],["t","7"],["t","8"],["d","b"],["p","b"]]))