// Funções recebem qualquer tipo de dado

function imprimirDado(dado) {
    console.log(dado())
}

// imprimirDado(1)
// imprimirDado("Texto")
// imprimirDado({nome: "Matheus"})

// E também posso passar uma função

imprimirDado(function() {
    return "Olá mundo"
})