// Estrutura de repetição For - Para

for(let i = 0; i <= 10; i++){
    console.log(i)

    // Para cada loop o i tem um incremento e passa a receber um novo valor, começando com o valor inicial de o como foi estabelecido no primeiro parâmetro dentro dos parenteses do for 
}


for(let i = 10; i > 0; i-- ) {
    if (i === 5) {
        continue;    // Pula a execuçao do momento
    }

    console.log(i)
}