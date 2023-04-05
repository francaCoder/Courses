/*
    Node JS - PLataforma open source que permite a execução da linguagem JS do lado do servidor, o mais comum é ver o JS sendo usado do lado do cliente, no browser, mas podemos usar ele para criar o nosso back end.

    V8 - interpretador de JS criado pela google que roda no chrome, executa o JS de forma mais rápida, pega o código e mostra de uma forma que o browser cosegue interpretar

    Módulos que já vem dentro do node

    Função do node - {
        - É baseado em arquitetura Event Loop (em eventos), onde dentro dele tem uma pilha de funções.
        - É single Thread
        - Non-blocking I/O (quando chamamos funções no node, uma não depende que a outra termine de ser executada para que ela possa rodar - Assíncrono)
        - Módulos próprios {
            - http
            - dns
            - file System
            - buffer
            ...
        }
    }

    Event Loop - Fica ouvindo a nossa call stack (lugar aonde estão as nossas funções). A partir do momento que ele escuta uma função ele manda ela para uma Thread disponível (possui 4 por padrão)

    Gerenciadores de pacotes do node [NPM, Yarn] - onde conseguimos instalar e disponibilizar pacotes e bibliotecas

    Frameworks {
        Express
        Egg.js
        Nest.js
        Adonis.js
    }

    API Rest

    API - interface de programação de aplicativos
    um conjunto de características que determinam a forma que um aplicativo irá interagir com outro

    Ao criar uma API é importante deixarmos uma boa documentação

    Rest - Modelo de arquitetura

    Rest possui 6 regras {
        Client Server - não precisa conhecer e nem se preocupar com o que está acontecendo no server
        Stateless - O cliente pode fazer quantas requisições quiser para o servidor, porém o servido não armazena nenhum estado acessando as requisições
        Cache - Nossa aplicação precisa ser construida de uma forma que o cache possa ser feito
        Interface uniforme - Como o cliente e o servidor vão compartilhar a interface {
            Identificação dos recursos - https://exemplo.com/produtos
            Representação dos recursos - O server pode entregar as solicitações de forma Json, xml, etc
        Mensagens auto-descritivas - Importante retornar ao cliente respostas descritivas
        HATEOAS - Retornar links dentro da nossa requisição
        Aplicação criada em camadas
        Código sob demanda - permite que as funcionalidades do cliente sejam estendidas na forma de script ou de mini aplicativos
        }
    }

    métodos de requisições {
        GET - leitura
        Post - criação de algum objeto/informação na nossa aplicação
        put - atualizar alguma coisa
        delete - dedletar
        patch - atualização parcial
    }

    HTTP Codes - tipos de retorno que podemos dar para os nossos clientes, o primeiro digito define a qual categoria/classe esse código pertence
        1xx - informativo (solicitação aceita ou processo continua em andamento)
        2xx - confirmação (requisição bem sucedida)
        3xx - redirecionamento (algo a mais precisou ser feito para que fosse completado)
        4xx - Erros do cliente (Bad request, Not Found)
        5xx - Erros no servidor (Internal server error, Bad Gateway)

    Tipos de parâmetros nas requisições {
        Header Params - Parâmetros que vão no cabeçalho (token, controle de seção, etc)
        Query Params - Parâmetros inseridos no final de uma url (...com.br/?name=value&name=value)
        Route Params - Parâmetros que vão no meio da rota por meio de {}
        Body Params - Parâmetros enviados dentro do nosso body
    }

    Boas práticas {
        utilização correta dos métodos http
        utilização correta dos stts code
        Padrão de nomenclatura 
    }

*/