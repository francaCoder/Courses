// Object

const person = {
    name: "Matheus França", // Obregatório no final de cada linha dentro do objeto ter a vírgula
    age: 18,
    weight: 83,
    isAdmin: true,
}
console.log(person)

// E se eu quiser pegar apenas uma propriedade?

console.log(person.age) 
/*
Usamos o Ponto Final para entrar nas propriedades existentes dentro do objeto. Como se fosse o > lá no CSS.
Após colocarmos o Ponto, o VS code Já nos ajuda com a sugestão de Auto complete dele
*/

console.log(`${person.name} tem ${person.age} anos :)`)