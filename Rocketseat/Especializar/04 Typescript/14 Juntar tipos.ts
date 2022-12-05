type Profile = {
    id: number,
    name: string
}

type Char = {
    nickname: string,
    level: number
}

// Quero juntar esses dois tipos

type Playerinfo = Profile & Char

let player: Playerinfo = {
    "Crtl + Space (Aparece todas as propriedades dos dois tipos)"
}