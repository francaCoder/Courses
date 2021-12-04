// Podemos fazer uma variável receber uma função

/*
      const sum = function(number1, number2){ // Parâmetros
         console.log(number1 + number2)
      }

      sum(2, 3) // Argumentos 
*/

// Se eu colocar o console log aqui, daria um referenceError de não definido, pois não rodaria fora do escopo

const sum = function(number1, number2) {
   total = number1 + number2
   return total
}

let number1 = 34
let number2 = 25

console.log(`O número 1 é ${number1}`)
console.log(`O número 2 é ${number2}`)
console.log(`A soma dos números é ${sum(number1, number2)}`)
console.log(total) // Só consegue aparecer porque o total dentro da function não tem nenhuma palavra chave como /let/const se eu colocasse o var chamaria, porque é global