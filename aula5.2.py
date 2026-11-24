print(" Digite os seguinte animais: ")
print("cachorro\n gato\n leão\n tigre\n")
animal = input("Digite o nome dos animais listados")

match animal:
    case 'cahorro' | 'gato':
        print('Este é um animal domesticado')
    case 'Leão' | 'tigre':
        print('Este é um animal selvagem')
    case _:
        print('Animal ivalido ou nome digitado incorretamente')
        