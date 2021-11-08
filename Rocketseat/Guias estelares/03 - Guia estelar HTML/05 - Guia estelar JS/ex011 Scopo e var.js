/* 
scopo determina a visibilidade de alguma variável no JS
*/ 

/* 
O var é global e pode funcionar fora de um escopo de bloco

Global é tudo que está dentro da tag script, local é o que está dentro do objeto
*/

console.log("> Existe x antes do bloco? ", x)

{
    var x = 0
}

/*
Ele diz que x existe, mas não tem um valor definido para ele. É como se ele fizesse asism:

var x
console.log(....... x)

{
    x = 0
}
O var vai lá pra cima e ele que fica indefinido
Isso é chamado de hoisting - Elevação
*/
