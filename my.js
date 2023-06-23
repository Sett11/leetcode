containsNearbyAlmostDuplicate=(a,d,k)=>{
    for(let i=-1;++i<a.length;)for(let j=i;++j<a.length;)if(Math.abs(i-j)<=d&&Math.abs(a[i]-a[j])<=k)return true
    return false
}

console.log(containsNearbyAlmostDuplicate([1,2,3,1],3,0))
console.log(containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))