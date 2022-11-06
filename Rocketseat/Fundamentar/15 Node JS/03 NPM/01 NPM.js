// NPM - Node Package Menager - Gerenciador de pacotes do node

__Glosary: Dependencies, packages, Modules__ // Mesma coisa no fim das contas
// Vamos colocar coisa que outras pessoas criaram aqui dentro do nosso projeto 

// Passos:
/* 
    * Verificar se temos o npm instalado (npm -v (8.1.0))
    * Entrar na pasta que você quer criar o package e criar nosso próprio pacote/dependência/módulo
    * Comando para criar - npm init // Comando para criar sem perguntar nada - npm init -y
    * Package.json - js object notation
    * É um objeto em JS com algumas chaves e valores
    * Baixar outros módulos de terceiros (npm install npm_name ou npm i npm_name)
    * Diretório node_modules, é aonde fica o npm que você baixou. E cada npm que você baixa precisa de dependências de outros npm's, então você acaba baixando outros automaticamente e a pasta node_modules vai enchendo.
    * Precisamos criar um .gitignore e colocar node_modules/ para ignorar ele e não subir junto no git
    * package-lock.json - nesse arquivo você não emxe, serve para fazer um mapeamento de todas as suas dependências que você tem no projeto, faz a manutenção de módulos.
    * Criar scripts para rodar no npm (npm run e o nome da chave no package json que você quer rodar)
    * Dependências globais - npm i opn -g (opção que vai installar de maneira global)
    * npm root -g para saber aonde o package global
    * npm uninstall npm_name -g para desinstalar globalmente
    * Mudar a versão de pacotes instalados - npm moment@versão ou npm outdated mostra todas as versões nisponíveis do pacote
    * npm upgrade para atualizar as versões
    * npm moment@latest para pegar a última versão
*/

/*
{
  "name": "qualquer-nome",
  "version": "1.0.0",
  "description": "Aprendendo Node",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "França",
  "license": "ISC"
}
*/
