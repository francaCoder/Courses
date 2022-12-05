// Podemos definir o tipo do retorno da função
// void - sem retorno
// Number ou string, etc

function showMessages(message: string): void {
    // Definimos que a mensagem é uma string
    // Quando um função não tem retorno ela é do tipo void
    console.log(message)
}

showMessages("teste")