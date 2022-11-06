// throw - lançar

// catch Pegar

function sayMyName(name) {
    if (name === "") {
        throw new Error("Nome é necessário")
    }

    console.log("Depois do erro")
}

try {
    sayMyName()
} catch(e) {
    console.log(e)
}

console.log("Depois do erro 2")