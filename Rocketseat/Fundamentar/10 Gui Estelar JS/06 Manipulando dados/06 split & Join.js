// Manipulando Strings e Arrays

// Separe um texto que contém espaços, em um novo array onde cada palavra é uma posição do array. Depois disso, transforme o array em um texto e onde eram espaços coloque _

let phrase = "Eu quero viver o amor"

// O split recebe como argumento, o que eu quero usar para separar a minha frase, no caso o escolhido foi "espaço", e automaticamente já salva esses valores em um array que cada posição é uma palavra
let myArray = phrase.split(" ")
console.log(myArray)

// Colocando underline
// Usamos o join para juntar os elementos conforme o argumento que eu passei para ele
console.log(myArray.join("_"))