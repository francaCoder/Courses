type Point = {
    x: number,
    y: number
}

function printCoord(points: Point) {
    console.log(`O eixo x é ${points.x} e o eixo y é ${points.y}`)
}

// Tenho que chamar passando um objeto
printCoord({x: 101, y: 15})

// 

type User = {
    name: string,
    age: number,
    email: string
}
const newUser: User
newUser.name