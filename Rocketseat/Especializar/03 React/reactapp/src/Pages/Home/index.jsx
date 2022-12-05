import React, { useState } from "react"
import "./style.css"
import { Card } from "../../components/Card"
// { useState } é o hook que permite que a gente crie os estados

// quando usamos o export sem o default, temos que ir no main e colocar o Home entre { }
export function Home() {
  // let studentName = ""
  // // Uma variável comum não tem o poder de refletir na nossa interface, por isso vamos usar estado

  // function handleNameChange(name) {
  //   studentName = name
  // }

  // 1º elemento - Nome do estado (lugar onde seu conteúdo vai ficar armazenado)
  // 2º elemento - Função que atualiza esse estado
  // Estado serve para armazenar valores que vão ser utilizados na sua interface em tempo real

  const [studentName, setStudentName] = useState()

  return (
    <div className="container">
      <h1>Nome: {studentName}</h1>
      <input 
        type="text" 
        placeholder="Digite o nome..."
        onChange={event => setStudentName(event.target.value)}
        />
        {/* Estou passando o conteúdo atual do input, e toda vez que é inserido um novo caracter ele envia novamente */}
      <button type="button">Adicionar</button>

      {/* Adicionando os componentes e Passando propriedades*/}
      {/* Porém nossos cards continuam fixos, a ideia é que depois que o usuário insira seu nome no input, a gente adicione e crie um novo card com essas informações*/}
      <Card name="Matheus" time="10:55:25"/>
      <Card name="João" time="11:15:02" />
      <Card name="Ana" time="12:10:32" />
    </div>
  )
}

// A regra é que temos que devolver somente um elemento

// Usando o fragment ( <> </> ) o retorno da nossa função devolve apenas um pacote, mas também podemos usar uma div

// export default Home
