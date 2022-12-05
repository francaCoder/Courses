/*
    Um esqueleto de uma futura classe
    Nessa classe podem ser criadas métodos e atributos, mas não implementamos nada.

    vai explicar como outras classes serão criadas através dela
*/

// Definir

class Parafuso { // Superclasse - abastrata
    constructor() {
        if (this.constructor === Parafuso) {
            throw new Error("Classe abstrata não pode ser instânciada")
        }
    }
    get tipo() {
        throw new Error("Método 'get tipo()' precisa ser implementado")
    }
}

class Fenda extends Parafuso {
    constructor() { super() }

    get tipo() {
        return "fenda"
    }
}

class Philips extends Parafuso {
    constructor() { super () }

    get tipo() {
        return "philips"
    }
}

class Allen extends Parafuso {}

// new Parafuso()
let fenda = new Fenda()
let philips = new Philips()
let allen = new Allen()

console.log(fenda.tipo, philips.tipo)
