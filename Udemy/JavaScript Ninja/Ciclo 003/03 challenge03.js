// Declarar uma variável qualquer que receba um objeto vazio

let person= {}

/*
Declarar uma variável "pessoa" que receba suas informações pessoais.
As propriedades e tipos de valores para cada propriedade desse objeto devem ser:
Nome: string
Idade: number
Altura: number
peso: number
andando: boolean - recebe false por padrão
caminhouQuantosMetros: number - 0 Por padrão
*/

person = {
    name: "Matheus",
    surName: "França",
    sex: "man",
    age: 1,
    height: 1.83,
    weight: 83,
    walking: false,
    howMuchMetersWalked: 0
}

// Add a metod for person objetc called by "happyBirthday". This metod must change the value of age property, add one for every time it is called

person.happyBirthday = function() {
    person.age++
}

console.log(person.happyBirthday())
console.log(person)

/*
 Add a metod for person obejct called "walk" must receive:
 - One parameter value that represented How much meters walked
 - He must change the value of property "HowMuchMetersWalked", adding for this person the value of your parameter
 - He must change  modify the value of walking property for the value boolean "True"
 */

person.walk = function(hmmw) {
    person.howMuchMetersWalked = hmmw
    person.walking = true
}

console.log(person.walk(100))
console.log(person)

// Add a METOD for "person" object called "stop", that will modidy the value of "walking" property for the value boolean "False"

person.stop = function() {
    person.walking = false
}

/*
create a metod called "fullName" that return the phrase: 
"Hi! my name's [NAME] [SURNAME]"
*/

person.fullName = function() {
    return `Hi! My name's ${person.name} ${ person.surName}`
}

/*
Create a metod called "showAge" that return the phrase:
"Hi! I have [AGE] years old"
*/

person.showAge = function() {
    return `Hi! I have ${person.age} years old`
}

/* 
Create a metod called "showWeight" that return the phrase:
"Hi! I have [Weight] kg"
*/
person.showWeight = function() {
     return `Hi! i have ${person.weight} kg`
 }

person.showHeight = function() {
    return `Hi! I have ${person.height}`
}

 /* 
Now let's play a lot whith this object:
whats is full name of person?
*/

console.log(person.fullName()) // Full name its a metod

// Whats the age, weight and height

console.log(person.showAge(), person.showWeight(), person.showHeight())

// Make this person walk some meters

console.log(person.walk(20))
console.log(person.walk(30))
console.log(person.walk(40))

// Make this person stop walk. walking = false
console.log(person.stop())

// how much meters this person walked?
console.log(person.howMuchMetersWalked)

/*
Create a metod for object person called "apresentation". This metod must return the string whith a apresentation

Before returning, you must make changes:
- If "sex" the person is "woman", the phrase must be adaptade
- If "age" is 1, write year, not years(same thing for How much meters walked)
*/

person.apresentation = function() {
    if (person.sex === "man" && person.age > 1) {
        return `Hi! my name's ${person.fullName} and i have ${person.age} years` 
    } else if (person.sex === "man" && person.age < 2) {
        return `Hi! my name's ${person.fullName} and i have ${person.age} year` 
    } else if (person.sex === "woman" && person.age > 1) {
        return `Hello! my name's ${person.fullName} and i have ${person.age} years` 
    } else if (person.sex === "man" && person.age < 2) {
        return `Hello! my name's ${person.fullName} and i have ${person.age} year` 
    }
    
}

console.log(person.apresentation())

 // Só não entendi porque não está escrevendo o nome completos dentro dos If's, mas a condição dele de trocar o início da frase e o plural da idade está funcionando.






