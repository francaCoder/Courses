// 2 Valores booleanos, quando verificados , irá retornar para nós : True or false

let pao = true
let queijo = true 

// AND - &&
// No meu café da manhã precisa ter pão E queijo, não adianta ser só 1
console.log(pao && queijo)

// Se uma das variáveis fosse "False", o console iria colocar false, pois precisa ser os dois


// OR - ||
let leite = true
let suco = false
console.log(leite || suco)
// No meu café, precisa ter leite OU suco
// Isso significa que, se eu tiver apenas um desses, já ta bom.
// Por esse motivo o Console coloca true nesse caso


// NOT !
console.log(!leite)

// Se você nega uma coisa ela inverte o valor, no caso se tornou "False"