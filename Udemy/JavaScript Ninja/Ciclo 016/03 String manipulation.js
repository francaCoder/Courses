(function() {

    console.log("Matheus".length)

    let name = new String("Matheus")
    console.log(name.length)
// Length - Count the characters

/*
 CharAt
 Wich is the letter in that index
*/

console.log("Matheus".charAt(0))
console.log("Matheus".charAt(1))

// Concat

console.log("Matheus".concat("  França"))

/*
IndexOf (    Too we have the lastIndexOf    )
If exist, he return the index, else return '-1'
*/

console.log("Matheus".indexOf("t"))
console.log("Matheus".indexOf("z"))
console.log("Matheus".indexOf("heus"))
console.log("Matheus".indexOf("heos"))


// Replace - Change

console.log("Matheus".replace("a", "o"))
// Motheus 

// Slice - First index last index

console.log("Matheus".slice(3))
/* 
If i pass just 1 parameter, he will return the phrase from this index, but if i pass 2 parameters, he will return the phrase from of first index to second index
*/

// Split - He braks the phrase according to your parameter

console.log("Matheus".split("a"))
console.log("Fernando".split("n"))

let fruit = "Bonono"
let breakes = fruit.split("o")
let join = breakes.join("a") 
console.log(join)


// Substring

console.log("Matheus".substring(2))
console.log("Matheus".substring(2, 4))

// Upper and Lower

console.log("Matheus".toLowerCase())
console.log("Matheus".toUpperCase())

// And If  i want let just the first letter in lower case?

let upper = "EXEMPLE"
console.log(upper.charAt(0).toLowerCase(), upper.slice(1))




})() 