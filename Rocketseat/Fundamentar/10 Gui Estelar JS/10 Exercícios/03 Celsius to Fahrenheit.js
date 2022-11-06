/*
    Crie uma função que faça essa conversão de temperaturas, ela deve receber os graus e para qual medida ela deve converter
*/

/*
function converterTemperatura(graus, medida) {
    if (medida.toUpperCase() == "F") {
        console.log(`${graus}º Celsius em Fahrenheit são ${}º`)
    } else if (medida.toUpperCase() == "C") {
        console.log(`${graus}º Fahrenheit em Celsius são ${}º`)
    } else {
        console.log("Coloque corretamente a inicial de qual medida esses graus devem ser convertidos")
    }
}
*/

// converterTemperatura(10, "F")

function transform(degree) {
    if (degree.toUpperCase().includes("C")) {
        number = Number(degree.toUpperCase().replace("C", ""))
        console.log(`${number * 9/5 + 32}ºF`)
        
    } else if (degree.toUpperCase().includes("F")) {
        number = Number(degree.toUpperCase().replace("F", ""))
        console.log(`${(number - 32) * 5/9}ºC`)
    } else {
        console.log("Coloque os graus seguido da letra inicial de sua atual unidade de medida (C ou F).")
    }
}

transform("10c")
transform("50f")
transform("30p")