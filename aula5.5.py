peso = float(input('Digite o peso em kg: '))

if peso > 100:
    excesso = peso - 100
    multa = excesso * 4
    print(f'Excesso de {excesso:.2f} kg. Multa: R$ {multa:.2f}')
else:
    print('Isento')