/* Tipagem explícita
    Ex: falar que o parâmetro da função é : number ou : string....

    h
*/

function showTicket(user, ticket) {
    console.log(`Olá ${user ?? "Usuário padrão"}, seu número de bilhete é ${ticket}`)
}

showTicket("Matheus", 5)

// ?? = É nulo? então faça...