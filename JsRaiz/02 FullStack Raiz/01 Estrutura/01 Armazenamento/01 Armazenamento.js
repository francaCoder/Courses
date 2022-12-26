// Estrutura de dados
// Pensar como seus dados vão ser armazenados

// Tipos primitivos

// String
const name = "Matheus"
console.log(name)

// Number
const age = 19

// Boolean
const status = true

// Array - Lista de dados dentro dele
const lista = ["arroz", "feijão", "carne"]

// Coleções - array de objetos
const users = [
    {
        id: 1,
        name: "Matheus",
        age: 19
    },

    {
        id: 2,
        name: "Ayrton",
        age: 26
    }
]

// Objeto
const user = {
    name: "Matheus",
    age: 19
}

console.log(user.name)

// Disvantagens quando precisa trabalhar em uma aplicação mais sofisticada

// Um array por exemplo tem muitas vantagens, porém a principal disvantagem é que para acessar um usuário específico dentro da coleção por exemplo, ele teria que varrer todos os dados

// Por uma arrow function passada para dentro do método find (que varre o array), retornamos o usuário que o Id é igual a 1 ou 2
console.log(users.find((user) => {
    return user.id === 2
}))

// O usuário foi achado mas a iteração sob todos os usuários teve que ser feita obrigatoriamente.
// Não consegue acessar diretamente um dado que você precisa

// Objeto nesse caso é mais vantajoso pois pode acessar direto com a propriedade específica

const newUsers = {
    "123": {id: "123", name: "Aytron"},
    "223": {id: "223", name: "José"},
}
// Acesso direto
console.log(newUsers["223"])

// Mesmo assim objetos também tem muitas limitações, array tem muito mais métodos de busca/filtro, não guardam a ordem dos dados adicionados, não sabe quantas propriedades tem no seu objeto.

users["213"] = {id: "213", name: "Maria"}
// Se eu fizer a iteração pode ser que esses dados não venham em ordem