/*
    push() - adicionar um elemento na ultima posição
    pop() - remover o último
    peek() - obter o elemento do topo da pilha
*/

class Stack {
    constructor() {
        this.data = []
        this.top = -1
        // this faz a referência do dado que eeu ainda vou criar
    }

    push(value) {
        this.top++
        this.data[this.top] = value
        return this.data
    }

    pop() {
        if (this.top < 0) return undefined
        const poppedTop = this.data[this.top]
        delete this.data[this.top]
        this.top--
        return poppedTop
    }

    peek() {
        return this.top >= 0 ? this.data[this.top] : undefined
    }
}

// utilizando
const stack = new Stack()

stack.push("learning")
stack.push("data")
console.log(stack.push("structures"))
console.log(stack.peek())

// remover
stack.pop()
console.log(stack.pop())
console.log(stack.peek())