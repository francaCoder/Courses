// Meus módulos

// Como criamos um módulo para ser usado dentro do node

// basta usarmos o objeto global 'module.exports', posso atribuir à ele algum tipo de dado e após isso eu posso chamar ele em outro arquivo usando o require

module.exports = "Enviando dados do meu módulo"

// Eu basicamente linkei dos arquivos JS através do module.exports e do require()
// Dentro do require (no arquivo que eu for chamar) eu passo o caminho do meu arquivo que eu criei os módulos.