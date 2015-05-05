texto = '''The Python Software Foundation and the global
   Python community  welcome  and  encourage participation
   by everyone.  Our  community is  based  on mutual respect,
   tolerance, and encouragement, and we are working to help each
   other live up to  these  principles.  We  want our  community
   to  be  more  diverse: whoever you  are,  and whatever  your
   background, we welcome  you.'''.lower()
for x in texto.split():
    texto = texto.replace(',',' ')
    texto = texto.replace('.',' ')
    texto = texto.replace(':',' ')
    
nova = []
texto = 'thiago'
for palavra in texto.split():
    for letra in palavra:
         if letra in 'python' and len(palavra) > 4:
             nova.append(palavra)
print("As palavras que possuem umas das letras'PYTHON' são:\n%s" %nova)
print("São %d palavras" %len(nova))


