# Navegando Pelo Terminal (macOS)

![Fonte: http://twentyeighttwelve.com/tron-legacy-command-line/](tron-legacy-grep.jpg){.center}

Você já deve ter visto em algum filme uma cena como a mostrada acima: [um "hacker" digita comandos freneticamente em uma interface onde só aparecem comandos de texto ininteligíveis até que magicamente ele obtém os dados que todos julgavam ser impossível obter](http://hackertyper.com/). Interfaces de linha de comando podem assustar um pouco no começo, mas veremos que sabendo apenas 2 comandos já é possível utilizá-las para navegar pelos arquivos do computador.

Talvez você nunca tenha aberto o terminal/console/prompt do seu computador, mas ele está ([e sempre esteve](https://en.wikipedia.org/wiki/Command-line_interface)) lá! Vamos começar abrindo o terminal no nosso computador.

## Abrindo o Terminal

!!! warning "Atenção"
    A partir deste ponto existem algumas diferenças entre os sistemas operacionais. **Este handout foi desenvolvido para usuários Mac OS X**. Se você usa Windows, consulte o [outro handout disponibilizado](../terminal-win).

Temos duas opções:

1. Abra a pasta *Applications*, depois abra a pasta *Utilities* dentro dela e então dê um duplo clique em *Terminal*;
1. Pressione ++command+space++ para lançar o *Spotlight Search*, digite *Terminal* e aperte ++return++.

![Uma janela parecida com essa deve aparecer ao abrir o terminal](osx-term0.png){width=50% .center}

Não vamos entrar em detalhes por enquanto, mas tudo o que aparece antes do \$ são informações como: o nome do seu usuário, em que pasta você está atualmente. Por enquanto você só precisa saber que os comandos são digitados depois do \$.

## O comando `ls`

Vamos começar pelo comando `ls`. Digite `ls` e aperte a tecla ++return++:

![Resultado do comando `ls`](osx-term1.png){width=50% .center}

O comando `ls` lista os arquivos e pastas presentes na pasta atual. Funciona mais ou menos assim: imagine que você é um personagem de um jogo em uma sala (a pasta atual) com diversas informações (arquivos) e algumas portas (outras pastas). Todos os comandos que você executar serão executados na pasta atual. Por enquanto, vamos considerar duas possibilidades de ação:

1. Visualizar os arquivos disponíveis da pasta atual;
2. Navegar para outra pasta.

O comando `ls` realiza a primeira opção. Se você não mudou nenhuma configuração do terminal você sempre começa na pasta do seu usuário (também conhecida como sua *home* e é abreviada pelo símbolo "`~`" no terminal). Para verificar que o comando listou os arquivos e pastas disponíveis, vamos abrir o Finder na mesma pasta:

![Conteúdo da *home*](osx-finder1.png){width=50% .center}

## O comando `cd`

Agora vamos tentar a segunda opção: navegar para outra pasta. Para isso usamos o comando `cd`. Ele deve ser seguido do nome da pasta. Vamos entrar na pasta `insper` listada acima. Para isso vamos usar o comando `cd insper`.

<div class="alert">
Os arquivos no seu computador provavelmente serão diferentes dos arquivos deste exemplo.
</div>

<div class="alert">
Os comandos executados anteriormente não são apagados.
</div>

![Executando o comando `cd`](osx-term2.png){width=50% .center}

O comando `cd` não imprime nada no terminal. Esse é o resultado esperado. Vamos visualizar o conteúdo da pasta `insper`. Para isso, mais uma vez usamos o comando `ls`:

![Resultado do comando `ls` na pasta `insper`](osx-term3.png){width=50% .center}

Vemos que essa pasta contém o arquivo `calendario.txt` e diversas pastas com nomes de disciplinas. Vamos entrar na pasta `design-de-software`. Mas antes disso, você notou que, na pasta atual, `design-de-software` é a única pasta que começa com as letras `des`? Além disso, o terminal acabou de listar as pastas, então em teoria ele "sabe" quais são as pastas e arquivos disponíveis. Não seria bom se eu pudesse escrever só o começo do nome da pasta e o terminal já completasse com o resto? E sim, ele faz isso! Podemos, por exemplo, digitar somente `cd des`:

![Digitando apenas `cd` e o começo do nome da pasta](osx-term4.png){width=50% .center}

Depois disso, ao apertar a tecla ++tab++, o terminal vai completar o comando com o resto do nome:

![O terminal completa o nome da pasta quando não há ambiguidade](osx-term5.png){width=50% .center}

No nosso exemplo, dentro da pasta `design-de-software` existe uma pasta `aulas`, que contém outras duas pastas `aula01` e `aula02`, que por sua vez contém 4 arquivos.

![Conteúdo da pasta `design-de-software`](osx-finder2.png){width=50% .center}

Pode ser um pouco cansativo usar um comando separado para entrar em cada pasta, ainda mais se você já souber o caminho completo. Por isso, também podemos avançar mais de um nível no comando `cd`, separando os nomes das pastas com uma barra ('/'):

![Podemos usar o comando `cd` com um caminho mais longo](osx-term6.png){width=50% .center}

Para verificar que estamos no lugar certo vamos usar, mais uma vez, o comando `ls`:

![Resultado do comando `ls` na pasta `insper/design-de-software/aulas/aula02`](osx-term7.png){width=50% .center}

Finalmente, podemos também voltar para pastas acima da pasta atual. Para isso usamos o `..`, que se refere à pasta mãe. Por exemplo:

![Usando o `cd ..` para subir um nível](osx-term8.png){width=50% .center}

Vemos que agora estamos na pasta `aulas`:

![Usando `ls` para ver o conteúdo](osx-term9.png){width=50% .center}

Podemos também compor o `..` no caminho de uma pasta. Por exemplo: `../..` são dois níveis acima da pasta atual.

![Combinando o `..` em um caminho mais complexo](osx-term10.png){width=50% .center}

Assim, depois de executar `cd ../..` vemos que estamos novamente na pasta `insper`:

![Verificando que estamos na pasta `insper`](osx-term11.png){width=50% .center}
