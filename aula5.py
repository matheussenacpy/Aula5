print('1 - cadastrar 2 - listar 3 - sair')
opcao = int(input("Digite o numero da opção"))

match opcao:
    case 1:
        print("Você escolheu cadastrar")
    case 2:
        print("Você escolheu listar") 
    case 3:
        print("Você esescolheu sair")    
    case _:
        print("Opção Invalida")    
