// Manipulando arrays

let techs = ["html" ,"css" ,"js"]


//Adicionar um item no fim
console.log(techs.push("nodejs")) 
//Adicionar um item no começo
techs.unshift("sql")
//Remover do fim
techs.pop()
//Remover do começo
techs.shift()
//Pegar somente alguns elementos do array
        //console.log(techs.slice(1, 3))
//Remover 1 ou + itens em qualquer posição do array 
        //console.log(techs.splice(1, 1))
//Encontrar a posição de um elemento no array 
let index = techs.indexOf("css")
console.log(index)


console.log(techs)

/*
push - fim
unshift - começo
pop - remove do fim, e é só os () vazios mesmo
shift - remove do começo, e é só os () vazios mesmo
slice - fatiar - Passar como argumento o elemento inicial e o final do array que você quer que ele tire. A primeira contagem começa do 0 e a segunda começa do 1 
splice - Qual index do array eu quero remover e quantos a partir dele que eu quero tirar também. Também recebe dois argumentos
indexOF - Qual é o index de... Aí no parâmetro a gente passa o elemento que ta dentro do array pra gente saber a posição dele
*/



// Remover Alguma coisa do array facilmente 
let newArray = [
    "carro",
    "moto",
    "ônibus",
    "bicicleta",
    "Caminhão",
]

let remover = newArray.indexOf("carro")
newArray.splice(remover, 1)

console.log(newArray)