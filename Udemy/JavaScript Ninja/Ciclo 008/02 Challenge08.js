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

/* Create a literal function called "calculator", that work like this:
- The function must receives a parameters that will say how mathematical operation she will use. ('+  -  *  /  %)
- This function must return a second function that will make the following:
- Must receives two parameters 
- This two parameters will be the operators used in mathematical operation
- The return of that second function is the complete operation, whith the phrase:
"The result of operation: [number1] [operator] [number2] = [Result]"
- If the operator don't be valid, return the phrase:
"Invalid operation"
*/

function calculator(operator) {
    return function(number1, number2){
        let result 
        switch (operator) {
            case "+":
                result = number1 + number2
                break;
            case "-":
                result = number1 - number2
                break;
            case "*":
                result = number1 * number2
                break;
            case "/":
                result = number1 / number2
                break;
            case "%":
                result = number1 % number2
                break;
                default:
                return "Invalid operation"
                break;
        }
        return `The result of operation: ${number1} ${operator} ${number2} = ${result}`
    }
}

/* Declare a variable called "sum", that will receives the function above, passing how parameter the operatos of sum*/

let sum = calculator("+")

// Now, sum is a function. Show in console the sum of two numbers using she.

console.log(sum(7,8))

/* Now, declare same variables whith the names: "subtraction", "Multiplication", "division" and "mod", and assign to her the function "calculator", passing the correct operator per parameter for each one them*/

let subtraction = calculator("-")
let multiplication = calculator("*")
let division = calculator("/")
let module = calculator("%")

// Make an operation whith each of the functions created above, showing the result in console
console.log(subtraction(5, 2))
console.log(multiplication(20, 5))
console.log(division(15, 3))
console.log(module(50, 10))
