// Slice

let myArray = [1, 2, 3, 4, 5]
console.log(myArray.slice(1)) 
// Return the elements from the number passed per parameter until the last number of array or until the next number passed per parameter.       He don't show the second number, put one more

// Splice - Remove from the number passed per parameter

console.log(myArray.splice(3))
console.log(myArray)

let newArray = [1, 2, 3, 4, 5, 6, 7]
// From index 1 I want remove 3 elements
newArray.splice(1, 3)
console.log(newArray)

// From index 1 I don't want remove anyone element, but i want add a new element
newArray.splice(1, 0, "a", "b", "c", "d")
console.log(newArray)

// If after i want remove this 4 new itens
/*
newArray.splice(1, 4)
console.log(newArray)

OR
*/

// After 1 I want remove a,b,c,d and add 2, 3, 4
newArray.splice(1, 4, 2, 3, 4)
console.log(newArray)