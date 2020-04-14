def letra (a):
    v = 0
    c = 0
    for letra in a:
        if letra in 'aeiou':
            v += 1
        else:
            c +=1
    print ('Vogais: %d'%v)
    print('Consoantes: %d'%c)
    print('Total de letras: ', v+c)
    print (a[::-1])
        
   
    
