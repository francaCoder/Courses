// Union
// Operador OU que pode fazer com que o parâmetro aceite mais de um tipo primitivo

function printUserID(id: number | string) {
    console.log(`O ID do user é ${id}`)
}

printUserID(101)