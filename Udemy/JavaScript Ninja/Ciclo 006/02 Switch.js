// Estruturas condicionais

function myFunction(x) {
    switch (x) {
        case 1:
            console.log("x is equal a 1")
            break;
        case 2:
            console.log("x is equal a 2")
            break;
        default:
            console.log("x ins't 1 nor 2")
            break;
    }
}

// For each case, return one diferent phrase, if dont exist, return default

myFunction(2)