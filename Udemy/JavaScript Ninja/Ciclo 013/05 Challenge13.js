(function(){
/* 
Involve all code in one IIFE

 Create an array and show in console the representation in 'String' of that array, using the method seen in class 13
*/
let array = [1, 2, 3]
console.log( array.toString())

})()

/* 
Create 2 arrays, 'south' and 'south east', that will be the regions of Brazil. Each array must have the states of that region.
*/

let south = ["RS", "SC", "PR", ]
let southEast = ["SP","ES", "RJ", "MG"]

/* 
Create a variable called 'Brazil' that will have receive both (as duas) regions concatenated. After show 'Brazil' in console.
*/

let Brazil = south.concat(southEast)
console.log(`Any states of Brazil: ${Brazil.join(", ")}`)

/*
Add 3 new states of  northeast region at first of array and show in console (UNSHIFT)
*/

Brazil.unshift("BA", "RN", "SE")
console.log(`Any states of Brazil: ${Brazil.join(", ")}`)

/* 
Remove the first state of array and after show him in console
*/

let removed = Brazil.shift()
console.log(`This state was remove: ${removed}`)

/* 
Create a new array called "newSouth", that receive only southern states, taking of 'Brazil' array. Dont remove this elements of 'Brazil', and afer show in console
*/

// let newSouth = [Brazil[2], Brazil[3], Brazil[4],]
// OR
let newSouth = Brazil.slice(2, 5) 
// The 5 he don't show
console.log(newSouth)

/* 
Create a new array called "North" and put yours states
*/

let north = ["AM", "AChg", "ROmgh", "RR", "PA", "AP", "TO"]

/* 
Remove of 'Brazil'  the states of 'southEast', and after put them in a variable called 'newSouthEast'
*/

let newSouthEast = Brazil.splice(5, 4)
// From 5 i want remove 4
console.log(newSouthEast)

/* 
Add the states of  'north' to 'Brazil' array. These states must stay in the same level that the states that already exist
*/

Brazil = Brazil.concat(north)
console.log(`Any states of Brazil: ${Brazil.join(", ")}`)

/*
Using forEach, sweep the 'Brazil' array and generate a new array called 'newBrazil'. This array must have each element how an object, with the properties:
id: Index of 'Brazil' array
state: State of Brazil array 
*/

let newBrazil = []
Brazil.forEach(function(element, index) {
    newBrazil.push({
        Id: index,
        State: element,
    })
});

console.log(newBrazil)

/* 
Sweep the 'Brazil' array and check if the states have more than 2 letters each, assign result to new variable. And change the phrases according to result
*/

console.log(Brazil)

let howMuchLetters 
let some = Brazil.some(function(element) {
    return element.length > 2
})

// i was think better use 'some' than 'every'

console.log(some ? 
    "We have any state with more than 2 letters." 
    : "We don't have states whith more than 2 letters.")

/*
Sweep the 'Brazil' array and chack if "CE" be include, assign the result to variable. Change the phrase according to result
*/

let newSome = Brazil.some(function(element) {
    return element === "CE"
})

console.log(newSome ? 
    "'CE' be include." :
    "'CE' not exist."
    )

/* 
Sweep the array 'newBrazil'  and create a new array that sum 1 in ID of each element these array, and add the following phrase a "State":
"[State] belongs to Brazil"
Assing the new array to one variable called 'map'
*/

let map = newBrazil.map(function(element, index) {
    return {
    ID: element.id + 1,
    State: element.State + " belongs to Brazil"
    }
})

console.log(map)

/* 
Filter the array created above, returning the states that have ID pair and after assign the value for a variable called 'filter'
*/

let filter = map.filter(function(element, index) {
    return element.ID % 2 === 0
})

console.log(filter)
