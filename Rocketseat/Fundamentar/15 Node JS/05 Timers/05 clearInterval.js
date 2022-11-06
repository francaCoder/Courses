const timeOut = 1000 
const checking = () => console.log("Cheking!")

let interval = setInterval(checking, timeOut) 

// clearInterval(interval) // Uso a clearInterval para cancelar esse intervalo
// Praticamente igual ao clearTimeout


setTimeout( () => clearInterval(interval), 3013) // Vai parar o intervalo após 3s