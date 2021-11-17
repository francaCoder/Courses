/* Functions are first calss objects 
everything you can do with objects, you can do whith function 

How you use literal  objects:
let car = {
    Mark: "Tesla",
    Model: "x"
}

you can create literal functions

function sum(x, y) {
    return x + y
}

a function can recieve an object
a variable can recieve an object, a function

I also return a function. For exemple:
*/

function sum(x) {
    return function(y){
        return x + y
    }
}

let add2 = sum(2)
console.log(add2(3))

//OR

console.log(sum(5)(8))


// I also can create function that receives an object and have acces to property
let car = {
    color: "Yellow"
}

function getCarColor(car) {
    return car.color
}

console.log(getCarColor(car))

// I also can pass a function as parameter