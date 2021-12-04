/* 
Const e let são locais e só funcionam no scopo onde foram criadas
*/

//console.log("> Existe y antes do bloco? ", y)

{
    let y = 0
    console.log("Existe y no bloco?", y)

}

// console.log("Existe y depois do bloco? ", y)

/*
Esse é o perigo de usar o var, pois ele é flexível e podemos redefinir ele sem querer e causar bugs inesperados, diferente de const e de let
*/