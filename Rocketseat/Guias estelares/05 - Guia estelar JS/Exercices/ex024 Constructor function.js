/* 
Expressão new
Cria um objeto automaticamente
Usa this como keyword
*/

function Person(name) {
    this.name = name 
    // O this sempre vai referenciar o "França" que está lá fora nesse caso
    this.walk = function() { // Walk é uma funcionalidade
        return this.name + "está andando"
    }
}
const frança = new Person("Matheus França") 
const lucas = new Person("lucas")
console.log(frança.walk)
console.log(lucas.walk)

// Tenho uma pessoa Matheus e uma pessoa chamada joão

// Vai retornar 2 functions, que cada pessoa está andando