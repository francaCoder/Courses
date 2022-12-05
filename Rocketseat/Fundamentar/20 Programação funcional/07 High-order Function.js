/*
    Funções que recebem funções como argumentos
    Funções que poderão retornar outras funções
*/

// ex com .map()

const numbers = [2, 4, 8, 16]

const square = n => n * numbers
// Quero ter um novo array com todos os números ao quadrado

const squaredNumber = numbers.map(square)
// uooooou, eu passei uma função como argumento do .map() que itera cada elemento do array, e essa função transforma os números ao quadrado


// Currying - aplicar parcialmente as funções 
const pause = wait => fn => setTimeout(fn, wait)

const wait200 = pause(200)
const wait1000 = pause(1000)

wait200(() => console.log("Waiting 200ms"))
wait1000(() => console.log("Waiting 1s"))
