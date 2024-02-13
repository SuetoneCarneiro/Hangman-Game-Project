from os import system  #limpar terminal = system("clear")
from random import choice
from time import sleep

import emoji  #permite o uso de icon pelo nome

tamanho = 40  #constante para fazer prints no menu


def menu_da_forca():
  '''
  -> Essa função gera o menu que dá início ao nosso programa. Ela não recebe parâmetros.

  O menu direciona o jogador a sua opção escolhida.

  :return: função sem retorno
  '''
  print('¬' * tamanho)
  print(f"{'Jogo da forca':^{tamanho}}")
  print('¬' * tamanho)
  print(f"{'MENU PRINCIPAL':^{tamanho}}")
  print(f'{"-"*tamanho}')
  print(f"{'[1] - Jogar':^{tamanho}}")
  print(f"{'[2] - Regras':^{tamanho}}")
  print(f"{'[3] - Sair  ':^{tamanho}}")
  print(f'{"-"*tamanho}')
  opcao = input('Sua opção\n>> ')
  while opcao not in '123':
    print(
        '\033[31mERRO!\nOpção inválida. Escolha uma das opções do menu.\033[m')
    opcao = input('\nSua opção\n>> ')
  else:
    if opcao == '1':
      system("clear")
      jogo()
    elif opcao == '2':
      system("clear")
      regras()
    else:
      system("clear")
      print('\033[32mObrigado por jogar!\032')
      exit()


def regras():
  '''
  -> Essa função serve para o usuário saber as regras do jogo.

  Ela apenas abre um arquivo com as regras, mostra o conteúdo e fecha o arquivo.

  :return: função sem retorno.
  '''
  file_name = 'regras.txt'
  system("clear")
  with open(file_name, 'r') as arquivo:
    print(f'{"-"*tamanho*2}')
    conteudo = arquivo.read()
    print(conteudo)
    print(f'{"-"*tamanho*2}')
  input('\nPressione ENTER para voltar ao menu.')
  system("clear")
  menu_da_forca()


def nickname_check(nickname):
  '''
  -> Essa função serve para verificar se o nickname já existe no nosso banco de jogadores.
  Caso já exista, a função retorna o nome.
  Caso não exista, a função cria um  novo nickname com a pontuação zerada e retorna o nome.
  :parametro: nickname: nome do jogador, existente ou não no nosso banco.
  :return: o nome do jogador.
  '''
  with open('banco_de_jogadores.txt', 'r') as jogadores:
    for linha in jogadores:
      if nickname in linha:
        linha = linha.split(';')
        return linha[0]  # linha[0] = nome
  with open('banco_de_jogadores.txt', 'a') as jogadores:
    jogadores.write(f'{nickname};{0};{""}\n')

  with open('banco_de_jogadores.txt', 'r') as jogador:
    for linha in jogador:
      if nickname in linha:
        linha = linha.split(';')
        return linha[0]


def deseja_continuar(nickname):
  '''
  -> Essa função serve para o usuário escolher se quer continuar jogando ou não
  :parametro nickname: nome do jogador
  :return: função sem retorno
  '''
  print('¬' * tamanho)
  print('''
  1) Jogar novamente
  2) Checar pontuação e sair
  ''')
  opcao = input('>> ')
  if opcao == '1':
    system("clear")
    jogo(nickname)
  else:
    system("clear")
    print('\033[36mObrigado por jogar!\032')
    with open('banco_de_jogadores.txt', 'r') as jogadores:
      arq = jogadores.readlines()
      for linha in arq:
        if nickname in linha:
          pontuacao = linha.split(';')[1]
          print(f'\033[36mSua pontuação atual é {pontuacao} pontos 😄')
    exit()


def zerando_o_jogo(nickname):
  '''
  -> Essa função checa se o jogador já adivinhou todas as palavras do banco de palavras.
  Caso sim, a função parabeniza, mostra a pontuação e retira o jogador do banco de jogadores.
  :parametro nickname: nome do jogador
  :return: função sem retorno
  '''
  cont_tamanho = 0
  arquivo_tam = open('banco_de_palavras.txt', 'r')
  for linha in arquivo_tam:
    if linha != '\n':  # linhas em branco não são contabilizadas
      cont_tamanho += 1
  arquivo_tam.close()
  with open('banco_de_jogadores.txt', 'r') as jogadores:
    for linha in jogadores:
      if nickname in linha:
        pontuacao_final = linha.split(';')[1]
        palavras_adivinhadas = linha.split(';')[2]
        palavras_adivinhadas = palavras_adivinhadas.replace("'", '').replace(
            '\n', "")
        palavras_adivinhadas = palavras_adivinhadas.split(',')
        tam = len(palavras_adivinhadas)
        tam -= 1  # 2
        palavras_adivinhadas.pop(tam)
        if tam == cont_tamanho:
          system("clear")
          print('\033[1;30;42m  PARABÉNS! Você zerou o Jogo da Forca  ')
          print(
              f'\n\033[1;30;46m  Você fez um total de {pontuacao_final} pontos '
          )
          #Apagando o jogador do arquivo depois que ele zera:
          try:
            with open('banco_de_jogadores.txt', 'r') as fr:
              lines = fr.readlines()
              with open('banco_de_jogadores.txt', 'w') as fw:
                for line in lines:
                  # strip() is used to remove '\n'
                  # present at the end of each line
                  if line.strip('\n') != linha.strip('\n'):
                    fw.write(line)
                exit()
          except:
            exit()


