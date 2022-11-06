// stdout - vai escrever alguma coisa de saída
// saída padrão do processo

// process.stdout.write("Alguma coisa")

/*
    \n - quebra de linha (new line)
*/

const questions = [
    "O que aprendi hoje?",
    "O que me deixou aborrecido?",
    "O que eu poderia fazer para melhorar?",
    "O que me deixou feliz hoje?",
    "Quantas pessoas ajudei hoje?"
]

const ask = (index = 0) => {
    process.stdout.write("\n\n" + questions[index] + " → ")
}

ask()

const answers = [

]

process.stdin.on("data", data => {
    answers.push(data.toString().trim() + "\n")

    if (answers.length < questions.length) {
        ask(answers.length) // esse agora já roda como 1, o prox 2, e assim sucessivamente
    } else {
        console.log(answers)
        process.exit() // vai fechar o processo após escrever o primeiro dado
    }
})

process.on("exit", () => {
    console.log(`
        Bacana França

        O que você aprendeu hoje foi:
        ${answers[0]}

        O que te aborreceu foi:
        ${answers[1]}

        O Que você poderia melhorar foi:
        ${answers[2]}

        O que te deixou feliz hoje:
        ${answers[3]}

        Você ajudou ${answers[4]} pessoas hoje.

        Volta amanhã para novas reflexões
    `)
})

// on() - vai ficar atento aos eventos e a alguma coisa que tiver acontecendo
// data - quando tiver dados ele vai ficar ouvindo e toda vez que for inserido dados ele vai rodar uma função
// Essa função será rodada todas as vezes que for inseridos dados no processo

// Retorno das respostas

// [
//     'Aprendi a organizar a str de pergunta\n',
//     'hm..acho que não gostei do jeito do app\n',
//     'sla\n',
//     'estou aprendendo nodeJs\n',
//     'qts tiverem assistindo a esse vídeo\n'
// ]
