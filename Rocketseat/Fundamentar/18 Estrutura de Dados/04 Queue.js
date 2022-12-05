// Enqueue() - Adicionar um elemento no final da fila
// dequeue() - Remover o primeiro elemento a entrar na fila

// Outros métodos como size() e front() para pegar o primeiro elemento da fila, dentre outros.

// 1 - Modelagem
class Queue {
    constructor() { // É executada no momento em que a gente criar a queue
        this.data = [

        ]
    }

    enqueue(item) {
        this.data.push(item)
        console.log(`${item} chegou na fila!`)
    }

    dequeue(item) {
        this.data.shift() // Vai tirar o primeiro a entrar nessa fila
        console.log(`${item} saiu da fila!`)
    }
}

// 2 - Utilizando
const fila = new Queue()

fila.enqueue("Mariana")
fila.enqueue("João")
fila.enqueue("Ariel")
fila.dequeue()
fila.dequeue()
fila.dequeue()