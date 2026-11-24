peso = float(input('Digite o peso em kg: '))
altura = float(input('Digite a altura em metros (ex: 1.75): '))

imc = peso / (altura ** 2)

print(f'Seu IMC é {imc:.2f}')

match imc:
    case i if i < 17:
        print('Muito abaixo do peso')
    case i if i < 18.5:
        print('Abaixo do peso')
    case i if i < 25:
        print('Peso normal')
    case i if i < 30:
        print('Acima do peso')
    case i if i < 35:
        print('Obesidade grau 1')
    case i if i <= 40:
        print('Obesidade grau 2')
    case _:
        print('Obesidade grau 3')