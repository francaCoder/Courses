function showTicket(user: string, ticket: number) {
    console.log(`Olá ${user ?? "Usuário padrão"}, seu número de bilhete é ${ticket}`)
}

showTicket("Matheus", 5)

// ?? = É nulo? então faça...