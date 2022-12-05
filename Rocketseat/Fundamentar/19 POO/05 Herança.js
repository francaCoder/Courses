class Veiculo { // classe pai
    rodas = 4
    portas = 4

    mover(direcao) {}
    virar(direcao) {}
}

class Moto extends Veiculo {
    // Podemos extender de outros objetos que pode extender de outro...facilita a reutilização de código
    constructor() {
        super() // Puxa todos os atributos e métodos do pai

        // Puxou, tanto é que após o this o vscode já faz sugestões
        this.rodas = 2 // Porém com 2 rodas
        this.portas = 0 // Porém sem portas
    }
}
