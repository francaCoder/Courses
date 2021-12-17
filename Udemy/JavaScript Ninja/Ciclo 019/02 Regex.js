/*
Methods that we can use:
- Match()
- Replace()
- Split()
- Search
*/

let CPF = "111.222.333-44"

// If i want break everything that isn't a number and after leave just them inside of array.

console.log(CPF.split(/\D/)) 


// Search

console.log(CPF.search(/\./))

// He will sweep the string, and will return the index of  the element that i asked

console.log(CPF.indexOf("."))