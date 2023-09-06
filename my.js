deserialize=x=>JSON.parse(x)

console.log(deserialize("324"))
console.log(deserialize("[123,[456,[789]]]"))