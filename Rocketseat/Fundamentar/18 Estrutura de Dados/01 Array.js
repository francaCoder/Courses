const pilotos = [
    "Senna", 
    "Prost", 
    "Schumacher",
    "Hamilton"
]

console.log(pilotos[0]) // Acessar pelo index
console.log(pilotos.length) // Quantidade de elementos no array

// Iterando por loop
for (const piloto of pilotos) {
    console.log(piloto)
}

// Adicionar pilotos
pilotos.push("Alonso")

// Procurar - verificar se existe ou não
const senna = pilotos.find(piloto => piloto === "Senna")
console.log(senna)

// Agora para achar o index devemos usar o indexOF()

pilotos.splice(2, 1) // No index 2 remova 1 elemento