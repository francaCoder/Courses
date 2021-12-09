// Regular expressions serves for manipulate Strings

let text = "Manuel Marques de Sousa, Conde de Porto Alegre (Rio Grande, 13 de junho de 1804 – Rio de Janeiro, 18 de julho de 1875), apelidado de 'O Centauro de Luvas',[nota 1] foi um militar, político, abolicionista e monarquista brasileiro. Ele nasceu em uma família rica e de tradição militar, entrando no exército em 1817 quando ainda era criança. Sua iniciação militar ocorreu na Guerra contra Artigas, que teve seu território anexado e se tornou em 1821 a província brasileira da Cisplatina. Ele ficou envolvido durante boa parte da década de 1820 no esforço brasileiro para manter a Cisplatina como parte de seu território, primeiro durante a independência do Brasil e depois na Guerra da Cisplatina. No final a província conseguiu se separar e se tornou a nação independente do Uruguai."


/*
g = Global 
i = Ignore case
*/

console.log(text.match(/m/g)) 

// Terms
/* 
don't exist = null
W = Alphanumeric characters?
D = number
 | = Pipe
[] = Similar to pipe
() = Grouping
$ = Capture
*/

console.log(text.match(/\w/g)) // Array[608] elements / letters
console.log(text.match(/\d/g))  // Global numbers
console.log(text.match(/\d\d/)) // Just the first 2 numbers

// I am search 'de' OR 'da'
console.log(text.match(/de|da/g)) 

//   []  it is similar to |   , but you don't need put oftentimes, just one 

console.log(text.match(/[abc]/g))
// Show in console = 'a'   OR   'b'   OR   'c'

//Grouping

console.log(text.match(/[(1875)(1817)]/g))

// I want all characters among 0 at 9

console.log(text.match(/[0-9]/g))

// All letters

console.log(text.match(/[a-z]/g))

// UpperCase

console.log(text.match(/[A-Z]/g))


// Now i a can change 'de' for 'DE', I can use replace() too

console.log(text.replace(/de/g, "DE"))
// When you find 'de' change for 'DE'

console.log(text.replace(/(d)(e)/g, '$1$1')) // DE = DD

console.log(text.replace(/(d)(e)/g, '--$2--$2')) // DE = DD

// Interspasing letters

console.log("Matheus".replace(/(\w)(\w)/g, function(AllCapture, letter1, letter2) {
    return letter1.toUpperCase() + letter2.toLowerCase()
})) 





