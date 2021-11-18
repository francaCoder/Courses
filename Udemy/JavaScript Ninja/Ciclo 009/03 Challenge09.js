/*
Create an IIFE that involve all code in this file. Make so the correct indentation in code, for to stay inside a IIFE

Analyze the functions below, ('myFunction', 'myFunction2' ande 'myFunction3'), and adjust the position of variables and internal functions, for codes within the console that are returning 'undefined' return the correct value of variable or called function
*/

function myFunction() {
    let number1 = 10
    let number2 = 20
    console.log(`In function 'myFunction', the first number is ${number1}`)
    console.log(`In function 'myFunction', the second number is ${number2}`)
    
    return number1 + number2
    
}
myFunction()

// myFunction2

function myFunction2() {
    let number1 = 10
    let number2 = 20
    let sum = function sum() {
    return number1 + number2
    }
    console.log(`The sum of 10 and 20 is equal ${sum ? sum() : undefined}`)
    return sum()
}
console.log(myFunction2())

// myFunction3
function myFunction3() {

    let number1 = 40
    let number2 = 50    
    function sum() {
        return number1 + number2
    }
    console.log(`The sum of 40 and 50 is equal ${sum()}`)
    console.log(`In function myFunction3, number1 is equal ${number1}`)
    
    return sum()
}

myFunction3()

/* 
In the previous challenge, we create a calculator, using the functional structure. Now, lets create another calculator, using otherwise( de outra forma):
- Create a function 'calculator' that receive 2 values of type numbers per parameter 
- This function must retrun another function, that receive 1 parameter called 'callback'
- Callback will be a function, that we will past per parameter to run the return of calculator
- The return of that  second function, must are a function of 'callback', passed per parameter, RUN, and passing to him per parameter 2 values that were(foram) passed for the first function 'calculator'
*/

function calculator(number1, number2) {
    return function(callback) {
        return callback(number1, number2)
        // The return of callback is the own (próprio - oum) callback, but that accept 2 numbers
    }
}

/* 
Declare a variable called 'sum', ang assign to him the function 'calculator', passing 2 numbers per parameter
*/

let sum = calculator(25, 52)

/* 
We know that 'sum' now have a function assign to him, that is the return of 'calculator'. And this function wait a parameter 'calback'. The 'callback' have two parameters available (disponíveis - Évélabol), that are was passed for the call from ''calculator' above.

Show in console the return of invocation of 'sum', passing per parameter a anonymous function that will return the sum of 2 numbers that this anonymous function have how your arguments
*/

console.log("The result of sum is:")
console.log(sum(function(number1, number2){
    return number1 + number2
}))

