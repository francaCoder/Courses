(function () {
    'use strict'

    /* 
    Array-like
    Looks lika an array, have the same structure but isn't an array
    */


    function myFunction(a, b, c) {
        console.log(arguments)
        // If i put argumets.forEach() - Is not a function
    } 

    console.log(myFunction(1, 2, 3, 4, 5, 6))


    function newFunction() {
        Array.prototype.forEach.call(arguments, function(item, index) {
            console.log(item)
        })
    }
    console.log(newFunction(1,2,3,4,5,6))



















})()