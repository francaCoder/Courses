// Objects are mutable (milrabow) and manipulates per reference

// I can create two objects qith the same properties

let object = {
    prop1: "prop1",
    prop2: "prop2",
}

let object2 = {
    prop1: "prop1",
    prop2: "prop2",
}

console.log(object)
console.log(object2)

// I can change properties

object.prop1 = "Black"
console.log(object)

// I can delete any propertie 

delete object2.prop2
console.log(object2)

// I can add properties 

object2.prop2 = "prop2"
console.log(object2)


// manipulates per reference

console.log(object === object2) // False

let objectCopy = object

console.log(objectCopy === object) // True
// Is equal object
// He have one reference of object

console.log(objectCopy)
objectCopy.prop1 = "Red"

console.log(object) 
// If i change any property of 'objectCopy', the 'object' changes too


// How create literals   (Literals - how constructor(new) - with object.create())

// Object is a function the return an empty object. And he have a property called 'create'

// Objects have a property called 'prototype'