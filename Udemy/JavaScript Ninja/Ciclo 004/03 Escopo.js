// Temos o escopo local e o escopo global
// Dentro / fora de uma função


// If you create a viriable inside a function, you can't using she in another momente, just inside function

let exemple = 1
console.log(exemple)

function myExemple() {
    let exemple2 = 2
    return exemple

}

console.log(myExemple())
console.log(exemple2) // I don't have accses an "Exemple2", he are inside scope function