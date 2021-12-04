
// Function hoisting

sayMyName()

function sayMyName() {
    console.log("Matheus França")
}

// Vai rodar do mesmo jeito, é como se o JS jogasse ela lá pra cima

// Se declarassemos antes usando o const, var, let e essa declaração recebesse a function, ela não sofreria o hoisting