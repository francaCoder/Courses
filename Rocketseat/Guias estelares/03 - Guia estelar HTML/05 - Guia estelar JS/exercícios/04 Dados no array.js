/* 
Buscando e contandos dados em Arrays

Baseado no array de livros por categoria abaixo, faça os seguintes desafios:

* Contar o número de categorias e o número de livros em cada categoria 
* Contar o número de autores
* Mostrar livros do Autor Augusto Cury
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
                title: "O homem mais rico da Babilônia",
                author: "George S. Clason",
            },
            {
                title: "Pai Rico, Pai Pobre",
                author: "Robert T. Kiyosaki",
            },
        ],
    },
    {
        category: "Inteligência emocional",
        books: [
            {
                title: "Você é insubstituível",
                author: "Augusto Cury",
            },
            {
                title: "Como enfrentar o mal do século",
                author: "Augusto Cury",
            },
            {
                title: "Os 7 hábitos das pesoas altamente eficazes",
                author: "Stephen R. Covey"
            }

        ],
    },
]

const totalCategories = booksByCategory.length

console.log(totalCategories)
for (const category of booksByCategory) {
    console.log(`Total de livros da categoria ${category.category}`)
    console.log(category.books.length) // Total de books da categoria
}

function countAuthors() {
    let authors = []

    for (const category of booksByCategory) {
            for(const book of category.books) { // É um array que eu estou     extraindo dele um objeto e chamando de book
                if(authors.indexOf(book.author) == -1 ) {
                    authors.push(book.author) // Estou alimentendo o array vazio com os livros
            }
        }
    }

    console.log(`Total de autores: ${authors.length}`)
}

countAuthors()


function booksOfAuthor(author) {

    for (const category of booksByCategory) {
            for(const book of category.books) { // É um array que eu estou     extraindo dele um objeto e chamando de book
                if(book.author == author) {
                    books.push(book.title) // Estou alimentendo o array vazio com os livros desse autor
            }
        }
    }

    console.log(`Livros do autor ${author}: ${books. join(", ")}`)
}

booksOfAuthor("Augusto Cury")