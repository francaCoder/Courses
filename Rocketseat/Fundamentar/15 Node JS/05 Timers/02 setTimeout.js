// Vai rodar uma função depois de tantos milisegundos

const timeOut = 3000 // 3s

const finished = () => console.log("done!")

setTimeout(finished, timeOut)
console.log("mostrar") // Vamos ver primeiro o mostrar e depois vamos ver o "done"

// Isso é o Assincronismo

// Ao rodarmos esse arquivo no terminal, esperamos ver a palavra "done" no terminal depois de 3s