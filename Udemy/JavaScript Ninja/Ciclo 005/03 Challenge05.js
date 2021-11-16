/* 
Make any variable, that recieve a array whith random values. More of 5
*/
let exemple = [1, 26, 78, 500, 18]

// Create a function that recieve a array as parameter, and return this array

function returnArray(arr) {
    return arr
}

//  Print the second index of array returned by function created above 

console.log(returnArray(exemple)[1])

//  Create a function that recieve 2 parameters: The first, one array of values, and the second, one index. The function must return a index of array that was past in the  first paramete. The index to be returned, must be the first number past in the second parameter.

function person(arr, index) {
    return arr [index]
}

let myArray = ["ninja", 52.4, true, [1,2, "frança"], {b: 2}]

// Run the fucntion  created above, and make returned all values of last array.

myArray.forEach(index => {
    console.log(index)
    index++
});

// or

for (let index of myArray) {
    console.log(index)
    index++
}

/* 
Create a function called 'book', that recieve one parameter, that be the name of 'book'. Inside this function, declare one variable that recieve an object whith the following characteristics:
- This object will recieve 3 properties , that be names of books
- Each one properties, will be a new object, that have another 3 properties
    - HowMuchPages - Number
    - Author
    - PublishingCompany
- The fuction must retrun the object referent to book past in parameter
- IF the parameter don't be past, the function must return the object whith all books
*/

function book(nameOfBook) {
    let books = {
        "father Rich Father Poor": {
            howMuchPages: 186,
            author: "Robert Kiyosaki",
            publisher: "Warner Business Books",           
        },
       "Work 4 Hours A Week": {
            howMuchPages:	416,
            author: "Timothy Ferriss",
            publisher: "Crown Publishing Group",
        },
        "Think And Grow Rich": {
            howMuchPages: 	336,
            author: "Napoleon Hill",
            publisher: "The Ralston Society",
        },
    }

    /* if (!NameOfBook) {
        return books
    } 

    return books [NameOfBook] */

    return !nameOfBook ? books : books [nameOfBook]
}

// Using the function created above, print the object whith all books

console.log(book()) // Just i run this function without no perameter

/* Print how much pages of any book, using the phrase:
"The book [NameOfBook] have [x] pages." */

let nameOfBook = "Work 4 Hours A Week"
console.log(`The book ${nameOfBook} have ${book(nameOfBook).howMuchPages}pages.`)

/* Print the name of author of any book, using the phrase
"The author of book [nameOfBook] is [Author]" */

console.log(`The author of ${nameOfBook} is ${book(nameOfBook).author}`)
// I need put the book before that 'nameOfBook'

/* Print the name of publisher of any book, using the phrase:
"The book [nameOfBook] was published BY (pela )the publisher [nameOfPublisher]"*/
let nameOfPublisher = book(nameOfBook).publisher
console.log(`The book ${nameOfBook} was published by the publisher ${nameOfPublisher}`)
// Or i could have written 'book(nameOfBook).publisher' inside the second placeholder