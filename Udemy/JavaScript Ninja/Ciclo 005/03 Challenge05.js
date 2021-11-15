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
Create a function called 'book', that recieve one parameter, that be the name of 'book'. Inside this function, declare one variable that recieve a object whit the ollowing characteristics:
- This object will recieve 3 properties , that be names of books
- Each one properties, will be a new object, that have another 3 properties
    - HowMuchPages - Number
    - Author
    - PublishingCompany
- The fuction must retrun the object referent to book past in parameter
- IF the parameter don't be past, the function must return the object whith all books
*/