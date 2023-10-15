const filter = function (a, f) {
  r = [];
  a.forEach((e, i) => (f(e, i) ? r.push(e) : null));
  return r;
};

console.log(filter([1, 2, 3, 4], (e) => e > 2));
