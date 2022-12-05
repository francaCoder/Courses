/*
    Ao menos um argumento
    Deverá retornar algo
    Nada que acontecer dentro do escopo dela afeta o escopo externo
    dados imutáveis
    não guardar estado
    não faremos uso de loops
*/

const radom = (number, Math) => Math.floor(Math.random() * number)

// recursão
// achar o fatorial do número

const factorial =  x => {
    if (x === 0) {
        return 1
    }

    return x * factorial(x-1)
    // ele devolve o valor fazendo loops chamando a função novamente passando o novo valor de x
}