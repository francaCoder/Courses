// Throw - disparar / Lançar e alguem vai pegar




function sayMyName(name = ""){
    if (name === "") {
        throw "nome é obrigatório" 
        // Podemos usar ele sem o Try e o catch, ele vai parar a aplicação quando der algum erro
    }

    console.log("Depois do erro")
}

try{
    sayMyName()
} catch(e) {
    console.log(e)

}

// Try - tentar 
// Catch - capturar