function tabuada() {
    let num = window.document.getElementById("txtn")
    let tab = window.document.getElementById("seltab")
    if (num.value.length == 0) {
       window.alert("Por favor, Digite um número.")
    } else {
        let n = Number(num.value) 
        let c = 1
        tab.innerHTML = "" // Antes de mostrar a tabuada limpe ela
        while (c <= 10) { // Enquanto C for menor que .... crie uma opção. Esse número representa o valor máximo da tabuada
            let item = document.createElement("option")
            item.text = `${n} x ${c} = ${n*c}` // Seleciona o que tem dentro do item
            item.value = `tab${c}`
            tab.appendChild(item) // Adiciona um item filho
            c++ // Incremento
        }
    }
}