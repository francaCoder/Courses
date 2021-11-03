let agora = new Date()
let diaSem = agora.getDay()

/*
0 = Domingo
1 = segunda
2 = terça
3 = quarta
4 = quinta
5 = sexta
6 = sabado
*/

//console.log(diaSem) 
    /* if (diaSem == 0) {
        console.log("Domingo")
        } else if(diaSem == 1) {
            console.log("Segunda")
        } .....
    */

switch (diaSem) {
    case 0: 
        console.log("Domingo")
        break
    case 1:
        console.log("Segunda-Feria")
        break
    case 2:
        console.log("Terça-Feira")
        break
    case 3:
        console.log("Quarta-Feira")
        break
    case 4:
        console.log("Quinta-Feira")
        break
    case 5:
        console.log("Sexta-Feria")
        break    
    case 6: 
        console.log("Sábado") 
        break

        default:
            console.log("Dia inválido")
}