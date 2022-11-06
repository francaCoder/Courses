
sayMayName() // Primeiro eu executei e depois eu criei a função

// Será que vai acontecer o hoisting? - Sim

function sayMayName() {
    console.log("Alguma coisa")
}

// 2 exemplo

digaMeuNome()

var digaMeuNome = function() {
    console.log("Matheus")
}

// var digaMeuNome

// digaMeuNome() - is not a function

// digaMeuNome = function() {
    // console.log("Matheus")
// }

// não sofre elevação e dá erro, aparece que ela não é uma função