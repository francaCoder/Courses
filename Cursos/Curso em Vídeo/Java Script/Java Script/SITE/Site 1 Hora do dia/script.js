

function carregar() {
    let msg = window.document.getElementById("msg")
    let img = window.document.getElementById("imagem")
    let data = new Date()
    //let hora = data.getHours()
    var hora = 15
    msg.innerHTML = `Agora são ${hora} horas`
        if (hora >= 0 && hora < 12) {
            // Bom dia
            img.src = "1 manhã.png"
            document.body.style.background = "#e8931c"
            } else if (hora >= 12 && hora <18){
                //Boa tarde
                img.src = "2 tarde.png"
                document.body.style.background = "#7f3011"
                } else {
                    // Boa noite
                    img.src = "3 noite.png"
                    document.body.style.background ="#0b1c23"
                }
            
        }

