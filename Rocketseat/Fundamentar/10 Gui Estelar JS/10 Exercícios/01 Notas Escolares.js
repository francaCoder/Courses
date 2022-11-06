/* Crie um algoritimo que transforme as notas escolares em letras

menor que 60 = f
entre  60 - 69 = d
entre 70 - 79 = c
entre 80 - 89 = b
de 90 pra cima = a
*/

let nota = 70

if (nota < 60) {
    console.log("F")
} else if (nota < 69) {
    console.log("d")
} else if (nota < 79) {
    console.log("c")
} else if (nota < 89) {
    console.log("b")
} else {
    console.log("a")
}