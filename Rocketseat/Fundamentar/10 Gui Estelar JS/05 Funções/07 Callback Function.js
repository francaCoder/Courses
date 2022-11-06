
    function sayMayName(name) {
        console.log(name)
    }

    // assim como variáveis, numbers, strings..eu posso passar dentro da função, eu também posso passar uma funçã dentro da função.
    sayMayName( 
        () => {
            console.log("Estou em uma callback")
        }
    )

    // A função inicial  vai nos retornar essa nova função.