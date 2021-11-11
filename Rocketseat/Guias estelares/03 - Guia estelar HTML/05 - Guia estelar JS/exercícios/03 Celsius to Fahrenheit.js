/*
Crie uma função que receba uma string em celsius ou fahrenheit e faça a transformação de uma unidade para outra 

C = (F - 32) * 5/9
F = C * 9/5 + 32

*/



function converteTemperatura(escalaOrigem, escalaDesejada,  temperatura) { // Parâmetros
    const conversor = {
        celsius: {
            fahrenheit() {
                const convertida = temperatura * 1.8 + 32 //   9/5
                return convertida
            }
        },

        fahrenheit: {
            celsius() {
                const convertida = (temperatura - 32) / 1.8
                return convertida
            }
        },
    }
        return conversor[escalaOrigem][escalaDesejada]()
}

console.log(converteTemperatura("fahrenheit", "celsius", 86))



// OU


function transformDegree(degree){
    const celsiusExists = degree.toUpperCase().includes("C")
    const fahrenheitExists = degree.toUpperCase().includes("F")
    // Dependendo da letra o valor vai para uma constante diferente

    if (!celsiusExists && !fahrenheitExists) { // Se não existir nenhum dos dois dá o erro
        throw new Error("Grau não identificado")
    }

    // fluxo ideal, F to C
    // Aqui eu assumi que só existe o F
    let updatedDegree = Number(degree.toUpperCase().replace("F", ""))
    let formula = (fahrenheit) => (fahrenheit - 32) * 1.8
    let degreeSign = "C"
    
    // Caminho alternativo, se tiver o "C" na string, o "Celsius" vai virar true
    if (celsiusExists) {
        updatedDegree = Number(degree.toUpperCase().replace("C", ""))
        formula = (celsius) => celsius * 1.8 + 32
        degreeSign = "F"
        
    }

    return formula(updatedDegree) + degreeSign

}

try {
    transformDegree("50F")
    transformDegree("10C")
    transformDegree("50Z")
    
} catch (error) {
    console.log(error.mesage) // Vai mostrar apenas a mensagem que você colocar no throw
    
}


