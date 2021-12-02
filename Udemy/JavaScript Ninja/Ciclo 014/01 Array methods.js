// Reduce

let array = [ 1, 2, 3, 4, 5]
let reduce = array.reduce(function (accumulated, current, x, y) {
    return accumulated + current
}, 0)
/*
1ª - 0 + 1 = 1
2ª - 1 + 2 = 3
3ª - 3 + 3 = 6
4ª - 6  + 4 = 10
5ª - 10 + 5 = 15
*/
console.log(reduce)

let myName = ["M", "a", "t", "h", "e", "u", "s"]
let newReduce = myName.reduce(function(accumulated, current, x, y) {
    return accumulated + current
})

console.log(newReduce)
