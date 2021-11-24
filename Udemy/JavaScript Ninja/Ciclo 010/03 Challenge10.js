(function(){
    // Create a IIFE that involves all in this file, ALL, and make the correct indentation

    /* 
    Without changing the codes in console.log below, make with that the their (deles)return be true, using the wrappers Objects with "Conversors" in values of the variables. Analyze of what is printed in console, for know how solve (resolver) the problem
    */

    let five = Number("5") // Wrapper object
    console.log(five + " Its number?", typeof five === "number")

    let concat = String(10) + 10 
    // When you transform any think in "String" and vefore use the operator +, the JS joins (junta) the two
    console.log("" + concat + "' é uma String? E é igual a '1010'?", typeof concat === "string")

})()

/* Going back to exemeple of calculator, lets use one more functional approach (Abordagem), but this time, separating some responsibles:
First - Create a object called "operation", that will have the properties: 
+  -  *  /  and   %
- Each propertie will receives function, so they will be methods, and this function will receive 2 parameters and will return the operation referent your propertie, using valeus pasts per parameter
*/

let operation = {
    "+": function(num1, num2) {
        return num1 + num2
    },
    "-": function(num1, num2) {
        return num1 - num2
    },
    "*": function(num1, num2) {
        return num1 * num2
    },
    "/": function(num1, num2) {
        return num1 / num2
    },
    "%": function(num1, num2) {
        return num1 % num2
    },
}

/* Create a function called "isOperatorValid", that will receive one operator per parameter
This function will be respinsible per verify if the operator past per parameter is valid
- IF are anyone of these above , she must return "True" or "False"
- In the challenge, we don't use Switch ou If
*/


function isOperatorValid(operator) {
    return (operator === "+" || operator === "-" || operator === "*" || operator === "/" || operator === "%")
}

console.log(isOperatorValid("**"))
// In this exercise, we don't need use "IF", because "operator === "..."  is boolean, he already verify "

// But, if we leave it like this, erevy time that i add a new operator, i will have that change in my object and in my function. We can verify if the operator passed per parameter exists or no inside the object, and return "True" or "False"


function isOperatorValid(operator) {
    return operation[operator] !== undefined
}

console.log(isOperatorValid("-"))
// He will verify if the operator exists inside the object
// IF he is  exist, he will be a function, boolean and true, if no, he is False


/* Now, lets create a calculator
- Create a function called "Calculator " that will receive per parameter one operator 
- IF the operator don't be valid, the function must return "False",
- IF the operator is valid, must return another function that will receive 2 parameters 
- IF any aprameter don't be a number, also return false
- Else, return the method of the object "operation" created above, based on operator passed for the function "Calculator", and passing for this method the two parameters of the function of return of "Calculator"
*/

function calculator(operator) {
    if (!isOperatorValid(operator)) { // If false
        return false
    }
    return function(num1, num2) {
        if (typeof num1 !== "number" || typeof num2 !== "number") {
            return false
        }
        return operation[operator](num1, num2)
    } 
}

/* 
Create a function called "showOperatorMessage" that receive tree parameters
- The operator, num1 and num2, The return of the function must be the phrase:
"The operation [num1] [operator] [num2] = [result]"
Thist function will show the message of the operation that we will create below
*/

function showOperationMessage(num1, operator, num2) {
    return `The operation ${num1} ${ operator } ${num2} is =`
}

/* 
Now, create a function called "showErrorMessage" the receive one parameter, the operator of calculator, when the operation don't be valid, this function must return the phrase:
"Operation '[operator] not allowed" 
*/

function showErrorMessage(operator) {
    return `Operation '${operator}' not allowed`
}

/* Now,  our calculator is ready, let's make tests
Step 1 - Declare 3 variables "number1" and "number2", starting with value zero, and "operationSignal" without value for a while
*/
let number1 = 0
let number2 = 0
let operatingSignal 

/*
Step2 - Assign to her the operator "+",  and declare a variable called "sum "that receive the function "Calculator", passing per parameter the variable, that was receive the signal of the operation
*/
operatingSignal = "**"
let sum = calculator(operatingSignal)

/* 
Step 3 - Now "sum" is a function, and, if the correct signal  don't be passed for the function "calculator", sum will be "false". Sum can't be "false", and so assign to variables one number for each that will be the operands
Before this, show in console the result of the operation, passing two parameters ins console.log
- The first, will be a message of the operation (using the function created above)
- The second, the function of sum, passing two parameters 
- IF "sum" be "false", show int console the message of error
*/

if (sum !== false) {
    number1 = 15
    number2 = 8
    console.log(showOperationMessage(number1, operatingSignal, number2), sum(number1, number2) )
} else {
    console.log(showErrorMessage(operatingSignal))
}

/* 
Repeat since "step 2", with the operations of subtraction, multiplication, division and module. Create variables with names "Substraction", "multiplication", "Division" and "mod". Before pass an invalid operator for show the messageError
*/

operatingSignal = "-"
let subtraction = calculator(operatingSignal)

if (subtraction !== false) {
    number1 = 20
    number2 = 8
    console.log(showOperationMessage(number1, operatingSignal, number2), subtraction(number1, number2) )
} else {
    console.log(showErrorMessage(operatingSignal))
}

// 

operatingSignal = "*"
let multiply = calculator(operatingSignal)

if (multiply !== false) {
    number1 = 5
    number2 = 5
    console.log(showOperationMessage(number1, operatingSignal, number2), multiply(number1, number2) )
} else {
    console.log(showErrorMessage(operatingSignal))
}

//

operatingSignal = "/"
let division = calculator(operatingSignal)

if (division !== false) {
    number1 = 20
    number2 = 8
    console.log(showOperationMessage(number1, operatingSignal, number2), division(number1, number2) )
} else {
    console.log(showErrorMessage(operatingSignal))
}

//

operatingSignal = "d"
let mod = calculator(operatingSignal)

if (mod !== false) {
    number1 = 5
    number2 = 15
    console.log(showOperationMessage(number1, operatingSignal, number2), mod(number1, number2) )
} else {
    console.log(showErrorMessage(operatingSignal))
}
