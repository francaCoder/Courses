/*
    Principais formas de manipulação

    - Transformar
        * map
        * flat & flatmap
        * reverse
        * reduce
        * reduceRight
        * fill
    - Combinar
        * Object.assing
        * spread
        * reduce
        * reduceRight
        * concat
    - Ordenar
        * sort
    - Filtrar
        * filter
        * reduce
        * reduceright
    - Eliminar
        * filter
        * reduce
        * reduceright
    - Localizar
        * find
        * findIndex
    - Testar
        * some
        * every
        * includes
*/

// Conversão entre tipos

//  Faça um array com ... do obj
// Object.keys(obj)
// Object.values(obj)
// Object.entries(obj)
// Object.fromEntries(arr)

// Obj → Array

const obj = {name: "Matheus", age: 19}

console.log("keys")
console.log(Object.keys(obj))

// console.log("values")
// console.log(Object.values(obj))

// console.log("Entries")
// console.log(Object.entries(obj))

// Array → Obj
// Pega os arrays com chave/valor e transforma em objeto
console.log(Object.fromEntries(Object.entries(obj)))


// Temos um objeto que queremos transformar em map
// map precisamos passar arrays de chave e valor

const map1 = new Map(Object.entries(obj))
console.log(map1)

console.log(map1.get("name")) 


{ // Invert object
    const raceResults = {
        first: "Matheus",
        second: "Jake",
        third: "Matheus"
    }

    function invertObj(obj) {
         return Object.fromEntries(Object.entries(obj).map(entry => {
            return[entry[1], entry[0]]
        }))
    }

    console.log(invertObj(raceResults))

    // Peguei um objeto, transformei em array invertendo as posições e depois transformei eu objeto novamente
}

{
    const raceResultsByFirstName = {
        first: "Alice",
        second: "Jake",
        third: "Alice"
    }

    function invert(obj) {
        return Object.entries(obj).reduce(function(acc, current) {
            return({
                // Vou retornar um objeto acumulando o resultado do current anterior
                ...acc, [current[1]]: [...(acc[current[1]] || []), current[0]]
            })
        }, {})
    }

    console.log(invert(raceResultsByFirstName))

    // Transformo em array para ter mais possibilidades de tratamento e depois eu transformo de volta para objeto com um array de entradas
}