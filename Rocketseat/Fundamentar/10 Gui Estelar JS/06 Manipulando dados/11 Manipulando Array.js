
// Manipulando arrays

let techs = ["html", "css", "js"]  

// Adicionar um item no fim
techs.push("NodeJs")
// Adicionar um no começo
techs.unshift("sql")
// Remover o último item
techs.pop()
// Remover do começo
techs.shift()
// Pegar somente alguns elementos do array ("css e js")
console.log(techs.slice(1, 3)) // cortar
// Remover 1 ou mais itens em qualquer posição do array
techs.splice(1, 1) // A partir do elemento na posição x quantos vc quer tirar?
console.log(techs)
// Encontrar a posição do elemento no array
let index = techs.indexOf("html")
techs.splice(index, 1)