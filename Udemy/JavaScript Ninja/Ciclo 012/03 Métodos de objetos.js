// Object.keys(obj)
let obj = { x: 1, y: 2 }
let obj2 = { x: 2}
let obj3 = {}

console.log(Object.keys(obj)) // Will return an array with properties of 'obj'

// If i can count how much properties have in any object:
Object.keys(obj).length

// I can use 'lenght' because now, he is an array

// If i want know if any object was inherit of another object

obj.isPrototype(obj2)
// The 'obj2' was inherit of main object?   // True

JSON.stringify(obj) // Will transform my object in 'Strings"
// JavaScriptObjectNotation

console.log(obj)

JSON.parse(obj) // Will transform my 'object string' in object again

// Stringify and Parse are Conversors