# Creacion de correos electronicos 
'''
empleados = []
compañia = []


cantidad = int(input('Cuantos empleados desea agregar: '))
for i in range(1,cantidad+1) : 
    empleados.append(input(f'Digite el nombre del empleado {i}: ').lower())
    compañia.append(input('Digite su compañia: ').lower())
    
for name,compa in zip(empleados,compañia) : 
    print(f'\nCorreo de {name} : {name}@{compa}.com')
    

'''


def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
             ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))

hangman("cat")
