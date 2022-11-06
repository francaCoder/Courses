// calculadora

function calculate(number1, operator, number2) {

    switch (operator) {
        case "+":
            console.log(number1 + number2)
            break;
        
        case "-":
            console.log(number1 - number2)
            break;
    
        case "*":
            console.log(number1 * number2)
            break;

        default:
            console.log("Não implementado")
            break;
    }

}

calculate(8, "*", 4)