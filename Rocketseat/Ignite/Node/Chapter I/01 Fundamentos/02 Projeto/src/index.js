// chamando o express
const express = require("express")

// renomeando
const app = express()

// middleware
app.use(express.json())

// definir a porta que o nosso node vai rodar (localhost:3333)
app.listen(3333)

// Podemos usar o nodemon para fazer a atualização automática e não ter que parar o nosso servidor a cada alteração no código

// get
app.get("/", (req, res) => {
    // O método send vai nor permitir mandar uma mensagem pra quem está fazendo a solicitação por essa rota
    // return res.send("hello World")
    return res.json({message: "hello world"})
})

app.get("/ignite", (req, res) => {
    // return res.send("hello world → ignite")
    return res.json({
        message: "Hello world 😁",
        page: "Ignite"
    })
})

app.get("/courses", (req, res) => {
    // Rota para cursos disponíveis
    const query = req.query
    console.log(query)
    return res.json(["curso1", "curso2", "curso3"])
})

// post 
app.post("/courses", (req, res) => {
    // Queremos adicionar o curso 4
    const body = req.body
    console.log(body)
    return res.json(["curso1", "curso2", "curso3", "curso4"])
})

app.put("/courses/:id", (req, res) => {
    const params = req.params
    console.log(params)
    return res.json(["curso6", "curso2", "curso3", "curso4"])
})

app.patch("/courses/:id", (req, res) => {
    return res.json(["curso6", "curso7", "curso3", "curso4"])
})

app.delete("/courses/:id", (req, res) => {
    return res.json(["curso6", "curso2", "curso4"])
})