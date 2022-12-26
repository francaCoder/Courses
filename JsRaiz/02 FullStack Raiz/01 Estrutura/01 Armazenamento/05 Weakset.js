/*
    Semelhante ao weakmap
    também não tem o clear

    tem
        add 
        has
        delete
*/

const ws = new WeakSet
const obj = {name: "Matheus"}
ws.add(obj)
ws.add(obj)
console.log(ws.has(obj))