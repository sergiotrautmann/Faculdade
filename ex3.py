def proibidas(frase):
    letras_proibidas = ['o','d','t']
    for x in letras_proibidas:
        print('foram contadas:', frase.count(x), 'letras', x)
proibidas('Hoje esta chovendo desde muito cedo')

def proibidas(frase):
    letras_proibidas =  ['m', 'p', 'q', 'a']
    for x in letras_proibidas:
        print('foram contadas:', frase.count(x), 'letras', x)
proibidas('Amanhã vai ser outro dia')

