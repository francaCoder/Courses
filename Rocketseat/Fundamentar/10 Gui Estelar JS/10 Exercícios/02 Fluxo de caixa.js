/* Crie um objeto que possuirá 2 propriedades, ambas do tipo array:
    receitas: []
    despesas: []

Agora, crie uma função que irá calcular o total de receitas e despesas, e irá mostrar uma mensagem se a família está com saldo positivo ou negativo, seguido do valor do saldo
*/

const rendaFamiliar = {
    receitas: [1000, 2000, 3000],
    despesas: [3000, 2000, 2000]
}

function calcularRenda(renda) {
    totalEntrada = 0
    totalSaida = 0

    for (const value of renda.receitas) {
        totalEntrada += value
    }

    for (const value of renda.despesas) {
        totalSaida += value
    }

    console.log(`Renda da Família:
    Entrada: R$${totalEntrada}
    Despesas: R$${totalSaida}
    `)
    if (totalEntrada > totalSaida) {
        console.log(`A família teve mais receita do que despesas e pagaram todas as contas. Ainda sobraram R$${totalEntrada - totalSaida}`)
    } else if (totalEntrada == totalSaida) {
        console.log(`Tanto a entrada quanto as despesas da família foram iguais. Não sobrou dinheiro mas todas as despesas foram pagas. 0 x 0`)

    } else {
        console.log(`A despesa da família foi maior que a receita. Estão com o saldo negativo de R$${totalEntrada - totalSaida}`)
    }

}

calcularRenda(rendaFamiliar)