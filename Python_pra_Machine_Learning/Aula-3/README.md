# Oficina Aula 3

Depois de ter estudado sobre NumPy e seus arrays, o que você acha de colocar em prática tudo isso que você aprendeu? Ótimo, vamos lá!

Etapa 1
Suponha a seguinte situação: você conseguiu um emprego no Instagram como cientista de dados. A sua chefe pediu que você analisasse as visualizações diárias de stories da última semana para uma lista de pessoas. O intuito é atualizar o algoritmo de sugestão do aplicativo para promover as pessoas que mais tiveram visualização nos stories. Seguem os dados abaixo:

```python
visualizacao_stories = [
    [187, 120, 88, 70, 130, 168, 213],
    [0, 0, 42, 0, 0, 55, 77],
    [91, 0, 61, 0, 71, 121, 271],
    [0, 0, 0, 0, 187, 0, 0],
    [42, 23, 34, 0, 39, 29, 36]
]
pessoas = ['Raquel', 'Lucas', 'Daniel', 'Natalia', 'Anderson']
dias_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
```

Os dados estão organizados da seguinte forma: a primeira linha se refere aos stories da Raquel; a segunda, aos do Lucas; e assim por diante. Com relação às colunas, a primeira coluna são os stories do Domingo, em seguida, os stories da Segunda e assim por diante até a última coluna, que se refere ao Sábado.

Sabendo disso, a sua chefe espera que você retorne algumas informações para ela até o fim do dia. Qual a média de visualizações por dia de todas essas pessoas? Qual o dia que teve mais visualizações de stories somadas? Quem foi que teve o maior número de visualizações na última semana?

Para esta primeira etapa da oficina, você deve responder a essas perguntas com base nos seus estudos. Caso tenha dúvidas, retorne ao conteúdo da aula e fique à vontade para pesquisar.

Etapa 2
Depois de sua chefe ficar empolgada com os resultados que você conseguiu, ela pediu pra você analisar as visualizações dos stories dessa semana. Porém, o sistema de coleta apresentou defeitos e não conseguiu registrar os stories sem visualização como 0. Os dados obtidos estão dispostos abaixo:

```python
visualizacao_stories_invalidos = np.array([
    [52, 68, 97, 55, -1, 98, -1],
    [53, -1, 38, -1, -1, 72, 49],
    [88, -1, 64, -1, 77, 130, 43],
    [-1, 30, -1, -1, -1, 182, -1],
    [41, 20, 33, -1, 37, 23, 7]
])
```

Note que o sistema de coleta da sua chefe produziu erros ao obter informações de dias que não conteve stories. Você deve considerar inválidos os valores com -1.

A sua chefe quer que você realize a análise considerando todos os dados das últimas duas semanas. Considerando isso, você deve responder às mesmas questões da etapa anterior.

Boa prática!
