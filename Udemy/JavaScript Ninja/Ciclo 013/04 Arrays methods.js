// Map

let array = [1, 2, 3, 4, 5]
let map = array.map(function(element) {
    return element +1
})

console.log(array , map)

// He return for we, a new array. He don't modify the main array

let object = [1, 2, 3, 4, 5]
let map2 = object.map(function(element) {
    return { index: element, element:element}
})

console.log(map2)

let newArray = []
array.forEach(function(element, index){
    newArray.push({index: index, element: element})
});

console.log(newArray)

// Filter


let bigger = [1, 2, 3, 4, 5, 6]
let filter = bigger.filter(function( element) {
    return element > 2})

// Just elements that are greater than 2
console.log(filter)