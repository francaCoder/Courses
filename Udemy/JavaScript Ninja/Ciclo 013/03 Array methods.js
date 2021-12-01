// For each
// Repeating structure

let myArray = [ 1, 2, 3, 4, 5, 6, 7]

myArray.forEach(element => {  // For each element, show the element
    console.log(element)
});

// I can pass 3 parameters (item, index and array)


let sum = [1, 2, 3, 4, 5, 6, 7]
let total = 0

sum.forEach(element => {
    total += element
});

console.log(total)

// total receive the sum of array


// Every

let newArray = [1, 2, 3, 4, 5, 6, 7]
let every = newArray.every(function(element){
    return element < 5
}) 

console.log(every)
// If  an element is false, he will return 'false'


// Some
let array = [1, 2, 3, 4, 5, 6, 7]
let some = array.some(function(element) {
    return element % 2 === 0
})

console.log(some)
// If an element is true, he will return 'true'