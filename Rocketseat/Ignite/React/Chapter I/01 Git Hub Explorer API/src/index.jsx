import React from "react";
import { render } from "react-dom";
import { App } from "./App";

// vamos chamar essa função render importada e dizer o que queremos renderizar
// vai renderizar um h1 dentro do elemeto que selecionamos
// render(<h1>Teste</h1>, document.querySelector("#root"))

// Em vez de renderizarmos o H1, vamos renderizar nosso componente APP que importamos, e do index.jsx enviamos para o root no index.html para ser renderizado.

render(<App />, document.querySelector("#root"))