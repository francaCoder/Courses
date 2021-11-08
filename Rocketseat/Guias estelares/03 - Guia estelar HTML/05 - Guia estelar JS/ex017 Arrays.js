// Arrays 
/*
let animals = [
    "lion",
    "cat",
    "dog",
]
 console.log(animals)
// Como acessar valores dentro de arrays?

// Cada valor dentro do array representa uma posição, as posições começam do número 0
 console.log(animals[0])

console.log(animals.length) // O length representa comprimento, nesse código então, perguntamos o comprimento do array de animals, que no caso é 3
*/

let animals = [
    "lion",
    "cat",
    {
        name: "dog",
        age: 3,
    }
]

console.log(animals[2]) // Aqui ele mostra o objeto na posição 2
console.log(animals[2].age) // Aqui conseguimos acessar a propriedade do objeto que está dentro do array. Acessa a posição e depois a propriedade.

console.log(animals)