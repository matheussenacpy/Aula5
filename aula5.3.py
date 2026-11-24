nota= float(input('Digite sua nota'))

match nota:
    case n if n >= 10:
        print ('Conceito A - Excelente!')
    case n if n >= 8:
        print ('Conceito B - Bom')    
    case n if n >= 6:
        print ('Conceito C - Regular')
