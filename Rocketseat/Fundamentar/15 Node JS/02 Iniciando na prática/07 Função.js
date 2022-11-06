function getFlags(flag) {
    const index = process.argv.indexOf(flag) + 1
    // está procurando no process.argv qual que é a posição da flag que foi passada
    // Após achar a flag retorne o argv[index + 1] (que é a resposta)
    return process.argv[index]
}

module.exports = getFlags // Exporta a função

// e vamos chamar minha função lá do arquivo process, já que é ele que está no return