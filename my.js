findSecondMinimumValue=t=>[...new Set(JSON.stringify(t).replace(/[^\d:]/g,'').replace(/:/g,' ').split` `.filter(e=>e).map(e=>+e).sort((a,b)=>a-b))][1]||-1

console.log(findSecondMinimumValue({
    v: 5,
    c: [
        {
            v:10,
            c: [
                {
                    v:11,
                }
            ]
        },
        {
            v:7,
            c: [
                {
                    v:5,
                    c: [
                        {
                            v:1
                        }
                    ]
                }
            ]
        }
    ]
}
))