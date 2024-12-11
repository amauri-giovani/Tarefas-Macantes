#! python3 
#quiz.py - Cria provas com perguntas e respostas em ordem aleatória, juntamente com os gabaritos contendo as respostas.

import random																#Importa o módulo random para embaralhar as provas.

#Os dados para as provas. As chaves são os estados e os valores são as capitais.
capitals = {'Acre':'Rio Branco', 'Alagoas':'Maceió', 'Amapá':'Macapá', 'Amazonas':'Manaus', 'Bahia':'Salvador', 'Ceará':'Fortaleza', \
'Distrito Federal':'Brasília', 'Espírito Santo':'Vitória', 'Goiás':'Goiânia', 'Maranhão':'São Luís', 'Mato Grosso':'Cuiabá', \
'Mato Grosso do Sul':'Campo Grande', 'Minas Gerais':'Belo Horizonte', 'Pará':'Belém', 'Paraíba':'João Pessoa', 'Paraná':'Curitiba', \
'Pernambuco':'Recife', 'Piauí':'Teresina', 'Rio de Janeiro':'Rio de Janeiro', 'Rio Grande do Norte':'Natal', 'Rio Grande do Sul':'Porto Alegre', \
'Rondônia':'Porto Velho', 'Roraima':'Boa Vista', 'Santa Catarina':'Florianópolis', 'São Paulo':'São Paulo', 'Sergipe':'Aracaju', 'Tocantins':'Palmas'}

#Gera 18 arquivos contendo as provas.
for quiznum in range(18):
	#Cria os arquivos com as provas e os gabaritos das respostas.
	quizFile = open('capitalsquiz%s.txt' %(quiznum + 1), 'w')				#Cria os arquivos de perguntas.
	answerFile = open('capitalsquiz_answers%s.txt' %(quiznum + 1), 'w')		#Cria os arquivos de respostas.

	#Escreve o cabeçalho da prova.
	quizFile.write('Nome:\n\nData:\n\n\n\n')		#Escreve no arquivo da prova os dados para o aluno preencher.
	quizFile.write(('' * 20) + 'Quiz de estados e capitais (Prova %s)' % (quiznum + 1))		#Escreve no arquivo da prova o título da prova.
	quizFile.write('\n\n\n')		#Pula 3 linhas no arquivo da prova.

	#Embaralhaa ordem dos estados.
	states = list(capitals.keys())											#Armazena na variável "states" as chaves (estados) 
	random.shuffle(states)													#Embaralha a ordem da lista "states"

	#Percorre todos os 27 estados em um loop. criando uma pergunta para cada um.
	for questionNum in range(27):
		#Obtém respostas corretas e incorretas.
		respcorreta = capitals[states[questionNum]]							#Armazena na variável "respcorreta" a chave(estado) começando em zero até 26.
		resperradas = list(capitals.values())								#Armazena na variável "resperradas" todas as respostas(capitais).
		del resperradas[resperradas.index(respcorreta)]						#Deleta a resposta correta da lista "resperradas".
		resperradas = random.sample(resperradas, 3)							#Seleciona aleatoriamente 3 respostas(capitais) erradas.
		respopcoes = resperradas + [respcorreta]							#Armazena na variável "respopcoes" as 3 respostas erradas + a resposta correta.
		random.shuffle(respopcoes)											#Embaralha as 4 alternativas para não gerar a mesma letra como resposta.

		#Grava a pergunta e as opções de resposta no arquivo de prova.
		quizFile.write('\n%s. Qual é a capital de %s?\n' %(questionNum + 1, states[questionNum]))	#Escreve a pergunta no arquivo da prova.
		for i in range(4):													#faz um loop para as 4 alternativas.
			quizFile.write('     %s. %s' %('ABCD'[i], respopcoes[i]))		#Grava alguns espaços, as letras das alternativas de A a D e as capitais.
			quizFile.write('\n')											#Pula uma linha para a próxima pergunta.


		#Grava o gabarito com as respostas em um arquivo.
		answerFile.write('%s. %s\n' %(questionNum + 1, 'ABCD'[respopcoes.index(respcorreta)]))	#Escreve no arquivo o gabarito com as respostas.

quizFile.close()															#Fecha o arquivo da prova.
answerFile.close()															#Fecha o arquivo das respostas.