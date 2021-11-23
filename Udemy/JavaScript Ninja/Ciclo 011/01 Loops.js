// Do While - First he enters in function and before verify the value

let counter = 1
// If i put one number bigger that 8 in counter, even so print in console "Eat pizza", just before he see that counter was bigger that 8, but now it's done....
do {
    console.log("Eat pizza")
    ++counter
} while (counter <= 8);

//

while (counter <= 8) {
    console.log("Eat pizza")
    ++counter
}



// For in - Scan/Sweep properties of that an object

for (let index = 0; index <= 10; index++) {
    console.log(index)   
}


let car = {
    Model: "S",
    Mark: "Tesla",
    Year: 2021,
    Color: "Gray",
}

for (const property in car) {
    console.log(property)
}

// Also can to be used for show if exists any property inside of your object 

console.log("Doors in car?" in car)