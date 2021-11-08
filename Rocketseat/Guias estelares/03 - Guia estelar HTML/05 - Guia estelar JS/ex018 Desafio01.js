//Declare  uma variável de nome weight
        // let weight

//Que tipo de dado é a variável acima?
        // console.log(typeof weight) // Undefined

/*
3 - Declare uma variável e atribua valores para cada um dos dados
    * name: string
    * age: number (integer)
    * stars: number (float)
    * isSubscribed: boolean
*/

/*
        let name = "Matheus França"
        let age = 18
        let stars = 5.0
        let isSubscribed = false
*/

/* 
4 - A variável studant abaixo é de qual tipo de dado?
- Atribua a ela as mesmas propriedades e valores do exercício 3
- Mostre no conseole log a seguinte mensagem:
"<name> com a idade <age> pesa <weihgt>"
Isso usando a interpolação e substituindo automaticamente do studant object
*/


        let student = {
            name: "Matheus França",
            age: 18,
            weight: 83,
            isSubscribed: false,
        }


        //console.log(`${studant.name} com a idade de ${studant.age} pesa ${studant.weight}kg`)

/*
5 - Declare uma variável do tipo array de nome studants e deixe o array vazio
*/

let students = []

/* 
6 - reatribua o valor da variável acima colocando o student object da questão 4
*/

students = [
    student 
]

console.log(students) // One object inside array in position zero

// 7 - Coloque no console o valor da posição 0 do objeto

console.log(students[0].name)

const Brandom = {
    name: "Brandom",
    age: 78,
    weight: 60,
    isSubscribed: true,
}

students = [
    student,
    Brandom,
]

console.log(students)

// Ou fazer a posição 1 do array receber o Brandom

//students[1] = Brandom

/*
Tente descobrir a resposta do exercício:
console.log(a)
var a = 1
*/

console.log(a)
var a = 1
// Da undefined porque A não existe na antes da linha do console.log, porém é feito o hoisting por debaixo dos panos levando o "var a" para cima do console.log
// Se fosse let daria um  erro de referência