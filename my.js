twoSum=(a,k)=>{
    for(let i=-1;++i<a.length;)for(let j=i;++j<a.length;)if(a[i]+a[j]===k)return [i+1,j+1]
}

console.log(twoSum([ 2 , 7 ,11,15],9))