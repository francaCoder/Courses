let cor = "yellow"
cor = "red"

const newCor = "Blue"
// newCor = "Black"

// Em objetos

const cart = {
    quantity: 2,
    total: 200
}

// cart.quantity = 3   BAD ↓
// (Não entendi porque que não pode) 

// Good ↑
// ... se lê expalhar, é como se fosse o super() em classes/construtores, puxa tudo o que tem no objeto anterior
const newCart = {...cart, quantity: 3}


// ReactJS
const [amount, setAmount] = useState(0)

// amount = 2  Bad

setAmount(2) // GOod

