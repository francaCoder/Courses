let myArray = []

// If i can put new elements inside my array

myArray[0] = 10
myArray[10] = 1
console.log(myArray) // [10, <9 empty items>, 1]

myArray.push(40)
console.log(myArray)

// .push  Add elements at the end

// I also can remove elements at the end

myArray.pop()
console.log(myArray)

let number = myArray.pop()
console.log(number)