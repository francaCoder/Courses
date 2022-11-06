// clearTimeout - vai cancelar o setTimeout

const timeOut = 3000 

const finished = () => console.log("done!")

let timer = setTimeout(finished, timeOut)

clearTimeout(timer)

// Ao rodarmos não acontece nada, o clearTimeout cancelou o setTimeout e também cancelou o "done"