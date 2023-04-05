// chamando o express
const { request } = require("express")
const express = require("express")
const {v4: uuidv4} = require("uuid") // v4 gerador de números aleatórios

// renomeando
const app = express()

// middleware - insomnia → console vsCode
app.use(express.json())

// definir a porta que o nosso node vai rodar (localhost:3333)
app.listen(3333)

const customers = []


/* criar uma conta - {
    cpf: "str",
    name: "str",
    id: number, (gerado dentro da aplicação)
    statement: [] (gerado dentro da aplicação)
}
*/

// Middleware - parâmetros req, res e next
function virifyIfExistsAccountCPF(req, res, next) {
    const { cpf } = req.params

    const customer = customers.find(customer => customer.cpf === cpf)

    if (!customer) {
        return res.status(404).json({Error: "User not found"})
    }

    // Passar nosso objeto para as requisições que usam o nosso middleware
    // todas as requisições que usarem o middleware agora terão acesso ao request.customer
    request.customer = customer

    // return res.json(customer)
    return next()
}

function getBalance(statement) {
    const balance = statement.reduce((acc, operation) => {
        if (operation.type === "credit") {
            return acc + operation.amount
        } else {
            return acc - operation.amount
        }
    }, 0)

    return balance
}

app.post("/account", (req, res) => {
    // a regra de negócio deixa claro que não podemos criar uma conta com o CPF existente, então já sabemos que temos que receber um CPF
    const {cpf, name} = req.body

    // validação do CPF 
    // Sem que ser feita antes do push porque se já existir ele não adiciona no array
    // Verifica se já tem alguém com esse CPF
    const customersAlreadyExists = customers.some((customer) => customer.cpf === cpf)

    // customersAlreadyExists → True OR False

    if (customersAlreadyExists) {
        return res.status(400).json({"Error": "Customer already exists"})
    }

    // Se não der o erro ele faz o push
    customers.push({
        cpf,
        name, 
        id: uuidv4(), 
        statement: []
    })

    return res.status(201).send()
})

// buscar o extrato bancário do cliente
// route params
// app.get("/statement/:cpf", (req, res) => {
//     // destructing
//     const { cpf } = req.params
//     // tendo o cpf temos que procurar nosso cliente e retornar o statement dele

//     // Temos que buscar o extrato mas stambém temos que verificar se a conta é existente
//     const customer = customers.find(customer => customer.cpf === cpf)

//     if (!customer) {
//         return res.status(404).json({Error: "User not found"})
//     }

//     return res.json(customer)
// })

// Passando a function middleware como segundo parâmetro
app.get("/statement", virifyIfExistsAccountCPF, (req, res) => {
    // Pegando o customer
    const { customer } = req
    return res.json(customer)
})

app.post("/deposit", virifyIfExistsAccountCPF, (req, res) => {
    // O CPF sempre será passado nos headers enquanto usamos essa função para verificar se a conta existe
    // recebemos o valor do depósito e uma descrição
    const { description, amount } = req.body
    // ao receber o depósito temos que coloca-lo no array statement desse mesmo usuário

    // recuperar o customer
    const { customer } = req

    const statementOperation = {
        // Inserindo a descrição e o valor que pegamos do nosso req body
        description,
        amount,
        created_at: new Date(),
        type: "credit"
    }

    customer.statement.push(statementOperation)

    return res.status(201).send()
})

app.get("/statement/date", virifyIfExistsAccountCPF, (req, res) => {
    // Pegando o customer
    const { customer } = req
    const { date } = req.query

    const dateFormat = new Date(date + " 00:00")

    const statement = customer.statement.filter((statement) => 
    statement.created_at.toDateString() === new Date(dateFormat).toDateString())

    return res.json(customer)
})

// Atualizar os dados do cliente

app.put("/account", virifyIfExistsAccountCPF, (req, res) => {
    // permissão de alteração do nome
    const { name } = req.body
    const { customer } = req

    customer.name = name

    return res.status(201).send()
})

app.get("/account", virifyIfExistsAccountCPF, (req, res) => {
    const { customer } = req
    return res.json(customer)
})

app.delete("/account", virifyIfExistsAccountCPF, (req, res) => {
    const { customer } = req

    // splice - 2 parâmetros (início / até onde faça a remoção)
    // remover uma posição a partir do customer
    customers.splice(customer, 1)

    return res.status(200).json(customers)
})

app.get("/balance", virifyIfExistsAccountCPF, (req, res) => {
    const { customer } = req
    const balance = getBalance(customer.statement)

    return res.json(balance)
})