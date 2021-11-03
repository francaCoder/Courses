function verificar() {
    let data = new Date()
    let ano = data.getFullYear()
    let fano = window.document.getElementById("txtano")
    let res = window.document.getElementById("res")
    if (fano.value.length == 0 || Number(fano.value) > ano) {
        window.alert("[ERRO] Verfique os dados e tente novamente")
    } else {
        let fsex = window.document.getElementsByName("radsex") // [0][1] her and she
        let idade = ano - Number(fano.value)
        let genero = ''
        let img = document.createElement("img")
        img.setAttribute("id", "foto")
        if (fsex[0].checked) {
            genero = 'Homem'
            if (idade >= 0 && idade < 10) {
                //Criança
                img.setAttribute("src", "bebehomem.png") 
            } else if (idade < 21) {
                //Jovem
                img.setAttribute("src", "adolescentehomem.png")
            } else if (idade < 60) {
                //Adulto
                img.setAttribute("src", "adultohomem.png")
            } else {
                //Idoso
                img.setAttribute("src", "idoso.png")
            }
        } else if (fsex[1].checked) {
            genero = 'Mulher'
            if (idade >= 0 && idade < 10) {
                //Criança
                img.setAttribute("src", "bebemulher.png")
            } else if (idade < 21) {
                //Jovem
                img.setAttribute("src", "adolescentemulher.png")
            } else if (idade < 60) {
                //Adulto
                img.setAttribute("src", "adultamulher.png")
            } else {
                //Idoso
                img.setAttribute("src", "idosa.png")
            }
        }
        //res.style.textAlign = "center"
        res.innerHTML = `Você é ${genero} e tem ${idade} anos.`
        res.appendChild(img) // Adicionar um elemento filho de img dps do res
    }

}