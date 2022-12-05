import axios from "axios";

Promise.all([
  // Array de chamadas que acontecem ao mesmo tempo
  axios.get("https://api.github.com/users/maykbrito"),
  axios.get("https://api.github.com/users/maykbrito/repos")
  // Ele só entra no Then depois que entrar em todos os Gets
]).then(responses => {
  // Responses porque a resposta também vem dentro de um array
  console.log(responses[0].data.login, responses[1].data[2])
}).catch(err => console.log(err.message))