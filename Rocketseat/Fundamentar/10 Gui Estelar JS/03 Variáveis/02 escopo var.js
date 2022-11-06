
    // Escopo Determina a visibilidade de alguma variável no javascript

// bloco
{
    let x = 0
    console.log(x)
}

// o var é global e também local, pode funcionar fora de um escopo de bloco


console.log("Existe x antes do bloco?", a)

{
    var a = 4
}

console.log("Existe x depois do bloco?", a)