import restaurants from "./data/restaurants.js"
import data from "./data/restaurants.js"

// console.log(data)

// Quero criar uma aplicação que foca em cardápios e também restaurantes, vamos desaninhar os cardápios dos restaurantes mas vamos manter um vínculo para saber o restaurante de cada cardápio

// Vou usar o map porque eu quero um acesso rápido e quero manter a ordem
// Colocar como chave um id para acesso rápido
// Desaninhar a estrutura

// data é uma coleção
// new Map([
//     [chave, valor],
//     [chave, valor],
//     [chave, valor],
// ])

const restaurantes = new Map(data.map(({menus, ...restaurant}) => {
     // Para cada restaurant de data ele vai retornar um array, que são os arrays de chave e valor dentro de map

     // Com a desestruturação ele removeu a parte dos menus no restaurant
     return [restaurant.id, {...restaurant, "menus": menus.map(menu => menu.id)}]
     // Agora na propriedade dos menus, em vez de aparecer [Object] [Object], aparece o id de cada cardápio
}))


// console.log(restaurantes)
// Agora que minha base de dados está em formato de map, eu posso pegar um restaurante específico rapidamente sabendo o id dele

// console.log(restaurantes.get("..."))

// restaurantes.keys() = {
//         '8f82c745-18b8-4a03-9119-23b6b6546da8',
//         'fbd92bd8-648a-426e-8f57-8fc176342785',
//         'af237151-6c16-4e5c-a91a-942c3f479ee4',
//         'c4be049e-1eb6-430e-9917-c1dc5c97a9ed',
//         '514479a1-3f2b-4474-9094-e3a33f357dd0',
//         '324181a1-c153-47f6-a466-1ca1b0bcf707',
//         '3f231724-6def-4919-b66d-d0ec70c2045f',
//         '62e5e2ca-0e50-4b8f-8bb4-13f9ae19610b'
// }

// também vou criar uma constante para menus

const menus = new Map(data.flatMap(restaurant => {
    return restaurant.menus.map(menu => {
        return [menu.id, {...menu, "restaurantId": restaurant.id}]
    })
}))

console.log(menus)
// restaurant.menus são objetos, por isso que eu tenho que fazer um map dentro dele
/* {
    id / index / status / sections
} */
// Agora temos um map cpm o id => menus

// console.log(menus)
console.log(restaurantes.get("8f82c745-18b8-4a03-9119-23b6b6546da8"))