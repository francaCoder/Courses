var n1 = 1545.5
var n1 = n1.toFixed(2) // Mostrar n1 com 2 casas decimáis
console.log(n1)

var n2 = 1545.5
var n2 = n2.toFixed(2).replace("." , ",") // 2 casas decimais trocando o ponto pela vírgula
console.log(n2)

var n3 = 1545.5
n3.toLocaleString('pt-br', {style: 'currency' , currency: 'BRl'})
console.log(n3) // Convertendo o valor pra BR, mas n funcionou mt n :(