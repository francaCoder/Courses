/*
Expressões
Unary      number
Binary     number + number
Ternary    true ? .... : ....
*/

/*
new
left-hand-side expression
criar um novo objeto automaticamente 
*/

let name = new String("França")
let age = new Number(18)
console.log(name, age) 
// Temos um object do tipo string e um object do tipo number 

let person = new String("Person")
person.name = "Matheus"
person.surName = "França"
console.log(person.name)
console.log(person.surName)

// Podemos criar objetos e propriedades diretamente com o NEW