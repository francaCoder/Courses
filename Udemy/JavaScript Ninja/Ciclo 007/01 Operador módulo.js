// Model operetor - %

console.log(5 % 2) // He cheks if exist uma sobra - 1
console.log(4 % 2) // - 0

// And if i want show just pair numbers?

let counter = 0 // Zero is pair, that's why zero was printed/shown
while (counter <= 20) {
    if(counter % 2 === 0) {
        console.log(counter)
    } else {
        console.log(" ")
    }
    counter++

    // OR

    /*
    counter % 2 === 0 ? console.log(counter) : console.log(" ")
    counter++
    */
   
}