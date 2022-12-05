// Sempre ao criar tipos crie com letra maiúscula (boa prática)

type PropertiesUser = {
    id: number,
    name: string,
    avatar: string
}

let userResponse = {} as PropertiesUser

// Posso usar o as e atribuir ao objeto as propriedades que eu defini inicialmente usando o type
// E quando eu chamo o objeto e uso o ponto ele já me dá sugestões das propriedades de dentro dele
userResponse.id
