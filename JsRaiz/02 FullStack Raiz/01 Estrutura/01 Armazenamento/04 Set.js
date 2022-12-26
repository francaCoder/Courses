/*
    Set
        Não permite valores repetidos
        Semelhante à listas
        não tem chaves, somente valores
*/

const set = new Set([
    100, {name: "oioi"}, "hello world", true, 100
])

// Ao adicionar valores repetidos ele não adiciona o valor mas também não dá erro
console.log(set)

/*
    Métodos do set
        size
        add
        has
        delete
        values
        entries - como o set não tem chaves ele retorna o nome como se fosse os index
        forEach
*/

set.add("Matheus")
set.add(["red", "green", "blue"])
console.log(set)
console.log(set.size)

// set para mapa
const newMap = new Map(set.entries())
// Ao fazer dessa forma temos o mesmo nome para chave / valor
console.log(newMap)

// Como o set é um iterável também consiguimos transformá-lo em um array

console.log(Array.from(set.entries()))

/*
    O set permite que façamos
        União
        Interseção
        Diferença
*/

{// União
    // Quero fazer a união dos dois conjuntos pegando todos os valores sem repetir
    const conjunto1 = [1, "hello", false, 100]
    const conjunto2 = ["hello", 200, true, 1]

    const set = new Set([...conjunto1, ...conjunto2])

    console.log(set)
    // Set(6) { 1, 'hello', false, 100, 200, true }
}

{// Interseção
    // Criar um novo conjunto só com os valores em comum

    const conjunto1 = new Set([1, "hello", false, 100])

    const conjunto2 = new Set(["hello", 200, true, 1])

    const novoConjunto = new Set(
        [...conjunto1].filter(value => {
            return conjunto2.has(value)
        })
    )

    console.log(novoConjunto)
}

{ // Diferença

    const conjunto1 = new Set([1, "hello", false, 100])

    const conjunto2 = new Set(["hello", 200, true, 1])

    const novoConjunto = new Set(
        [...conjunto1].filter(value => {
            return !conjunto2.has(value)
            // Só retorna o que NÃO ! tem no conjunto 2 
        })
    )

    console.log(novoConjunto)
}

