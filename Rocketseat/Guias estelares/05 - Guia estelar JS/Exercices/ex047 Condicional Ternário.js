// Dependendo da condição, nós receberemos valores diferentes

// Condição - Se sim valor 1 se não valor 2
// condition? value1 : value2

// Exemplos
// Objetivo: café da manhã top
let pao = true
let queijo = false

const niceBreakFast = pao && queijo ? "Café top" : "Café ruim"
console.log(niceBreakFast)

// É a condição do && que nos retorna true or false

let age = 16
const canDrive = age >= 18 ? "can Drive" : "Cant't drive"
console.log(canDrive)