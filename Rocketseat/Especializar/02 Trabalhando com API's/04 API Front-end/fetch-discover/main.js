const { response } = require("express")

const url = "http://localhost:5500/api"
const newUser = {
    name: "Matheus França",
    avatar: "http://picsum.photo/200/300",
    city: "Minas Gerais"
}

const updatedUser = {
    name: "Marcelo",
    avatar: "http://picsum.photo/200/300",
    city: "Sergipe"
}

function getUsers() {
    // fetch trabalha com promisses - then e cacth
    fetch(url).then(response => response.json())
    .then(data => renderResult.textContent = JSON.stringify(data))
    .catch(error => console.error(error))
}

getUsers()

// Mostrando um único usuário

function getUser(id) {
    fetch(`${url}/${id}`).then(response => response.json()).then(data => {
        // return renderResult.textContent = JSON.stringify(data)

        // Depois de data podemos colocar ponto e acessar alguma propriedade específica para filtrar

        userName.textContent = data.name
        userCity.textContent = data.city
        userAvatar.src = data.avatar
    })
    .catch(error => console.error(error))
}

getUser(1)

// addUser(newUser)

function addUser(newUser) {
    fetch(url, {
        method: "POST",
        body: JSON.stringify(newUser),
        Headers: {
            "content-type": "application/json; charset=UTF-8"
        }
    }).then(response => response.json())
    .then(data => alertAPI.textContent = data).catch(error => console.error(error))
}

addUser()

// update user

function updateUser(user) {
    fetch(`${url}/1`, {
        method: "PUT", 
        body: JSON.stringify(user),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then(response => response.json())
    .then(data => alertAPI.textContent = data)
    .catch(error => console.error(error))
}

updateUser(updatedUser)

// delete user

function deleteUser(id) {
    fetch(`${url}/${id}`, {
        method: "DELETE",
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then(response => response.json())
    .then(data => alertAPI.textContent = data)
    .catch(error => console.error(error))
}
