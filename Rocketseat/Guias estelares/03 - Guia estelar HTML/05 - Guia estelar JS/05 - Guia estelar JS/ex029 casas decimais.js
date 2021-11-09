// Transofrmar um número quebrado com 2 casa decimais e trocar ponto por vírgula 

let number = 1531.153153
console.log(number.toFixed(2).replace("." , ",")) 
// É a variável .toFixed ,  não Number
// Replace serve para trocar os pontos, como parâmetro você vai colocar entre aspas o que você quer trocar e pelo que você quer trocar, esse dois separados por vírgula
