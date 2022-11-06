/*
    Function() constructor

    * expressão new
    * Criar um novo objeto
    * this keyword
*/

function Person(name) {
    this.name = name
}

const matheus = new Person("Matheus") 
const joao = new Person("João")
// quando eu uso o new seguido da função, essa função se torna uma função construtora
console.log(joao)

// é como se fosse um molde para criar novos objetos


let name = new String("Matheus")
console.log(name)