/*

    Baseado no array de livros por Categoria abaixo, faça os seguintes desafios:

    * Contar o número de categorias e o número de livros em cada categoria
    * Contar o número de autores
    * Mostrar Livros do autor Augusto Cury
    * Transformar a função acima em uma função que irá receber o nome do autor e devolver os livros desse autor
*/

const booksByCategory = [
    {
        category: "Riqueza",
        books: [
            {
                title: "Os segredos da mente milionária",
                author: "T. Harv Eker",
            },
            {
                title: "O Homem mais rico da babilônia",
                author: "George S. Clason",
            },
            {
                title: "Pai rico, pai pobre",
                author: "Robert Kiyosaki",
            }
        ]
    },

    {
        category: "Inteligência Emocional",
        books: [
            {
                title: "Você é insubstituível",
                author: "Augusto Cury",
            },
            {
                title: "Ansiedade - Como enfrentar o mal do século",
                author: "Augusto Cury",
            },
            {
                title: "Os 7 hábitos das pessoas altamente eficazes",
                author: "Stephen R. Covey",
            }
        ]
    },
]

let categories = booksByCategory.length

// Número de autores

let authors1 = 0

for (const key in booksByCategory) {
    for (const collection of booksByCategory[key].books) {
        authors1 += 1
    }
} // Dessa forma não filtra autores repetidos

let authors = []

for (const category of booksByCategory) {
    for (const book of category.books) {
        if (!authors.includes(book.author)) {
            authors.push(book.author)
        }
    }
} // Se no array de autores não tiver  autor da vez, adicione ele no array

console.log(authors)


// Mostrar livros do autor Augusto Cury

for (const key in booksByCategory) {
    for (const element of booksByCategory[key].books) {
        if (element.author == "Augusto Cury")
            console.log(element.title)
    }   
}

// Uma função que recebe o nome do autor e retorna os livros dele

function livrosDe(autor) {
    for (const key in booksByCategory) {
        for (const element of booksByCategory[key].books) {
            if (element.author == autor) {
                console.log(element.title)
            }
        }
    }
}

// livrosDe("Augusto Cury")

