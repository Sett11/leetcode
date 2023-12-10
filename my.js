const checkIfInstanceOf = (o, c) => {
  const a = Object.getOwnPropertyNames(o.__proto__),
    b = new c()
  return Object.getOwnPropertyNames(b.__proto__).join`` === a.join``
}

console.log(checkIfInstanceOf(5, Number))