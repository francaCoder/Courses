/* 
Now we will speak a litle about soccer. Choice any championship for started the challenge

declare one variable called "Championship" that will recieves the name of 'championship'
after print the name of championship in console
*/

let championship = "Euro League"

/*
Declare one variable called "Teams", that will recieves one array whith 5 elements. The elements will be names of teams of championship that you choiced, and the names must be in ordered according to table in moment of resulution this challenge
*/

let teams = ["Napoli", "Lyon", "Mônaco", "Lazio", "Rangers"] 

/* 
Create a function called 'showTeamsPosition' whit the following characteristics:
- The fuction must recieves a number as parameter
- The fuction must return a phrase:
"The team that be wining is in position [Position]º place is the [name of team]"
- Where [Position] is the value past in parameter and [name of team] is the team that be this position in array created above whith names os teams.

tip: Remember that arrays initiate by 0, then the position past must be ever 1 number more that the index of array

- The function just must return the phrase above if the team is in top 5
- IF don't exist team to position past, must return the message:
"we don't have any information about the team that is in this position."
*/

function showTeamsPosition(position) {

    if (position > 5 || position < 1) {
        return "We don't have any information about the team that is in this position"
    } 

    return "The team that be wining is in position " + position + "º place is the " + teams[position - 1] + "."

}

// Choice 4 teams of championship and show their position. Among these (entre esses) 4, add 1 that don't be among these top 5.

console.log(showTeamsPosition(1))
console.log(showTeamsPosition(3))
console.log(showTeamsPosition(2))
console.log(showTeamsPosition(5))
console.log(showTeamsPosition(8))

// Show the numbers among 20 a 30 in console, using the repeating structure "While"

let counter = 20 // Initiate whith 20
while (counter <= 30) {
    console.log(counter)
    counter++
}

/* 
Create a function called "convertToHex", whith the following characteristics:
- The function recieves a color per parameter, of type "String"
- Choice 5 colors that will be converted of name of color for your hexadecimal
- Using the repeat structure Switch, verify if the passed color in the parameter is some chosen hex, and return the phrase (if is true) :
"The hexadecimal for the color [color] is [hexadecimal]"
- IF the passed color in the parameter don't be among these the selected, show the phrase:
"We don't the equivalent hexadecimal for [color]"
*/

function convertToHex(color) {

    switch (color) {
        case "Red":
            return `The hexadecimal for the color ${color} is #FF0000`
            break;
        case "Green":
            return `The hexadecimal for the color ${color} is #00FF00`
            break;
        case "Blue":
            return `The hexadecimal for the color ${color} is #0000FF`
            break;
        case "Yellow":
            return `The hexadecimal for the color ${color} is #FFFF00`
            break;
            case "Orange":
            return `The hexadecimal for the color ${color} is #F24F00`
            break;
        default:
            return `We don't the equivalent hexadecimal for ${color}`
            break;
    }
}

console.log(convertToHex("Black"))