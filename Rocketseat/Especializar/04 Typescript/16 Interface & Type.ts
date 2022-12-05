// Unindo com type

type Tuser = {
    id: number,
    name: string
}

type Tpayment = {
    method: string
}

type Taccount = Tuser & Tpayment

 let user: Taccount = {
    // (Crtl + Space = Suggestions)
}


// Unindo com interface (extends)

interface Iuser {
    id: number,
    name: string
}

interface Ipayment {
    method: string
}

interface Iaccount extends Iuser, Ipayment {}

let newUser: Iaccount = {
    // (Crtl + Space = Suggestions)
}