/*
Crie um algorítimo que transoforme as notas escolares do alunos de 1, 2, 3.... para A, B, C....

* De 90 pra cima - A
* Entre 80 e 89 - B
* Entre 70 e 79 - C
* Entre 60 e 69 - D
* Menor que 60 - F

*/

/*

let nota = 70

if (nota >= 90) {
    console.log("A")
} else if (nota >= 80 && nota < 90) {
    console.log("B")
} else if (nota >= 70 && nota < 80) {
    console.log("C")
} else if (nota >= 60 && nota < 70) {
    console.log("D")
}else {
    console.log("F")
}

*/


let nota = 90

switch (true) {
    case nota >= 90:
        console.log("A")
        break;

    case nota >= 80 && nota < 90:
        console.log("B")
        break;

    case nota >= 70 && nota < 80:
        console.log("C")
        break;

    case nota >= 60 && nota < 70:
        console.log("D")
        break;

    case nota < 60:
        console.log("F")
        break;

    default:
        console.log("Insira a nota")
        break;
}




/*

function convertScore(nota){

    let finalScore
    
    if (nota < 0 || nota > 100){
        finalScore = "Nota inválida"
    }else if (nota >= 90) {
        finalScore = "A"
    } else if (nota >= 80 && nota < 90) {
        finalScore = "B"
    } else if (nota >= 70 && nota < 80) {
        finalScore = "C"
    } else if (nota >= 60 && nota < 70) {
        finalScore = "D"
    }else if(nota < 60){
        finalScore = "F"
    } 

    return finalScore
}

console.log(convertScore(101))
console.log(convertScore(-1))
console.log(convertScore(0))
console.log(convertScore(1))
console.log(convertScore(45))
console.log(convertScore(60))
console.log(convertScore(61))
console.log(convertScore(75))
console.log(convertScore(85))
console.log(convertScore(95))

*/