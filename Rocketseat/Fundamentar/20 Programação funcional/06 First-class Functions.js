/*
    Podem estar em qualquer lugar, inclusive como parâmetro de outras funções

    A função poderá sert entendida como uma variável
*/

const sayMyName = () => console.log("Matheus")
const runFunc = fn => fn()

runFunc(sayMyName)
runFunc(() => console.log("Discover"))

console.log(runFunc(Math.random))