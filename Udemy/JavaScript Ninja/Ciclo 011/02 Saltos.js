// For exemple, the "Return" that just can be used inside functions

function myFunc() {
    let number = 10
    if(number === 10) {
        return true // Is a jump
    } else {
        return false
    }
    
}

console.log(myFunc())

/* Another "Jump" is the 'Break' that stay inside switch*/

let number = 10
switch (number) {
    case 10:
        console.log("Ten")
        break;
    case 20:
        console.log("Twenty")
    default:
        console.log("ERROR")
        break;
}

// IF i don't put break, he will verify all cases


// I alson put Break inside loops, for exemple:

for (let i = 0; i <= 10; ++i) {
    if (i === 5) {
        break
    }
    console.log(i)
}
// Whe he be equal five, finish the process
console.log("Stop process")

/* Another "Jump" is the continue */

for (let i = 0; i <= 10; ++i) {
    if (i === 5) { 
        continue        
    }
    console.log(i)
}

// Is equal five? continue and jump five
