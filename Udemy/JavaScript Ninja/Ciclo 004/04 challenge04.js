/*
Create a variable called "isTruhty", and add a she a function whith one parameter. This function must return "true" if the value boolean that parameter it's true, or false....
*/

let isTruhty = function(TOF) {
    
    return !!TOF // Os dois pontos !! Indica se ele é true or false
}

console.log(isTruhty(1))

// Run the function "isTruthy" and put all values "falses" how argument

console.log(isTruhty(false, undefined, null, NaN, 0, -0, ""))

// Run the function "isTruthy" and how parameter, put 10 values "true"

console.log(isTruhty(1, [], {}, "a", 40, 41, 42 ,43 ,44, true))

/* 
Create a variable called "car" and add a she a object whith this propertys:
- Mark: String
- Model: String
- Board: String    *Placa
- Year: Number
- Color: String
- howMuchDoors: Number
- seats: Number  - 5 how pattern
- howMuchPeoples: Number  - 0 how pattern
*/

let car = {
    mark: "tesla",
    model: "S",
    board: "000-aaa-0",
    year: 2021,
    color: "Gray",
    howMuchDoors: 2,
    seats: 5,
    howMuchPeoples: 0,
}

// Create a METOD called "changeColor" according to color of parameter

car.changeColor = function(newColor) {
    car.color = newColor
}

console.log(car.changeColor("red"))
console.log(car)

// Created a metod called "getColor"