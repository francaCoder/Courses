// Quero transformar um número quebrado com 2 casas decimais e trocar ponto por vírgula

let number = 25.991648

// toFixed(número de casas decimais)
// Replace("O que eu quero trocar", "Pelo que eu quero trocar")
console.log(number.toFixed(2).replace(".", ","))
