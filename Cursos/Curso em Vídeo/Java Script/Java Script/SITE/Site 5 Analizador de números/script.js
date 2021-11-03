let num = document.getElementById("fnum")
let lista = document.getElementById("flista")
let res = document.getElementById("res")
let valores = []

function isNumero(n) {
    if (Number(n) >= 1 && Number(n) <=100) { // Só aceite números entre 1 e 100 
        return true
    } else {
        return false
    }
}

function inLista(n, l) {
    if (l.indexOf(Number(n)) != -1 ) { // Se ele existir return true
        return true
    } else {
        return false
    }
}

function adicionar() {
    if (isNumero(num.value) && !inLista(num.value, valores)) { // Ele só vai adicionar se for um número e se não estiver na lista
        valores.push(Number(num.value))
        let item = document.createElement('option')
        item.text = `Valor ${num.value} adicionado`
        lista.appendChild(item)
        res.innerHTML = '' // Quando eu conseguir adicionar um elemento, ele tem q limpar o resultado
    } else {
        window.alert("Valor inválido ou já encontrado na lista")
    }
    num.value = ""
    num.focus() // Localização do Cursor do mouse fica no lugar certo e já limpa o "num" 
}

function finalizar() {
    if (valores.length == 0 ) {
        alert("Adicione valores antes de começar") 
    } else {
        let tot = valores.length
        let maior = valores[0]
        let menor = valores[0]
        let soma = 0
        let media = 0
        for (let pos in valores) {
            if (valores[pos] > maior)
            maior = valores[pos]
            if ( valores[pos < menor])
            menor = valores[pos]

        }
        media = soma / tot
        res.innerHTML = ''
        res.innerHTML += `<p>Ao todo, temos ${tot} números cadastrados.</p>`
        res.innerHTML += `<p>O maior valor informado foi ${maior}.</p>`
        res.innerHTML += `<p>O menor valor informado foi ${menor}.</p>`
        res.innerHTML += `<p>Somando todos os valores temos ${soma}</p>`
        res.innerHTML += `<p>A média dos valores é ${media}</p>`
    }
}