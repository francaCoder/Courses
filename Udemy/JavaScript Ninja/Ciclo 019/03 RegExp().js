let regex = new RegExp("theus")
console.log("Matheus".match(regex))
let newRegex = /theus/
console.log("Matheus".match(newRegex))

// Samething

/* 
RegExp have methods:
 .test(string)
 .exec
*/

// Teste

let name = "Matheus"
console.log(/\e/.test(name))
console.log(/\d/.test(name))
// Test check if exist the element in your string


// Exec
let regex = /\d/g
let name = "Mat123heus"
let result 
while (result = regex.exec(name) !== null) {
    console.log(result)
}

/*
1  because is the first number in 'name'
If you don't put the 'g' flag, he will do an infinity loop
*/



let clean = new RegExp("[!$]", "g")
let letters = new RegExp("\\w+", "g")
let result = clean + letters
console.log("11dsa!1.2dsa$22.3fas!33-444".replace(result))