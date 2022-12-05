import "./style.css"

export function Card(props) {
    // Ou posso desestruturar o props
    // Card({name, time})
    // E dentro das tags eu colocaria apenas {name} e {time}
    return(
        // Preciso resgatar cada propriedade que eu coloquei nos cartões para que eles sejam renderizados automaticamente
        <div className="card">
            <strong>{props.name}</strong>
            <small>{props.time}</small>
        </div>
    )
}