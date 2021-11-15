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

// Create a metod called "getColor", that must return  the 'color' of 'car'.

car.getColor = function() {
    return car.color
}

// Create a metod called "getModel", that must return the 'Model' of 'car'.

car.getModel = function() {
    return car.model
}

// Create a metod called "getMark", that must return the 'mark' of 'car'.

car.getMark = function() {
    return car.mark
}

/* Create a metod called "getMarkAndModel", that must return:
"This car is a [mark] [model]"
use the metods */

car.getMarkAndModel = function() {
    return `This car is a ${car.getMark()} ${car.getModel()}`
}

/* Create a metod that must add peoples in the car. This metod must have the following characteristics:
- He must recieve for parameter the number of peoples that will enter in car. This number dont need to fill (encher) a car, you can add peoples slowly.
- The metod must return the phrase: "We have [peoples] peoples in car."
- IF the car be already fil, must  return the phrase: "The car is already fill"
- IF have empty seats in car,  but the numbers of peoples in parameter is more that the number of seats, you must show how much seats can be occupied/busy (ocupados), whith the phrase:
"Just only fit more [number of how much peoples] peoples"
- IF fit just more one people, show the word "people" in place "peoples"
*/

/*
car.addPeoples = function(NOP) {
    if (NOP > car.seats) {
        return "The car just have 5 seats, sorry."
    } else if(NOP === car.seats) {
        return "The car be already fil, fasten your belts." // Aperte os cintos
    } else if(NOP < car.seats) {
        return "More peoples can enter in car."
    }
}

console.log(car.addPeoples(4))
*/

car.addPeoples = function(NOP) {
    let totalPeoples = car.howMuchPeoples + NOP

    if (car.howMuchPeoples === car.seats && totalPeoples >= car.seats) {
        return "The car be already fil, fasten your belts." // Aperte os cintos"
    }

    if (totalPeoples > car.seats) {
        let howMuchPeoplesFit = car.seats - car.howMuchPeoples
        let pluralOrSingular = howMuchPeoplesFit === 1 ? "people" : "peoples"
        return `Just only fit more ${howMuchPeoplesFit} ${pluralOrSingular}`
    }
    car.howMuchPeoples += NOP
    return `already have ${totalPeoples} peoples in car`
    
}
console.log(car.addPeoples(3))
console.log(car.addPeoples(4))

// Add more 2 peoples in car

// Make the car be fill

//take 4 peoples out of the car

// Try add 10 peoples in car


