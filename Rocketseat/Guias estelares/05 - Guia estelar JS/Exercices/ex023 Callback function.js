// Callback function

/*
function sayMyName(name) {
    console.log(name)
}

sayMyName("Matheus frança")
*/

function sayMyName(name) {
    console.log(name)
}

sayMyName(() => {
    console.log("Estou em uma callback")
})

// Callback é uma função passada para outra em forma de parâmetro
// O terimnal do VS code nos mostra que isso retorna uma função, mas no console conseguimos ver o que está dentro dela também

function demonstrando(animal) {
    console.log("Antes de chamar o animal")
    animal()
    console.log("Depois de chamar o animal")
}

demonstrando(() => {
    console.log("Leão")
})