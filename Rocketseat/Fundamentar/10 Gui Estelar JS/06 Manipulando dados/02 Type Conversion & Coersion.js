/*
    Type conversion (Typecasting) vs Type coersion

    * Alteração ed um tipo de dado para outro tipo
*/

console.log("9" + 5) //95
// Nosso programa usa o type coersion para forçar uma transformação de tipo do 5 para string para que nosso programa não dê erro, e retorna o valor 95 como string.


// Posso mudar manualmente
console.log(Number("9") + 5) //14

console.log("9" + String(5))