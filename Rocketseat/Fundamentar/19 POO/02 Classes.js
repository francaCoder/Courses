/*
    É um molde para objetos, os objetos são criados a partir dads classes.

    Ex: máquina de biscoito
    A máquina de biscoito é a classe, nela você coloca todos os ingredientes e no final recebe o biscoito, que é o seu objeto

    No JS a sua classe já herda muitas outras propriedades
*/

class Pessoa {
    constructor(nome) {
        this.id = ~~(Math.random() * 100000)
        this.nome = nome
    }

    dizerNome() {
        console.log(this.nome)
    }
}

const pessoa = new Pessoa("Matheus")

console.log(pessoa)