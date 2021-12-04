let num = [5,8,2,9,3]
num.push(1)
console.log(num)
console.log(`O valor tem ${num.length} posições.`)
console.log(`O primeiro valor do array né ${num[1]}`)

for (let pos = 0; pos < num.length; pos++) {
    console.log(num[pos])
}

//ou 

for (let pos in num) {
    console.log(`A posição ${pos} tem o valor de ${num[pos]}`)
} 
// Para cada posição dentro de num, mostre p num[pos]

num.indexOf(7)
// Vai retornar a chave onde o 7 se encontra. (o "Of" É maiúsculo)