def boneco_forca(cont_erros):
  '''
  -> Essa função gera o boneco da forca de acordo com a quantidade de erros do jogador.
  :parametro cont_erros: quantidade de erros do jogador
  :return: função sem retorno
  '''
  if cont_erros == 0:
    print("┌───┐")
    print("|   ")
    print("|    ")
    print("|    ")
    print("|    ")
  elif cont_erros == 1:
    print("┌───┐")
    print(f"|   {emoji.emojize(':zany_face:')}")
    print("|    ")
    print("|    ")
    print("|    ")

  elif cont_erros == 2:
    print("┌───┐")
    print(f"|   {emoji.emojize(':zany_face:')}")
    print("|   |")
    print("|    ")
    print("|    ")

  if cont_erros == 3:
    print("┌───┐")
    print(f"|   {emoji.emojize(':zany_face:')}")
    print("|   /|")
    print("|    ")
    print("|    ")

  if cont_erros == 4:
    print("┌───┐")
    print(f"|   {emoji.emojize(':zany_face:')}")
    print("|   /|\\")
    print("|    ")
    print("|    ")

  if cont_erros == 5:
    print("┌───┐")
    print(f"|   {emoji.emojize(':zany_face:')}")
    print("|   /|\\")
    print("|    /")
    print("|    ")

  if cont_erros == 6:
    print("┌───┐")
    print(f"|   {emoji.emojize(':zany_face:')}")
    print("|   /|\\")
    print("|    /\\")
    print("|    ")
    print(" Você perdeu! ")


def jogo(nickname='game_nick_padrao'):  #parâmetro opcional
  '''
  -> Essa função é responsável pela lógica do jogo em si.
  Caso o nick name seja passado como parâmetro, o jogo não pede para o jogador digitá-lo.
  :parametro nickname: é uma parâmetro opcional com o nome do jogador.
  :return: função sem retorno
  '''
  #para não pedir nickname caso o jogador jogue novamente
  if nickname == 'game_nick_padrao':
    nick = input('Insira seu nickname: ')
    nick_checado = nickname_check(nick)
  else:
    nick_checado = nickname

  zerando_o_jogo(nick_checado)

  with open('banco_de_palavras.txt', 'r') as arquivo:
    lista_de_linhas = arquivo.readlines()
    linha_sorteada = choice(lista_de_linhas)
    palavra_chave = linha_sorteada.split(';')[0]
    #checando se a palavra já foi adivinhada
    with open('banco_de_jogadores.txt', 'r') as jogadores:
      for linha in jogadores:
        if str(nick_checado) in linha:
          palavras_adivinhadas = linha.split(';')[2]
          palavras_adivinhadas = palavras_adivinhadas.replace("'", '').replace(
              '\n', "")
          palavras_adivinhadas = palavras_adivinhadas.split(',')
          ult = len(palavras_adivinhadas) - 1
          palavras_adivinhadas.pop(ult)
          while (palavra_chave in palavras_adivinhadas):
            linha_sorteada = choice(lista_de_linhas)
            palavra_chave = linha_sorteada.split(';')[0]
    # -----------------------------------------------------------------
    dica = linha_sorteada.split(';')[1].replace('\n', '')
    letras_da_palavra = []
    letras_adivinhadas = []
    letras_erradas = []
  pontos = 0
  cont_erro = 0
  cont_acerto = 0
  while cont_erro <= 6:
    system("clear")
    print('¬' * tamanho)
    print(f"{'Jogo da forca':^{tamanho}}")
    print('¬' * tamanho)
    boneco_forca(cont_erro)
    if len(letras_erradas) == 6:
      deseja_continuar(nick_checado)
    for j in palavra_chave:
      if j not in letras_da_palavra and j != ' ':
        letras_da_palavra.append(j)
    print(f'{"-"*tamanho}')
    print(f'Dica: {dica}')
    print(f'{"-"*tamanho}')
    print()
    if cont_erro > 0:
      print(f'Letras já tentadas: {letras_erradas}')
      print()
    print('Palavra:')
    for i in palavra_chave:
      if i == ' ':
        print('-', end='')
      if i in letras_adivinhadas:
        print(f'{i}', end='')
      if i not in letras_adivinhadas and i != ' ':
        print('_', end='')
    print()
    print()

    letra = str(input('Digite uma letra: ')).lower()

    if letra not in letras_adivinhadas:
      letras_adivinhadas.append(letra)
    else:
      print('\nVocê já tentou essa letra!')
      sleep(3.5)
      continue
    if letra not in palavra_chave:
      cont_erro += 1
      letras_erradas.append(letra)

    if letra in palavra_chave:
      cont_acerto += 1
      pontos += 10

    if cont_acerto == len(letras_da_palavra):
      print()
      print(f'Você acertou, a palavra era {palavra_chave.title()}!')
      print(f'Sua pontuação foi de {pontos} pontos.')
      print()

      with open('banco_de_jogadores.txt', 'r') as players:
        arquivo_em_lista = players.readlines()
      with open('banco_de_jogadores.txt', 'a') as players:
        players.truncate(0)  #apaga conteúdo do arquivo
        for linha in arquivo_em_lista:
          if str(nick_checado) in linha:
            linha_dividida = linha.replace('\n', '').split(';')
            nova_pontuacao = int(linha_dividida[1]) + pontos
            lista_de_palavras = ''
            for i in linha_dividida[2]:
              lista_de_palavras += i
            lista_de_palavras += "'"

            for j in palavra_chave:
              lista_de_palavras += j
            lista_de_palavras += "'"
            lista_de_palavras += ','

            players.write(
                f'{nick_checado};{nova_pontuacao};{lista_de_palavras}\n')
          else:
            players.write(linha)
      zerando_o_jogo(nick_checado)
      deseja_continuar(nick_checado)
      break
