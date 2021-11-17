// Arrays they are a object disguised - He have properties and metods

// Length is responsible for counting how much elementes exist inside the array

let array = [0, 1, 2, 3]

console.log(array.length) // 4

// If i want show elements 

array.forEach(element => {
    console.log(element)
}); // The best for this occasion

/* before i need know how much elements exist inside my array  or put 'array'.length */

for (let index = 0; index < array.length; index++) {
    const element = array[index];
}