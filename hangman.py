import random

'''words = ['PERSON', 'PICTURE', 'PEN', 'PENCIL', 'PARK', 'PARTY', 'OIL', 'PAINTER', 'NEST', 'NEWS', 'MOUNTAIN', 'MOVIE', 'MORNING', 'NAME', 'MOBILE', 'MONEY', 'MARKET', 'MIRROR', 'LIFE', 'MAGAZINE', 'LAND', 'LAW', 'LEAVES', 'LETTER', 'JEWELRY', 'JOB', 'INDUSTRY', 'ISLAND', 'HOSPITAL', 'IDEA', 'YESTERDAY', 'HILL', 'YEAR', 'HEALTH', 'WOMEN', 'GAS', 'WOOD', 'GROUP', 'GARDEN', 'WEEK', 'WATER', 'GAME', 'VIEW', 'FUTURE', 'TRAIN', 'FOOD', 'TRADE', 'FLOWERS', 'TRACTOR', 'FLOOR', 'JAZZ', 'ZEPHYR', 'FIZZ', 'BUZZ', 'BUS', 'QUIZ']
'''

dick = {'pequeño':'small','grande':'big','quiere ser':'wants to be', 'también':'also','inteligente':'intelligent','puede contar':'is able to count','al revés':'in reverse','atlético':'athletic','gimnasta':'gymnast','poético':'poetic','puede inventar':'can invent','babuino':'baboon','tan pequeña como':'as small as','quiere tener':'wants to have','trompa':'trunk','puede levantar':'is able to lift','levanta':'lifts','piernas':'legs','orejas':'ears','todavía':'still','pobre':'poor','por accidente':'by accident','roca':'rock','salta':'jumps','mueve':'moves','lo atrapa':'traps him','grita':'shouts','hoyo':'hole','salvar':'to save','salva':'saves','escapa':'escapes','puede escapar':'is able to escape','corazón':'heart','está contento':'is happy','día':'day','porque':'because','héroe':'hero','necesita mover':'needs to move'}

words = list(dick.keys())

def validguess(guessed):
  #checks everything to make sure the input is valid, and returns that input as a guess
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÑ"
  while True:
    letter = input("Please make your guess (A-Z): ")
    if letter.upper() in alphabet and len(letter) == 1 and letter.upper() not in guessed:
      return letter
    elif letter.upper() in guessed:
      print()
      print("You've already guessed that letter")
      print()
    else:
      print()
      print("Sorry, that's not a valid letter")
      print()

def print_hangman(word, guessed, de):
  string = ''
  for i in word:
    if i == ' ':
      string += "  "
    elif i.upper() in guessed:
      string += i + ' '
    else:
      string += '_ '
    
    
  defi = dick[word]
    
  word = word.replace(' ', '')
  wrong = 0
  for letter in guessed:
    if letter.upper() not in word.upper():
      wrong += 1

  print()
  print(' ' * 15 + "-" * 15)

  if wrong == 0:
    for _ in range(5):
      print(" " * 29 + '|')

      #Head
  elif wrong >= 1:
    print(' ' * 15 + '|' + ' ' * 13 + '|')
    print(' ' * 13 + '-----' + ' ' * 11 + '|')
    print(' ' * 11 + '/'  + ' ' * 7 + '\\' + ' ' * 9 + '|')
    print(' ' * 11 + '\\'  + ' ' * 7 + '/' + ' ' * 9 + '|')
    print(' ' * 13 + '-----' + ' ' * 11 + '|')

      #arms and body
  if wrong >= 2 and wrong <= 4:
    for _ in range(3):
      print(' ' * 15 + '|' + ' ' * 13 + '|')
  elif wrong == 5:
    print(' ' * 15 + '|' + ' ' * 13 + '|')
    print(' ' * 12 + ' / |  ' + ' ' * 11 + '|')
    print(' ' * 11 + ' /  |   ' + ' ' * 10 + '|')
  elif wrong == 6:
    print(' ' * 15 + '|' + ' ' * 13 + '|')
    print(' ' * 12 + ' / | \\' + ' ' * 11 + '|')
    print(' ' * 11 + ' /  |  \\' + ' ' * 10 + '|')
  elif wrong <2:
    for _ in range(3):
      print(" " * 29 + '|')

      #Legs or lack of them
  if wrong == 3:
    print(' ' * 15 + '|' + ' ' * 13 + '|')
    if de == True:
        print(' ' * 12 + '     \\' + ' ' * 11 + '|' + '      ' + defi)
    else:
        print(' ' * 12 + '     \\' + ' ' * 11 + '|' + '      ')
    print(' ' * 11 + '       \\' + ' ' * 10 + '|')
  elif wrong > 3:
    print(' ' * 15 + '|' + ' ' * 13 + '|')
    if de == True:
        print(' ' * 12 + ' /   \\' + ' ' * 11 + '|' + '      ' + defi)
    else:
        print(' ' * 12 + ' /   \\' + ' ' * 11 + '|' + '      ')
    print(' ' * 11 + ' /     \\' + ' ' * 10 + '|')
  elif wrong < 3:
    print(" " * 29 + '|')
    if de == True:
        print(" " * 29 + '|'+ '      ' + defi)
    else:
        print(" " * 29 + '|'+ '      ')
    print(" " * 29 + '|')

  #all possible values of 'wrong' print this, so its outside of an if statement
  print(" " * 29 + '|' + '      ' + string)
  print(" " * 29 + '|')
  print(" " * 29 + '|' + '      Guessed letters:')
  print(" " * 29 + '|' + '      ' + ''.join(sorted(guessed)))
  print(' ' * 24 + '-' * 11)
  print()

  #checks if word has been fully guessed
  count = 0
  for letter in word:
    if letter.upper() in guessed:
      count += 1
  if count >= len(word):
    return True
  elif wrong >= 6:
    return 'lost'
  else:
    return False

def hangman():
  word = random.choice(words)
  print()
  print()
  print("Welcome to hangman! A random word will be chosen and your job is to figure it out without guessing more than 6 wrong letters.")
  print()
  print("Make sure to type in your accents!")
  print()
  print("The word is %s letters long" % (str(len(word))))
  print()
  de = False
  if input('Would you like to play with definitions enabled? (y/n): ').upper() == 'Y':
    de = True
  print()
  guessed = []
  win = 0
  #print(word)
  while win == 0:
    guess = validguess(guessed)
    guessed.append(guess.upper())
    status = print_hangman(word, guessed, de)
    if status == True:
      win = 1
    elif status == 'lost':
      win = 2
  if win == 1:
    print("Congratulations, you win!")
  else:
    print("Too bad, you lose!")
    print()
    print("The word was: " + word)
    
hangman()

while True:
    if input('\n Would you like to play again? (y/n): ').upper() == 'Y':
        hangman()
        print()
    else:
        break

#exec(open("./script.py").read())

