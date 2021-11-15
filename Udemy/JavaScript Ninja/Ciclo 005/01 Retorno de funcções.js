/*
so far we use the sames types of return, but  the return can return another things, as a array....objects...
I can create a object inside scope of my function, don't need be in global scope.
*/

function myFunction() {
    return [1, 2, 3]
}

console.log(myFunction())
// I can, for exemple, take diferents index of my array and after make the manipulation
console.log(myFunction()[1])

let exemple = myFunction()[2]
console.log(exemple)

// Inside a function, i can put properties, after i can make that one future variable empty, recive one propertie that was my function