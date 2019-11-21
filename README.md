# jogo-da-velha-python
Avaliação 1 disciplina de Inteligência artificial 2019/2


**Exe1:** Implemente um programa que insira valores em uma lista encadeada. Considere que os valores a serem inseridos estão inicialmente armazenados em uma matriz.

**Exe 2:** Implemente um programa que adicione valores (a partir de uma lista de valores) como nós em uma árvore binária de forma ordenada, partindo da raiz da árvore. Considere que:
- Se o nó não existir, deve-se criar o nó e armazenar o valor;
- Se o nó existir, deve-se comparar o valor a ser inserido com o valor do nó;
- Se o valor for maior ou igual ao valor do nó, adicionar como filho direito deste
nó;
- Se o valor for menor que o valor do nó, adicionar como filho esquerdo deste nó;
- Se o filho a ser criado já existir, repetir a comparação do valor com este filho, eassim sucessivamente, até que o filho a ser criado não exista; neste caso cria-se o nó e adiciona-se o valor;
- Deve ser possível localizar um valor na árvore e obter como retorno um ponteiro para o nó com este valor;

**Exe3:** Faça um programa para gerar uma árvore com todas as possibilidades de tabuleiro para uma partida de jogo da velha;
- Represente cada tabuleiro como um vetor de 9 posições, onde são representadas as linhas do tabuleiro `{1,2,3,4,5,6,7,8,9}`;
- em cada posição pode ter `‘O’,’X’ ou ‘ ‘`;

**Exe4:** Modificar o programa de geração da árvore do jogo da velha para:
- marcar as posições de fim de jogo;
- identificar quem foi o vencedor;
- Identificar o caminho que levou a uma dada situação de fim de jogo;

**Exe5:** Adicionar a cada nó o peso da heurística apresentada em aula (diferença entre alinhamentos da peça do jogador 1 e jogador 2); Percorrer a árvore escolhendo a jogada com base no valor da heurística para o jogador 1
e entrada via teclado para o jogador 2;
