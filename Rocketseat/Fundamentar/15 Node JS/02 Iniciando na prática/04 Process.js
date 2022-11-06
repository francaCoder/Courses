// console.log(process) // ele vai trazer pra gente muitas informações, vamos ver em específico o 'argv (um array que tyraz uma lista de argumentos que eu estou rodando no node)'

// console.log(process.argv)

// console.log("Seu nome é", process.argv[2] + " " + process.argv[3])
// Dessa forma o argv fica com mais argumentos, como ele é uma lista eu posso selecionar seus index's, e consequentemente montar uma frase como essa. Basta eu executar de seguinte forma:
// node process.js Matheus França, o console pegará as posições e montará a frase
// Podemos atribuir o argv[index] para alguma variável e chamar eladps, etc


// → Rodando o desafio:

const getFlagValue = require("./07 Função")

console.log(`Oi ${getFlagValue("--name")}, ${getFlagValue("--greeting")} ${getFlagValue("--complemento")}`)

// node '.\04 Process.js' --name "Matheus França" --greeting "Blz mano?"
// Aqui eu passei as flags e as frases em sequência da mesma forma, o arquivo process salva todos os index dentro da lista e eu uso um console.log que usa a função importada (getFlagValue) de outro arquivo para montar a frase. Essa função recebe essas flags que eu passei para ela em cada chave, volta no aquivo process, procura e retorna o index + 1 (resposta) dessa flag, assim conseguindo montar a frase

// Quando eu rodo esse arquivo apenas usando node process, ele retorna apenas o oi porque eu não usei nenhuma flag, aí ele retorna esses caminhos logo em sequência

// E também descobri que você pode utilizar qualquer flag sem nome específico pré estabelecido. (só não sei se isso é um bom modo da linguagem :))
