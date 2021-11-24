(function(){

// Involve all code in this file in one IIFE

/* 
Create a variable called "once", that receive "False" how your value.
Create a loop that execute while this variable are truthy. Inside loop, show in console the message:
"Entered at least once  (entered at list uonce - Entrou pelo menos uma vez)"
How loop you must use for that this message will be shown in console?
*/

let once = false

do { // First he execute and after verify
    console.log("Entered at list once")
} while (once === true);

/* 
Create a object called "Person", that receive the foollowing properties:
"Name", "Age", "Weight" and "Birthday". Complete with the correct values for the name, age, weight and birth date
*/

let person = {
    Name: "Matheus França",
    Age: 18,
    Weight: 84,
    Birthday: "20/07",
}

/* 
Use a loop for sweep the object created above, showing in console the phrase:
"The [PROPERTY] of person is [VALUE]"
Enjoy and create a variable "counter" that will count how much properties have this object.
Before loop, show the phrase:
"The person has [COUNTER] properties"
*/
var counter = 0
for (const propertie in person) {
    counter++ // For each propertie add 1 for counter
    console.log(`The ${propertie} of person is ${person[propertie]}`)
}

console.log(`The person has ${counter} properties`)

/* 
Create a function called "moreThan", that will verify if the person (Created above) is older that the age passed per parameter.
IF true, return the message in console:
"The person has more than 25 years old?"
*/

function moreThan(age) {
   return person.age > age ? true : false
}

console.log(`The person has more than 25 years? old ? ${moreThan(25)}`)

/* 
Create a loop among 0 at 20, that add each number how one element of an array called "Numbers". If the counter is geater than 10, leave the loop. Show in console the numbers in array
*/

// before
let Numbers = []

let newCounter = 0 // Counter has already been declared
while (newCounter < 21) {
    if (newCounter > 10) {
        break;
    }
    Numbers.push(newCounter)
    ++newCounter
/*
OR 

    for (let newCounter = 0; newCounter < 20; newCounter++) {
    if (newCounter > 10) {
        break;
    }
    numbers.push(newCounter)
*/

}

console.log(Numbers)

/* 
Make another loop among 0 at 20, that add to an array called "newNumbers" (already created above, but need be restarting). If number === pair jump for next number 
Show in console the numbers of array
*/

let newNumbers = []
    
    for (let number = 0; number < 21; number++) {
        if (number % 2 === 0) { // !== 0 is odd    <1 is pair > 0 is odd
            continue;
        }
        newNumbers.push(number)
    }
    
console.log(newNumbers)
})()