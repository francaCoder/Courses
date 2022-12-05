// A sintax está certa, porém nesse caso o JS entende que queremos concatenar o texto, e as vezes mexendo no código podemos causar erros inesperados por conta de atribuições erradas


// function sum(a, b) {
//     return a + b
// }

// console.log(sum("1", "2"))

// Podemos por exemplo definir que os parâmetros recebam apenas números, strings, nulos

// É um verificador de tipo estático
// Vai dizer quando as coisas podem dar errado antes de executar nosso programa

// Sublinha a chamada da função pois userName is not a function
// const userName = "Matheus"
// userName()

// Sublinha o "age" pois essa propriedade não existe
/*
const user = {
    name: "Matheus França",
    email: "matheus@email.com"
}

console.log(user.age)
*/

// Podemos definir o tipos dos parâmetros de uma função
// Sublinha mostrando any - ("Isso pode ser qualquer coisa")
// Sublinha também métodos que tentamos usar mas que não são para funções

/*
function sum(a: number, b: number) {
    return a + b
}

sum.toLowerCase()
sum("2", 4)
*/