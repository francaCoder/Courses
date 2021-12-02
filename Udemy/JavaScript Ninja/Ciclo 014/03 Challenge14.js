(function () {

/* 
Create an array called 'numberObjects'. This array must have 10 elements. Each element will be an object with the following characteristics:
- { number: [NUMBER]}
- The numbers must be among 1 at 10
 - After show the array
*/

let numberObjects = []

for (let index = 0; index < 11; index++) {
    numberObjects.push({ Number: index})
}
// console.log(numberObjects)

/*
Create an array called 'justNumbers', that will have how elements just the numbers of array created above
*/

let justNumbers = numberObjects.map(function(element) {
    return element.Number
})
console.log(justNumbers)

/* 
create an array called 'justMod2Or3', that will receive of array created above just the numbers that be division per 2 or 3. Show this array in console
*/

let justMod2Or3 = justNumbers.filter(function(element) {
    return element % 2 === 0 || element % 3 === 0
})

console.log(justMod2Or3)

/*
Declare a variable called 'operation' that receive a value of array created above reduced of the following operation:
- Add 1 to last value returned
- Multiply the result of the current value
The calculation must start from 0
*/

let operation = justMod2Or3.reduce(function (accumulated, current) {
    return (accumulated + 1) * current
}, 0)

console.log(operation)

/* 
Make the same sum passed above, but start from last element. And assign the result to variable called 'operation2'.
*/

let operation2 = justMod2Or3.reduceRight(function(accumulated, current) {
    return (accumulated + 1) * current
}, 0)

console.log(operation2)

/* 
Create an array called 'name'. Each element these array must be a syllable of your name. Let's reduce this array. Joining all syllables, but using the lenguage of "p"
*/

let name = ["Ma", "the", "us"]
let reduced = name.reduce(function(accumulated, current) {
    return accumulated + "P" + current
}, "")

console.log(reduced)

/*
let newName = ["Ma", "the", "us"]
let reduced = "P" + newName.join("P")

console.log(reduced)
*/

/*
Create a variable called "inverseName", that will reduce the array in one String, and will return your inverse name
*/

let inverseName = name.reduceRight(function(accumulated, current) {
    return accumulated + current
})

console.log(inverseName)

/* 
Show in console numberObjects
*/

console.log(numberObjects)

/* 
Check if exists in any index of 'numberObjects', one object equal a 'Number: 2'. If exists, show him in console:
- " Exists an object [object] in numberObjects"
Else, show the phrase:
- "Don't exists an object [object] in numberObjects"
*/

let object = numberObjects[1]
if(numberObjects.indexOf(object) > -1) {
    console.log(` Exists an object {Number: 2} in numberObjects`)
} else {
    console.log( `Don't exists an object {Number: 2} in numberObjects`
    )
}

/* 
Now make the same exercise starting of last and cerify if { Number: 2 } exists, from index 2
*/

if(numberObjects.lastIndexOf(object, 2) > -1) {
    console.log(` Exists an object {Number: 2} in numberObjects`)
} else {
    console.log( `Don't exists an object {Number: 2} in numberObjects`
    )
}

/* 
Verify if 'justMod2Or3' is an array. 
*/

if (Array.isArray(justMod2Or3)) {
    console.log(justMod2Or3.toString())
}

})()

