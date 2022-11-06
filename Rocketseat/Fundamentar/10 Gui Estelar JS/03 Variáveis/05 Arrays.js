

    const animals = [
        "Lion", 
        "Monkey", 
        "Cat",
        {
            name: "bummer",
            age: 8
        }

    ]

    // Como acessar valores de dentro de um array?
    // Precisamos lembrar que diferentemente do objeto, o array não tem nome em suas CanvasCaptureMediaStreamTrack, por isso devemo acessar pelo index.

    console.log(animals[1])

    // Agora dentro do nosso array temos um objeto, e queremos acessar uma propriedade específica daquele objeto

    console.log(`O ${animals[3].name} tem ${animals[3].age} anos`)