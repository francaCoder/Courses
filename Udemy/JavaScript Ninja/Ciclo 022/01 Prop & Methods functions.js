(function () {
    'use strict'


    // Today we go to study properties and methos of functions.


    // .Length - Say how much parameters this function receive
    function myFucntion(a, b, c) { }
    console.log(myFucntion.length) // 3


    /*
     .toString
    When i use this method with an array, he is converted for String and separeted for comma
    */

    let array = [1, 2, 3, 4]
    console.log(array.toString())

    /* Whe i use .toString with function....*/
    function newFunction(a, b, c) { }
    console.log(newFunction.toString())

    // She is showed in the literal format


    /* 
    Call
    He serves for run some function, but i can pass per parameter who will be the 'this' of that function
    */

    function whoIsThis() {
        console.log(this.lastName)
    }

    let object = {
        name: "Matheus",
        lastName: "França"
    }

    let object2 = {
        lastName: "Silva"
    }

    whoIsThis.call(object2)
    /* 
    This change according to name passed inside call

    1 - França
    2 - Silva

    The same function can return differents 'last names'
    */


    function sumNumbers() {
        console.log(this.n1 + this.n2)
    }

    let obj = {
        n1: 5,
        n2: 6
    }

    let obj2 = {
        n1: 7,
        n2: 8
    }

    sumNumbers.call(obj)



    // I also can use call passing the 'this' and others arguments


    function test(a, b, c, d) {
        console.log(this.lastName, a, b, c, d)
    }

    test.call(test, 1, 2, 3)



    // Now i can pass per parameter the elements of an array

    function receiveElements(a, b, c, d) {
        console.log(this.lastName, a, b, c, d)
    }

    let arr = [1, 2, 3, 4]
    receiveElements.apply(object, arr)

})()