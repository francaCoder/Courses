// Condições aninhadas (uma condição dentro da outra)

let idade = 109
console.log(`Vicê tem ${idade} anos`)
    if (idade < 16) {
        console.log("não vota")
     } else if (idade < 18 || idade > 65) {
            console.log("Voto opicional")
        } else if (idade >= 18){
                console.log("voto obrigatório")
            }