# Principais exercícios

 Principais exercícios do `Mundo 1 de python`, com descrições dos exercícios e do raciocínio lógico usado para o desenvolvimento do upgrade de cada exercício.
<hr>

## Ex001 → Welcome
<div>
  <img src="https://github.com/franssa01/Courses/blob/main/Curso%20em%20V%C3%ADdeo/Python%20World/World%201/%26%20-%20Image/ex001.jpeg">
</div>

* O primeiro exercício do curso, já começamos a usar `inputs` como forma de interação como o usuário, fazendo com que a variável `name` recebesse o valor inserido no input, que por sinal o tipo foi especificado usando o `str(input("..."))`, para fazer uma possível conversão de tipos, que nesse caso não tinha necessidade. E no print mostramos a diferença entre o `.format()` e o método mais moderno da `f"{}"`, mais simples, legível e menor.

<hr>
<br>

## Ex009 → Times Table
<div>
  <img src="https://github.com/franssa01/Courses/blob/main/Curso%20em%20V%C3%ADdeo/Python%20World/World%201/%26%20-%20Image/ex009.jpeg">
</div>

* Trocando os diversos comandos (com baixíssima eficácia) de `print()` por uma versão usando o `for .. in range()`, que conseguiria resolver esse exercício e uma tabuada muito mais complexa mesmo com poucas linhas. E ainda sim incrementei esse `for .. in range()` dentro de uma função `def times_table`, que ao ser chamada, dá a possibilidade do usuário escolher o número que quer ver a tabuada e até quantas vezes deseja que aquele número seja multiplicado.

<hr>
<br>

## Ex014 → Cash or Installments
<div>
  <img src="https://github.com/franssa01/Courses/blob/main/Curso%20em%20V%C3%ADdeo/Python%20World/World%201/%26%20-%20Image/ex014.jpeg">
</div>

* Colocando o `For .. in range()` novamente para trabalhar ao nosso favor, com a sutíl diferença de que agora é possível fazer o cálculo de muitos e muitos `juros` de acordo com a `quantidade máxima de parcelas` que será estabelecida pelo usuário, retornando para o mesmo o `disconto de 10%` caso ele queira pagar à vista ou o `acréscimo de 8%` referente a cada parcela. 

<hr>
<br>

## Ex015 → Converter Temperature
<div>
  <img src="https://github.com/franssa01/Courses/blob/main/Curso%20em%20V%C3%ADdeo/Python%20World/World%201/%26%20-%20Image/ex015.jpeg">
</div>

* Esse é um exemplo de que um `código menor nem sempre é melhor`. Colocar os códigos dentro de funções permite que seu código fique `mais organizado e legível`, tendo até uma possibilidade da `criação de um módulo que contém diversas funções voltadas só para conversão de temperaturas`, nesse caso foi feita somente do fahrenheit, mas ao saber das regras de conversão era possível ser feita para qualquer temperatura.
<hr>
<br>

## Ex016 → Car Rent
<div>
  <img src="https://github.com/franssa01/Courses/blob/main/Curso%20em%20V%C3%ADdeo/Python%20World/World%201/%26%20-%20Image/ex016.jpeg">
</div>

* Trabalhando novamente com funções, porém agora com `múltiplos parâmetros` (definidos como padrão 0 cada um), que a função mostrará quando o cliente deverá pagar após usar o `serviço de aluguel`. E a função quando chamada fará um `input específico` para cada parâmetro.

<hr>
<br>

## Ex020 → Prize Draw
<div>
  <img src="https://github.com/franssa01/Courses/blob/main/Curso%20em%20V%C3%ADdeo/Python%20World/World%201/%26%20-%20Image/ex020.jpeg">
</div>

* Um `For .. in Range()` de 0 até um número que o usuário estipulou como a quantidade de nomes que vai querer inserir, essa é a diferença da `versão limitada` do lado esquerda. Ele faz o trabalho de fazer a lista `names = []` criada no escopo global receber o `.append()` do input preenchido pelo usuário, e no final o programa escolhe um nome aleatório dentro da lista usando o `método choice` importado da biblioteca random.

<hr>
<br>

## Ex021 → Prize Draw Presentation
<div>
  <img src="https://github.com/franssa01/Courses/blob/main/Curso%20em%20V%C3%ADdeo/Python%20World/World%201/%26%20-%20Image/ex021.jpeg">
</div>

* Semelhante ao exercício anterior, só que nesse foi necessário importar o `método shuffle` que retorna a `lista embaralhada`, retornando a ordem de apresentação, e não escolhendo apenas um nome. Temos a versão aprimorada do meio que eu inseri vários `loops de verificação` com a intenção de previnir que o sistema seja burlado e que só aceite os valores esperados, pergunta se realmente deseja salvar o usuário e para cada resposta preenchida com "Y" é feito um `.append()` para a lista `names = []` que está no `escopo global`, e também permite inserir mais nomes enquanto a opção de continuar for preenchida com "Y". Já a versão do canto direito é uma função que recebe como parâmetro o número que representa a `quantidade de nomes` que o usuário vai querer colocar, e que no final também devolve a `ordem de apresentação`.

<hr>
<br>

## Ex025 → Name of the city
<div>
  <img src="https://github.com/franssa01/Courses/blob/main/Curso%20em%20V%C3%ADdeo/Python%20World/World%201/%26%20-%20Image/ex025.jpeg">
</div>

* Uma simples, porém interessante `manipulação de strings`. O usuário recebe um `str(input))` para colocar o nome da cidade que deseja consultar, o programa irá verificar se o nome da cidade `começa com "SANTO"`. Para isso é necessário evitar erros, e por isso usamos o `.strip() e o .upper() ao lado do input` assim como em vários exercícios, que elimina os espaços desnecessários e o `.upper()` permite que o valor seja igualmente comparado ao "SANTO" do If. `E sabendo que "SANTO" possui os index de 0 à 4`, basta fazer uma condição de que se `nome[:5] == "SANTO"`, e se a resposta for `True` é porque os primeiros 4 index da cidade inserida começam com essa palavra.
<hr>
<br>

## Ex029 → IA
<div>
  <img src="https://github.com/franssa01/Courses/blob/main/Curso%20em%20V%C3%ADdeo/Python%20World/World%201/%26%20-%20Image/ex029.jpeg">
</div>

* Tinhamos um exercício interessante e com uma dificuldade razoável para ser elaborado, afinal foi o primeiro "mini-game" que fizemos, eu apenas acrescentei a possibilidade de continuar jogando tanto na vitória quanto na derrota e a possibilidade de parar, e a cada jogada também é exibido o placar, e ao final do jogo é verificado quem foi o vencedor. 

<hr>
<br>

## Ex034 → Higher / Smaller Number
<div>
  <img src="https://github.com/franssa01/Courses/blob/main/Curso%20em%20V%C3%ADdeo/Python%20World/World%201/%26%20-%20Image/ex034.jpeg">
</div>

* Diversos If's trocados por uma função que recebe como parâmetro a `quantidade de números que o usuário quer analizar`, e para um `For .. in Range()` de 0 até a quantidade máxima `estabelecida pelo usuário`, a cada loop a lista `numbers = []` recebe um `.append()`. E no final usamos dois métodos prontos que facilitam e muito a nossa vida,  `min(mínimo)` e `max(máximo)`, então verificamos o min/max dentro da lista e retornamos.

<hr>
<br>
