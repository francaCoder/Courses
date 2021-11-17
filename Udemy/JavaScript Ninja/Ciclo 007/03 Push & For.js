// The push serves for add more one element inside array

let array = [0,1 , 2 ,3 ,4]

array.push(5)
console.log(array)

// I can to spend any think

// For is a repition structure , almost equal a While

let counter = 0
while (counter <= array.length ) {
    console.log(counter)
    counter++
}

// Or FOR

for (let index = 0; index < array.length; index++) {
    const element = array[index];    
    console.log(index)
}
// Initialize, condition, increment

//OR

array.forEach(element => {
    console.log(element)
});

