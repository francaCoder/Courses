(function(){
// Involve all code in this file with one IIFE

/* 
Create an object called "Person" with the properties:
name: String
surName: String
age: Number

Complete each property with yours personal datas, respect the type of value for each property
*/

let person = {
    name: "Matheus",
    surName: "França", 
    age: 18,
}

/*
 Show in console, in an array , all properties of object created above. Don't use nothing repeating structure and don't create the array manually
*/

console.log(Object.keys(person))

// Create an empty array called 'books'

let books = []

/* 
Add insine array 3 objects, that will be 3 name of books. Each book must have the following properties:
Titles and Pages
*/

books.push({title: "the secrets of the millionaire mind", pages: "100"})
books.push({title: "The man more rich of Babylon", pages: "150"})
books.push({title: "Father Rich, Father Poor", pages: "200"})

console.log(books)

// Remove the last book and after show him in console

console.log(books.pop())

// Show in console the restant books

console.log(books[0], books[1]) // Or just console.log(books)

// Convert the objects os books for Strings

        // console.log(JSON.stringify(books)) 

// Convert again for objects

        // console.log(JSON.parse(books))

/* Show in console all properties and values in the format below:
"[PROPERTY]: [VALUE] "
*/

for (let index = 0; index < Object.keys(books).length; index++) { // Sweep array
    // While it's smaller the number of books
        for (const property in books[index]) { // Sweep properties
            console.log(`${property}: ${books[index][property]}`)
                
        }
}

})()


/* 
Create an array called 'myName'. Each element of array must be one letter of your name. Add your full name in array
*/

let myName = ["m", "a", "t", "h", "e", "u" ,"s"]

// Joining all elements of array, show in console your name

console.log(myName.join(""))

// Show in console your name on the contrary

console.log(myName.reverse().join(""))

// Show all elements of array in alphabetical order

console.log(myName.sort().join(""))
