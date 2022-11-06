// Módulos nativos

// Preciso sempre mandar para o require() um argumento 

// console.log(require("path")) // obj com várias informações

// Require - Usado para chamar módulos nativos ou módulos que ainda podemos criar ou instalar no node
// Path é um módulo que já existe no node (basta olhar na documentação)

const path = require("path")
console.log(path)

console.log(path.basename(__filename)) // ver qual é o nome do arquivo em que estamos

// chamando meu módulo

const myModule = require("./03 Criando Módulos")
console.log(myModule)