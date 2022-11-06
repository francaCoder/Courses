

    // Const e let são globais e só funcionam no escopo onde foram criadas


    console.log("Existe y antes do bloco?", y)

    {
        let y = 0
    }

    console.log("Existe y depois do bloco?", y)