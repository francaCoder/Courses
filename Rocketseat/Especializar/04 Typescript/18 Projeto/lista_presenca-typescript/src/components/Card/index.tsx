import './styles.css';

// Após trocar a extensão do arquivo para tsx, logo abaixo podemos criar um type que vamos atribuílo para o argumento props. Onde obrigará o usuário a colocar um name: string e um time:string
export type CardProps = {
  name: string;
  time: string;
}

export function Card(props: CardProps) {
  return (
    // Após baixar a tipagem do react ele entende o conteúdo do return
    <div className="card">
      <strong>{props.name}</strong>
      <small>{props.time}</small>
    </div>
  )
}