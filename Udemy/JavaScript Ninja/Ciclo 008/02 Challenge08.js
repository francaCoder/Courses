/* Declare a variable called "Sum" and assign  to her a function called "calculateSum". The function must receive two parameters and returne the sum theses parameters*/

let sum = function calculateSum(x,y){
    return x + y
}

/* Run the function created above, passing two parameters that will be added, and before show in console using the phrase: "The sum among [value1] and [value2] is [result]"*/

let value1 = 10
let value2 = 20
console.log(`The sum among ${value1} and ${value2} is ${sum(value1, value2)}`)

/* Show in console the name of funciton created above, whith the phrase:
"The name of function that make the 'sum' is [Name of Fucntion]"*/

let nameOfFunction = sum.name
console.log(`The name of function that make the sum is ${nameOfFunction}`)
// Sum just is the variable that receives the function

/* Create a literal function called "showName". This function must return your name */

/*
let person = {
    name: "Matheus",
    surName: "França",
    age: 18,
    height: 1.83,
}

function showName(person) {
    return `Your name is ${person.name} ${person.surName}`
}

console.log(showName(person))
*/

function showName() {
    return "Matheus França"
}

// Declare a variable called "letShowName" that receives a function created above

let letShowName = showName()

/* 
Using the variable created above, show in console the name and the return of function assign to her, whith the following phrase:
"The function [Name of Function] return [Return of function]"
*/

let nameOfFunc = showName.name
let returnOfFunction = showName() // Run the function for get the return
console.log(`The function ${nameOfFunc} return ${returnOfFunction}`)