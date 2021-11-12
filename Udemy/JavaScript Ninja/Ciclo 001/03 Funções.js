// É um bloco de código que pode ser chamado com ()


var x = 1
function soma() {
    x += 1
}

soma()
console.log(x)

soma()
console.log(x)

// Podemos reutilizar funções a qualquer momento, é só chamar ela


function escopo() {
    let nome = "Matheus França"
    return nome // Podem retornar valores 
}

console.log(nome) // Não conseguimos acessar o que está dentro do escopo da function



// Podem receber argumentos e parâmetros
function soma(x, y){ // Parâmetros
    return x + y
}

console.log(soma(1, 2)) // Argumentos