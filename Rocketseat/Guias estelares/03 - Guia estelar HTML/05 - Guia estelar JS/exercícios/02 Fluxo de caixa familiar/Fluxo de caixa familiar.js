/* 
Crie um objeto que possuirá 2 propriedades, ambas do tipo array:
    * Ativos: []
    * Passivos: []
    
Agora crie uma função que irá calcular o total de ativos e passivos e irá mostrar uma mensagem se a família está com saldo positivo ou negativo, seguido do valor so saldo
*/


let caixa = {
    ativos: [100.156, 500.5289, 480, 90],
    passivos: [44, 885, 20]
}

function sum(array) {
    let total = 0

    for (const value of array) {  
        total += value
    }
    return total 
}

function calculateBalance() {
    const calculateAtivos = sum(caixa.ativos)
    const calculatePassivos = sum(caixa.passivos)

    const total = calculateAtivos - calculatePassivos

    const itsOk = total >=0

    let balanceText = "negativo"

    if (itsOk) {
        balanceText = "positivo"
    }
    console.log(`Seu saldo é ${balanceText}: R$${total.toFixed(2)}`)
}
calculateBalance()