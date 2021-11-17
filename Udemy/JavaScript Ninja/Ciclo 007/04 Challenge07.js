// Create a array whith 5 elements

let array = [
    0, 
    "Matheus frança", 
    true, 
    5.2, 
    function returnPhrase() {
        return "Hello"
    } ]

// Create a function called "addElement", that will add element in array crated above. The function must return the array whith you new version

function addElement() {
    array.push("New element")
    return array
}

addElement()
console.log(array)

/* Add a new array to first array, whith at (wide ) least 3 diferents types of elements, before show the result in console */

let newArray = [false, null, "exemple"]

array.push(newArray)
console.log(array)

// Show in console the second element of the last array created above, whith the phrase: "The second element of second array is [ELEMENT]"

console.log(newArray[1])

// Now show in console how much elements have the second array created above, whith the phrase: "The second array have [howMuchElements] elements"

let howMuchElements = newArray.length

console.log(`The second array have ${howMuchElements} elements.`)

// Using the repition structure 'While', show in console all numbers pairs among 10 a 20

let counter = 10 // Let counter initialize from 10

while (counter <= 20) {
    if (counter % 2 > 0) {
         console.log(" ") 
    }
    console.log(counter) // Don't press F8 whithout put the last line
    counter++ // While is a repition structure, you need make a loop
}

// Whith the same idea as the exercises above, show now numbers odd
while (counter <= 20) {
    if(counter % 2 !== 0) {
        console.log(counter)
    }
    counter++
    // Counter % 2 !==0 ? console.log(counter) : console.log(" ")
}
console.log(counter)

/* Repeat the sames exercices, but now use the loop FOR
- First. show the numbers among 100 a 120
- Second. Show the numbers among 111 a 125 
*/

for (let counter = 100; counter <= 120; counter++) {
    const element = array[counter];
    counter % 2 === 0 ? console.log(counter) : console.log(" ")
}

for (let counter = 111; counter <= 125; counter++) {
    const element = array[counter];
    counter % 2 !== 0 ? console.log(counter) : console.log(" ")
}