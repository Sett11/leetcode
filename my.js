isEmpty = (x, y = JSON.stringify(x)) => y === "{}" || y === "[]"

console.log(isEmpty({}));
console.log(isEmpty({ x: 9 }));
