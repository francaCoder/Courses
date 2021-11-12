let exemple = function() {
    return "variável exemple"
}

console.log(exemple())

let person = {
    name: "Matheus",
    age: 18,
    height: 1.82,
    weight: 83,
}

person = {sexo: "Masculino"}
 // Se eu fizer isso eu redeclarei ela e perdi todos os meus antigos dados

// Se eu quiser adicionar uma propriedade de maneira correta:

person.hair = "Black"
console.log(person)

person.walk = function() { return "Walking person"} // Isso é um método
console.log(person.walk)

// here our object person have a property "Walk", Walk receive a function, the function return "Walking person". When i hwant that person walking, i run this function

let matheus = {
    name: "Matheus",
    surName: "França",
    age: 18,
    height: 1.83,
}

matheus.birthday = function() { // I add a metod a function
    matheus.age++
}

console.log(matheus.birthday())
console.log(matheus)

// after i run a birthday function, the property age recieve +1

matheus.nomeCompleto = function() {
    return `O nome completo é ${matheus.name} ${ matheus.surName}`
}

console.log(matheus)
console.log(matheus.nomeCompleto())