function sum() {
    return 1 + 2
}

console.log(sum())

//OR

let sum2 = function() {
    return 2+ 3
}

console.log(sum2())
// Now, sum2 it is a function, so i too can run the function using sum()

let sum3 = function otherSum(){
    return 3 + 4
}

console.log(sum3)
console.log(otherSum()) // Is not defined, was assign to sum3

// I can run a function that don't have name, only if she is inside of any object or be IIFE

// I transform she in exmpression using (..........)

(function() {
    return 1 +2
}) ()
console.log(sum)

// When i use the IIFE - immediately invoked function expression, i don't need have a global scope
// How much smaller your scope, is best for worked