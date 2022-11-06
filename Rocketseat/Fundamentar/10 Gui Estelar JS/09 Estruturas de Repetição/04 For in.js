// For in - para objetos

let person = {
    name: "Jhon", 
    age: 30,
    wheight: 88.6
}

for (const prop in person) {
    console.log(`${prop} → ${person[prop]}`)
}