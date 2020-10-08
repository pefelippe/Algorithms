'''
Encryption is transform some readable to not readable 
by sorting following rules.
Explicação:
    Uma frase: 'DianaMiguel' vai passar pela base
    
    Dian
    aMig
    uel
        Vamos tomar as letras de cada coluna: Dau iMe ail ng
'''

from math import sqrt


def encryption(s):
    l = len(s)
    sql = sqrt(l)
    rou = round(sql)

    if sql > rou:
        row, col = rou, (rou+1)
    else:
        row, col = rou, rou
    
    if len(s) < (row*col):
        auto_increment = row*col-len(s)
        s_increment = s+' '*auto_increment
    else:
        s_increment = s
    s_sliced = [s_increment[(m-1)*col:m*col] for m in list(range(1, row+1))]

    str_encpt = []
    for r in list(range(col)):
        for m in s_sliced:
            if r <= (len(m)-1):
                str_encpt += m[r]

    encrypt = ''.join(str_encpt)

    encrypt_sliced = [encrypt[(nn-1)*row:nn*row]
                      for nn in list(range(1, col+1))]

    encrypt_ss = [ss.strip() for ss in encrypt_sliced]
    encrypt_final = ' '.join(encrypt_ss)
    print(encrypt_final)
    return encrypt_final

    '''Entre com uma frase para criptografar.
        Alguns exemplos: 
            haveaniceday --> hae and via ecy
            feedthedog   --> fto ehg ee dd
            chillout     --> clu hlt io
    '''


cont = 0
while cont < 2:
    if cont == 0: print('A sentença: Feed the dog criptografada: ' + encryption('feedthedog'))
    print('**************************')
    encryption(''.join(input('Coloque sua frase para criptografar: ').split()))
    print('==========================')
    cont += 1
