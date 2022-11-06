const { EventEmitter } = require("events")

const ev = new EventEmitter()

ev.on("saySomething", () => console.log("I heard you") ) // Precisa estar ligado, ouvindo essa emissão de eventos
// Porém também não adianta apenas ouvir se também não temos nenhuma ação para executar
// Por isso já colocamos uma arrow function como segundo argumento dentro do on, quando ele ouvir faça tal coisa...

ev.emit("saySomething") 

// Além do .on para ouvir eventos, também temos o .once, que vai ouvir os eventos uma única vez
// vai ouvir somente o primeiro .emit e os outros ele vai ignorar