/*
    * Algumas diferenças do map
    * É uma caixa preta
        Não consegue saber nenhum valor que está dentro do weakmap se você não tiver o weakmap e nem a chave dentro dele.

        Portanto ele não tem keys, entries, não é iterável, etc

        Não consegue adicionar como chave os tipos primitivos, só aceita objetos e funções

        Para acessar algum valor preciso ter meu weakmap e a chave dele
    * Referência fraca nas chaves
*/

const name = "Matheus"
const user = {id: "122"}

const mapa = new Map()

// Defini como chave do meu mapa a constante user (como passagem de referência)
mapa.set(user, "Valor 1")

const wMapa = new WeakMap()
wMapa.set(user, "valor 2")

// O Weakmap não impede que sua chave seja apagada da memória
user = null
console.log(wMapa)