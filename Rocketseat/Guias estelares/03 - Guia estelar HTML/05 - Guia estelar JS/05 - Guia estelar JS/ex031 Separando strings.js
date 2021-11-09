 /*
 Separe um texto que contém espaços em um novo array, onde cada texto é uma posição do array. Depois disso, transforme o array em um texto e onde eram espaços coloque _
 */

 let phrase = "Eu quero viver o amor!"
 let newArray = phrase.split(" ")
 console.log(newArray)

  // console.log(String(newArray).replace("," , "_"))      Por que nao funcionou?

let phraseWithUnderscore = newArray.join(" ") 
// Coloque dentro do parâmetro do join pelo que você quer que as palavras sejam separadas 
console.log(phraseWithUnderscore.toUpperCase())