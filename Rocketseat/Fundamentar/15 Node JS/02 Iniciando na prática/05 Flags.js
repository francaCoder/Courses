// podemos usar flags no terminal
// --name --greeting

// node '.\05 Flags.js' --name "Matheus França" --greeting "Tudo bem com você?"
console.log(process.argv)

// saída do argv:

// [
//     'C:\\Program Files\\nodejs\\node.exe',
//     'C:\\Users\\mathe_dr5d6so\\Codes\\Cursos\\Rocketseat\\Fundamentar\\15 Node JS\\02 Iniciando na prática\\05 Flags.js',
//     '--name',
//     'Matheus França',
//     '--greeting',
//     'Tudo bem com você?'
//   ]

// lemos:
// a flag name recebe Matheus França e a tag greeting (saudações) recebe essa frase