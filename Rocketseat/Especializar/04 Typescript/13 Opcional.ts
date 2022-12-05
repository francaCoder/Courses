type User = {
    name: string,
    age: number,
    email: string,
    isAdmin?: boolean
}

// Se eu não colocar o isadmin como opcional e preencher as outras propriedades, vai dar erro falando que essa propriedade isAdmin foi esquecida
// Para tornar uma propriedade opcional basta colocar o ponto de interrogação logo na frente dela
let newUser: User = {
    name: "Maheus",
    email: "Matheus@hotmail.com",
    age: 19
}