kthSmallest=(t,k)=>JSON.stringify(t).replace(/[^\d:]/g,'').replace(/:/g,' ').split` `.filter(e=>e).map(e=>+e).sort((a,b)=>a-b)[k]

console.log(kthSmallest({
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
},
3
))