// Vai criar um loop a partir de alguma variável que nós previamente tivermos 

let name = "França"
let names = ["matheus", "João", "Pedro"]

for(let charactere of name){
    console.log(charactere)  
    // A cada loop ele pegou uma letra do valor de name e imprimiu, e eu defini que cada letra seria acessada por "charactere"
}

for(let name of names){
    console.log(name) // O name nesse caso serão os elementos dentro do array
}