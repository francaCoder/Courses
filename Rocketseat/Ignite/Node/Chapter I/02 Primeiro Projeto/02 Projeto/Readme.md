### Requisitos

    Deve ser possível {
        ✅ Criar uma conta
        ✅ Buscar o extrato bancário do cliente
        ✅ Realizar um depósito
        ✅ Realizar um saque
        ✅ Buscar o etrato bancário do cliente por data
        ✅ Atualizar dados da conta do cliente
        ✅ Obter dados da conta do cliente
        ✅ Deletar uma conta
        ✅ Balanço geral
    }
    
### Regras de negócio

    Não deve ser possível {
        ✅ Cadastrar uma conta com um CPF existente
        ✅ Fazer depósito em uma conta não existente
        ✅ Buscar extrato em uma conta não existente
        ✅ Fazer saque em uma conta não existente
        Excluir uma conta não existente
        Fazer saque quando o saldo for insuficiente
    }