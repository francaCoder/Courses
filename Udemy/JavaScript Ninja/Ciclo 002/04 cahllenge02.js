// Crie uma function que receba dois argumentos e retorne a soma dos mesmos

function calculateNum(number1, number2) {
    return number1 + number2
}

console.log(calculateNum(45, 15))

// Declare uma variável que receba a invocação da função criada acima, passando dois numeros quaisquer por argumento

let funcional = calculateNum(45, 15)
console.log(funcional)

// Declare uma variável sem valor

var exemplo

/*
Crie uma function que adicione um valor à variável criada a cima, e retorne a string "o valor da variável agora é ${valor}"
onde ${valor} é o novo valor da variável
*/

function addValue() {
    exemplo = 10
    return "10 é o novo valor de exemplo"
}

console.log(addValue())

 exemplo = 9
 console.log(exemplo)
 exemplo = 5 
 console.log(exemplo)
 console.log(addValue())


 /*
Crie uma função com as seguintes características:
 - Deve receber 3 argumentos 
 - Se os 3 não estiverem preenchidos deve retornar uma string de erro
 - O retorno da função deve ser a multiplicação dos 3 argumentos 
 */

 function multiplyNumbers(number1, number2, number3) { // Parâmetros 
     if( number1 === undefined || number2 === undefined || number3 === undefined){
        return "Preencha todos os valores corretamente"
     } 

     return number1 * number2 * number3

 }

 console.log(multiplyNumbers( 2, 3, 4)) // Argumentos



