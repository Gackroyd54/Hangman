# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
     def __init__(self,palavra):
          
          self.letras_certas = []
          self.letras_erradas = []
          self.letras_digitadas = []
          self.palavra = palavra
          
          
	# Método para adivinhar a letra
     def adivinha(self,letra):
          self.letras_digitadas.append(letra)
          if letra in self.palavra and letra not in self.letras_certas:
               self.letras_certas.append(letra)
               return True
          elif letra not in self.palavra:
               self.letras_erradas.append(letra)
               return False
          
     
                    
	# Método para verificar se o jogo terminou
     def game_over(self):
          return self.won() or len(self.letras_erradas) == 6

          
	     
          
               
	# Método para verificar se o jogador venceu
     def won(self):
         
          for l in self.palavra:
               if l not in self.letras_certas:
                    return False
               else:
                    return True
	# Método para não mostrar a letra no board
     def hide(self,letter): 
          plc = ''
          for let in self.palavra:
               
               if letter == let: 
                    plc += letter
               elif let in self.letras_certas :
                        plc += let
               elif letter != let  :
                    plc+='_ '  
             
               
          return plc
                              
	# Método para checar o status do game e imprimir o board na tela
     def mostraBoard(self):
          if len(self.letras_erradas) <7:
               
               print(board[len(self.letras_erradas)])
               print(len(self.letras_erradas))
                    


def sorteia_palavra():
     palavras = ['banana','abacate','figo','laranja','morango','jabuticaba','tomate','uva','acerola']
     sorteada = random.choice(palavras)
     return sorteada

def main():
     print("Bem vindo ao jogo Hangman")
     letra_escolhida = input("\nDigite uma letra: ")
     game = Hangman(sorteia_palavra())
     while not game.game_over():
          
          print(game.hide(letra_escolhida))
          game.adivinha(letra_escolhida) 
          
         
          game.mostraBoard()
          letra_escolhida = input("\nDigite uma letra: ")

     if game.won():
          print("Parabéns,você ganhou!")
     else:
          print("Você perdeu! A palavra era "+game.palavra)
          

     
if __name__ == "__main__":
     main()