'''
 Passo a passo do projeto:

1- Abrir o sistema da empresa


2- Fazer login 

3 - Abrir/importar a base de dados de produtos para cadastrar

4 - cadastrar um produto

5: - Repetir isso tudo até acabar a lista de produtos

'''
import pyautogui as pa 
import pandas as pd
import time 
pa.PAUSE = 0.5 

# Passo 1 
# Acessar o sistema em minha máquina
pa.press('win')
# abrir o navegador (chome)
pa.write('Chrome')
pa.press('enter')
# abrir o siste do sistema de cadastro 
pa.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pa.press('enter')
time.sleep(3)

# passo2
# Clicar no campo de login
pa.click(x=918, y=349)
# Preencher o campo
pa.write('guigui@gmail.com')
# passar para próximo campo
pa.press('tab')
# digitar a senha 
pa.write(str(12345678910))
# passar para o botão
pa.press('tab')
pa.press('enter')

# Passo3 
# abrir os produtos no arquivo csv com pandas
tabela = pd.read_csv('.\produtos.csv')

# Passo 4
# Cadastrar produto, preenchendo campo por campo

# clicar no campo do código do produto

for linha in tabela.index:

		codigo_values = str(tabela.loc[linha, 'codigo'])
		mark_values = str(tabela.loc[linha, 'marca'])
		type_values = str(tabela.loc[linha, 'tipo'])
		category_values= str(tabela.loc[linha, 'categoria'])
		preco_values = str(tabela.loc[linha, 'preco_unitario'])
		custo_values = str(tabela.loc[linha, 'custo'])
		obs_values= str(tabela.loc[linha, 'obs'])
		pa.click(x=743, y=244)
		
		# preencher o código 
		pa.write(codigo_values)
		# passar para o próximo campo
		pa.press('tab')
		
		# marca 
		pa.write(mark_values)
		# passar para próximo campo 
		pa.press('tab')

		# tipo
		pa.write(type_values)
		# passar para próximo campo 
		pa.press('tab')
		 
		# categoria 
		pa.write(category_values)
		# passar para próximo campo 
		pa.press('tab')
		
		# preço
		pa.write(preco_values)
		# passar para próximo campo 
		pa.press('tab')
		
		# custo
		pa.write(custo_values)
		# passar para próximo campo 
		pa.press('tab')
		
		# obs
		obs = str(tabela.loc[linha, 'obs'])
		if obs != 'nan': 
			pa.write(obs_values)
		# passar para próximo campo 
		pa.press('tab')
		
		# apertar botao
		pa.press('enter')
		
		# Voltar ao inicio
		pa.scroll(1000)
		pa.click(x=743, y=2442)

		break
		 
		 # codigo da aula:  aprendapython