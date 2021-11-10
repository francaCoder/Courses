
let user = "admin"

// Cada expressão precisa ter um Break, se não da erro
switch (user) {
    case "Estagiário": 
        console.log("Novato")
        break;

    case "Operador":
    console.log("Intermediário")
        break;

    case "admin":
    console.log("Chefe")
    default:
        console.log("Insira um cargo que seja válido")
        break;
}
