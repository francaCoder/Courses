/*
    Uma função que retorna um dado e esse dado vai paara outra função
*/

const people = ["Rafa", "Diego", "Dani", "Rod"]

// Dentro do filter eu paço uma função, que para cada elemento vai verificar se aquele elemento começa com D
// O filter faz a varredura igual o map
// Adicionamos o map posteriormente para aplicar uma outra função em cima desses dados que já retornou pra gente
const upperCasePeopleThatStartsWithD = people.filter(person => person.startsWith("D")).map(dperson => dperson.toUpperCase())


console.log(upperCasePeopleThatStartsWithD)