
let aceitar = true
console.log("Pedir uber")

const promessa = new Promise((resolve, reject) => {

    if (aceitar) {
        return resolve("Peedido aceito")
    } else {
        return reject("carro chegou")
    }
})

// O new Promisse com a função vazia retorna <pending>

console.log("Aguardando")

promessa.then(result => console.log(result)).catch(erro => console.log(erro)).finally(() => console.log("Finalizada"))