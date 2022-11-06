const { EventEmitter } = require("events")

const ev = new EventEmitter()

ev.emit("saySomething") // para emitir basta usar o .emit, porém se rodarmos o código não vai acontecer nada porque ainda precisamos ouvir esse evento