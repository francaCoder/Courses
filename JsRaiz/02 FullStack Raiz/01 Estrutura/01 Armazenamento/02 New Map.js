// Nova estrutura
// Ama das que eu vou mais utilizar provavelmente
// Vantagens em relação à objetos e arrays

// Uma forma de estruturar dados
// Assim como objetos também utiliza pares de elementos (propriedade e valor)
// Aceita praticamente todos os tipos primitivos como chave
// Mantém a ordem dos elementos adicionados
// Acessa um valor rapidamente assim como nos objetos
// Saber o tamanho do map usando o size
// método próprio para deletar uma propriedade
// Clear para limpar todos os objetos do map

// O map não tem um "símbolo literal" como o do array ou objetos = [] / {}
// Você precisa declarar sua variável atribuindo um new map

const user = new Map([
    // Entradas
    // Chave - valor
    [0, "Programador"],
    [1, "a"],
    [2, "Bordo"]
])
console.log(user)
// Devolve um map com 3 elementos e mostra o valor de cada chave

// Ou posso instanciar um novo map e depois ir adicionando propriedades com o set

const mapa = new Map
mapa.set(0, "Programador")
mapa.set(1, "a")
mapa.set(2, "Bordo")
// mapa.set({}, "teste")
const obj = {}
mapa.set(obj, "teste")

console.log(mapa)

// Como acessar os valores dentro do mapa
// Ele tem o método prórpio para acesso (get)
// Porém eu tenho a necessidade de saber o nome da chave

console.log(mapa.get(2))
// console.log(mapa.get({})) - undefined
// O parâmetro passado no set é diferente do que foi passado agora no get
console.log(mapa.get(obj)) // teste
// Passagem por referência


// Tamanho do mapa
console.log(mapa.size)

// Difereça do size - length

const arr = []
arr[50] = "teste"
console.log(arr.length) //51

mapa.set(50, "altura")
console.log(mapa.size) //5
// Mapa não é uma lista indexada e o valor 50 foi entendido como chave

// Outros métodos do map
/*
    has
    delete
    clear
    forEach
    keys
    values
    entries
*/

console.log(mapa.has(50)) // true
mapa.delete(50)
console.log(mapa)
// mapa.clear()

console.log()
mapa.forEach((value, element) => {
    console.log(`${value} → ${element}`)
});

// Podemos iterar também usando o forOf

console.log()
for (const element of mapa) {
    console.log(element)
    // chave - valor
}

// e posso fazer a desestruturação
console.log()
for (const [key, value] of mapa) {
    console.log(`${key} →→→ ${value}`)
}

// Keys
console.log()
console.log(mapa.keys()) // { 0, 1, 2, {} }

// Criar um array com as keys do mapa
console.log()
console.log(Array.from(mapa.keys()))

// Outra forma de fazer um array é utilizando o spread

console.log([...mapa.keys()])

// Iterando as chaves ou valores
console.log()
for (const k of mapa.keys()) {
    console.log(k)
}

console.log(mapa.entries())

// new Map
const users = new Map([
    [0, {name: "Matheus", country: "Brazil"}], 
    [1, {name: "Lulu se liga", country: "EUA"}], 
    [2, {name: "tots", country: "Australia"}]
])

// Quero filtrar meu mapa para que ele retorne apenas os usuários que moram no Brasil
// O mapa não tem método prórpio para filtro, portanto vamos transformá-lo em array para filtrar

// Crie um array a partir das entradas do Users e filtre os usuários onde no index 1 de entrada (country) é igual a Brazil. E por fim faça um new Map disso.
const brazilianUsers = Array.from(
    users.entries()).filter(user => {
        return user[1].country === "Brazil"
})

const newUsers = new Map(brazilianUsers)
console.log(newUsers)

