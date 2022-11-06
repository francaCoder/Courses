const express = require("express") // Vai criar um servidor para mostrar tudo o que a gente ta construindo dentro do navegador

// instanciar o express 
const app = express()

// falando para o express que vamos usar o ejs
// Estamos falando para o express que a nossa view engine (ferramenta que vamos usar para renderizar o html) vamos usar o ejs para isso
app.set("view engine", "ejs")

// vamos criar uma rota
app.get("/", function(req, res) {
    const items = [
        {
            tittle: "D", 
            message: "esenvolvedor aplicações/serviços de forma fácil"
        },

        {
            tittle: "E", 
            message: "JS usa JS para renderizar HTML"
        },

        {
            tittle: "M", 
            message: "uito fácilde usar"
        },

        {
            tittle: "A", 
            message: "morzinho"
        },

        {
            tittle: "I", 
            message: "nstall EJS"
        },

        {
            tittle: "S", 
            message: "intaxe simples"
        }
    ]

    const subtitle = "Uma linguagem de modelagem para criação de páginas HTML usando JS"
    res.render("pages/index", {
        qualitys: items,
        subtitle: subtitle
    })
    // Esse res.render já espera que tenhamos uma pasta chamada views e que tenha um index.ejs dentro dela
    // O pages e o partials é para separar e organizar o que é a página e quais são os arquivos de layout que a gente vai usando
    // Os arquivos ejs aceitam que a gente passe objetos para eles, e estamos passando o items que criamos acima
})

app.get("/sobre", function(req, res) {
    res.render("pages/about")
})

app.listen(8081)

console.log("Servidor funcionando")