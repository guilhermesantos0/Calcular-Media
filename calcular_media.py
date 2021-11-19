import os

def calculateGrades():
    firstTri = float(input('Primeiro trimestre: '))
    secondTri = float(input('Segundo trimestre: '))
    thirdTri = float(input('Terceiro trimestre: '))

    firstSem = float(input('Semestral: '))

    firstTriFinal = firstTri * 2
    secondTriFinal = secondTri * 3
    thirdTriFinal = thirdTri * 3

    actualCount = firstTriFinal + secondTriFinal + thirdTriFinal + firstSem

    anualNeed = 60 - actualCount
        
    os.system('cls')
    print(f'\n\n---------------------------\nSua soma: {"{0:.3g}".format(actualCount)}\n---------------------------\nNota necessária na anual: {"{0:.3g}".format(anualNeed)}\n---------------------------\n\n')

def calculateExpectedAnual():
    firstTri = float(input('Primeiro trimestre: '))
    secondTri = float(input('Segundo trimestre: '))
    thirdTri = float(input('Terceiro trimestre: '))

    firstSem = float(input('Semestral: '))
    secondSem = float(input('Anual: '))


    firstTriFinal = firstTri * 2
    secondTriFinal = secondTri * 3
    thirdTriFinal = thirdTri * 3

    if secondSem > firstSem:
        global newFirstSem
        newFirstSem = secondSem

    actualCount = firstTriFinal + secondTriFinal + thirdTriFinal + firstSem + secondSem
    simulatedCount = firstTriFinal + secondTriFinal + thirdTriFinal + newFirstSem + secondSem

    os.system('cls')
    print(f'\n\n---------------------------\nSoma Atual: {"{0:.3g}".format(actualCount)}\n---------------------------\nSoma Simulada: {"{0:.3g}".format(simulatedCount)}\n---------------------------\n\n')

while True:
    print('===============================\nO QUE VOCÊ DESEJA?\n===============================\n\n 1 - Calcular Média         2 - Simular Nota na Anual         3 - Sair')
    choice = input('>> ')

    if choice == '1':
        os.system('cls')
        calculateGrades()
    elif choice == "2":
        os.system('cls')
        calculateExpectedAnual()
    else:
        break
