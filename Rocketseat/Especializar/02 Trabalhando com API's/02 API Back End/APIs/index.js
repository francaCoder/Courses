// Quero no navegador, quando eu digitar localhost:3000, que ele abra o que estamos programando

const express = require('express')
const app = express()

// Listen fica ouvindo o navegador, e quando entramos na porta 3000 ele vai jogar lá pra dentro o que a gente quiser
app.listen("3000")

// Vamos criar as rotas para o navegador mostrar

// Get - requisição e response
// app.route("/").get((req, res) => {
//     res.send("Helooo")
// })

// app.route("/sobre").get((req, res) => {
//     res.send("Helooo sobre")
// })

// Midleware - ponte do insomnia pra cá
// app.use(express.json())

// // Post - req - conteúdo da requisição
// app.route("/").post((req, res) => {
//     res.send(req.body)
// })

// Put
// let author = "Matheus"

// app.use(express.json())

// app.route("/").put((req, res) => {
//     author = req.body
//     res.send(author)
// })

// Delete

// let author = "Matheus"

// app.route("/:id").delete((req, res) => {
//     res.send(req.params.id)
// })

// Parâmetros na requisição são formas da gente passar informações que não estavam lá antes

// app.route("/").get((req, res) => res.send(req.query.name))

// app.route("/").post((req, res) => res.send(req.body))

// app.route("/:parametro").get((req, res) => res.send(req.params.parametro))


// Body params
// midleware - vai transformar o que está chegando na api em JSON

// app.use(express.json())

// app.route("/").post((req, res) => {
//     // console.log(req.body)
//     // console.log(req.body.nome)
//     // console.log(req.body.livros[1])

//     const {nome, cidade, livros} = req.body
//     console.log(`Meu nome é ${nome}, moro em ${cidade} e meu livro preferido é o ${livros[1]}`)
    
// })


// Route params
// app.route("/").get((req, res) => res.send("olá"))

// Independente do que eu escreva depois da / , vai virar uma variável no meu código chamada nome
// app.route("/:nome").get((req, res) => res.send(req.params.nome))

// app.route("/identidade/:nome").get((req, res) => res.send(req.params.nome))


// quey params - ?
// Eu basicamente crio propriedades e valores direto na url
// ?nome=...&cidade=...&age=...
app.route("/").get((req, res) => res.send(req.query))

app.route("/about/user").get((req, res) => res.send(req.query))