function memoize(f) {
  const o = {};
  return function (...a) {
    let c = typeof a === "number" ? a + "" : a.join`,`,
      r = null;
    if (c in o) return o[c];
    r = f(...a);
    o[c] = r;
    return o[c];
  };
}

let callCount = 0;
let c = 0;
const memoizedFn = memoize(function (a, b) {
  callCount += 1;
  return a + b;
});

console.log(memoizedFn(2, 3));
console.log(memoizedFn(2, 3));

function f(x) {
  c += 1;
  return x <= 1 ? 1 : f(x - 1) + f(x - 2);
}

q = memoize(f);

console.log(q(9));
console.log(q(9));
console.log(callCount);

console.log(c);
