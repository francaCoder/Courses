/*
S - state
T - Type
K - Key
V - Value
E - Element
*/

function useState<T>() {
    // let state: number | string
    let state: T

    function get() {
        return state
    }

    // function set(newValue: number | string) {
    function set(newValue: T) {    
        state = newValue
    }

    return{get, set}
}

// Podemos definir o tipo posteriormente quando formos chamar a função
let newState = useState<string>()
newState.get()
newState.set(123)
newState.set("Matheus")