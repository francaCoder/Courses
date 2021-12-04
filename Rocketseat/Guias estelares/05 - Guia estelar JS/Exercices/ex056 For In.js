// Vai criar um loop em cima de um object, pegando as propriedades dele

let person = {
    name: "Matheus",
    surName: "França",
    age: 18,
    weight: 83,
}

for(let property in person){
    console.log(property)
}