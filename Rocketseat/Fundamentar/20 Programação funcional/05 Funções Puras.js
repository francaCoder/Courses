/*
    A diferença é que não irá modificar nenhum dado e não vai guardar nenhum estado
*/

// Função impura

function calculate(radius) {
    // Ela é impura pois depende da biblioteca que está no escopo global. Seria pura se recebesse o Math como argumento
    return Math.PI * (radius + radius)
}

// ex 2: Alterando um dado externo
// Impura
let person = {
    name: "Matheus França",
    age: 19
}

function changeName(name) {
    person.name = name
}

changeName("Carlin")

// Função pura
// ex 1 

const calculateCircum = function(pi, radius) {
    return pi * (radius + radius)
}

// ex 2

const changeCircumf = (pi, radius) => pi * (radius + radius)

// ex 3
const changePersonName = (person, name) => ({...person, name})