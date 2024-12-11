Não é magia, é o módulo itertools da biblioteca padrão do Python
Quem ouve falar que Python vem com baterias incluídas, geralmente não imagina que elas estão mais próximas de uma usina nuclear do que de um par de pilhas Rayovale (sim, existe!). Nunca me canso de ficar surpreso toda vez que lembro que existem módulos como o itertools, por exemplo. Passeando pela documentação, é fácil encontrar funcionalidades poderosas, pérolas que podem salvar o dia em alguns minutos quando o seu problema é um desses:

Percorrer os elementos de várias sequências de uma só vez

Com a função `chain() <http://docs.python.org/3/library/itertools.html#itertools.chain>`__, basta fazer:

>>> import itertools
>>> a = [100, 200, 300]
>>> b = ('Newton', 'Einstein', 'Hawking', 'Cooper')
>>> c = 'Python'
>>> for item in itertools.chain(a, b, c):
... 	print item
...
100
200
300
Newton
Einstein
Hawking
Cooper
P
y
t
h
o
n
Calcular a soma acumulada a cada passo da iteração

Vamos supor que uma criança guarda parte de sua mesada num cofrinho todo mês. Com a função `accumulate() <http://docs.python.org/3/library/itertools.html#itertools.accumulate>`__ (Python 3) é possível calcular o valor economizado mês a mês:

>>> import itertools
>>> cofrinho = [10, 12, 15, 5, 7, 0, 20, 13, 9, 0, 1, 16]
>>> for mes, valor\_guardado in
enumerate(list(itertools.accumulate(cofrinho)), start=1):
... print(mes, '= R$', valor\_guardado)
...
1 = R$ 10
2 = R$ 22
3 = R$ 37
4 = R$ 42
5 = R$ 49
6 = R$ 49
7 = R$ 69
8 = R$ 82
9 = R$ 91
10 = R$ 91
11 = R$ 92
12 = R$ 108
Na verdade essa é apenas a funcionalidade mais básica da função accumulate(). É possível passar qual a função que será usada no lugar da soma, permitindo fazer operações muito mais complexas envolvendo séries de elementos. Mais detalhes podem ser vistos na documentação oficial.

Encontrar todas as possíveis combinações entre os elementos de um conjunto

Lembra de análise combinatória na escola? Uma entre as funções do módulo itertools que poderiam nos ajudar na hora do aperto é a `permutations() <http://docs.python.org/3/library/itertools.html#itertools.permutations>`__. Um problema clássico da análise combinatória é encontrar todos os anagramas de uma palavra:

>>> import itertools
>>> [''.join(anagrama) for anagrama in
itertools.permutations('gato')]
['gato', 'gaot', 'gtao', 'gtoa', 'goat', 'gota', 'agto', 'agot',
'atgo', 'atog', 'aogt', 'aotg', 'tgao', 'tgoa', 'tago', 'taog', 'toga',
'toag', 'ogat', 'ogta', 'oagt', 'oatg', 'otga', 'otag']
Esse é só um aperitivo das possibilidades do módulo itertools. A documentação oficial traz, além da referência de todas as funções do módulo, uma seção só com receitas do que se pode construir a partir da combinação das funções. Vale dar uma olhada, pois nunca se sabe quando vai ser necessário usar algo parecido.

Referência

itertools — Functions creating iterators for efficient looping (The Python Standard Library)
