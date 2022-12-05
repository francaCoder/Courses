const https = require("https")
const API = "https://jsonplaceholder.typicode.com/users?_limits=2"
// Ele vai até essa  URL para buscar o resultado disso

https.get(API, res => {
    console.log(res.statusCode)
})
console.log("Conectando API")