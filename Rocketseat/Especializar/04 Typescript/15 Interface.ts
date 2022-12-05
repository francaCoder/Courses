interface User {
    id: number,
    name: string
}

let newUser: User = {
    id: 1, 
    name: "Matheus"
}

function registerNewUser(newUser: User) {
    console.log(newUser.name)
}