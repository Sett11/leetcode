const expect = v => {
  return {
    toBe: function(e){
        if(e===v)return true
        throw Error('Not Equal')
    },
    notToBe: function(e){
        if(e!==v)return true
        throw Error('Equal')
    },
  }
}

console.log(expect(5).notToBe(5));
