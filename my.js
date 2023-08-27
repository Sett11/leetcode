twoSum=(a,b)=>{
    for(let i=-1;++i<a.length;)for(let j=-1;++j<a.length;)if(a[i]+a[j]===b&&i!==j)return [i,j]
}

console.log(twoSum([2,7,11,15],9))