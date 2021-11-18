function myFunc() {
    function sum() {
        return 1 + 2
    }
    return sum()
}

// I can't run sum() whithout myFunc

function exemple() {
    let result = 0
    return result
}

console.log(result)
// Result is not defined, because it is inside function
// Also i can create a new variable called result outside the function, because she is different of the variable that it is inside function

function myFunction() {
    let number1 = 1
    let number2 = 2
    return sum()
    function sum(){
        return number1 + number2
    }
}
// When i run this function, will an error happen? Let's find out
// Doesn't happen, because was maked a hoisting