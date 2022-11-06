// Vai setar um intervalo para aquela função ficar rodando, é como se colocasse isso dentro de um loop for

const timeOut = 1000 // milisegundos 1000 - 1s
const checking = () => console.log("Cheking!")

setInterval(checking, timeOut) // 2 args, a função e o tempo

// ao rodar dessa forma, a cada 1s vai ser escrito no terminal a palavra "checking"
// Essa função simula algo que teríamos que verificar a cada 1s se algo está "ok"

// Aparentemento no primeiro argumento do setInterval só é aceito dados do tipo function

const sayHi = function() {
    console.log("hi")
}

setInterval(sayHi, timeOut)

// Essas funções vai rodar infinitamente e de forma assíncrona