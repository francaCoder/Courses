let a, b = 2, c
// a - undefined, b = 2, c - undefined
function myFunction() {
    let x = 0
    return (x += 1, x)
    // O x vai receber tudo que ele tem mais 1 e vai retornar o valor de x
}
