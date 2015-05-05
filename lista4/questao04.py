import string
texto = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'

#palavras = texto.split()
#print(type(texto))
#print(type(palavras))

for bad in string.punctuation:
	texto = texto.replace(bad, '')
#print(texto)
match = []

texto = texto.split()
#print(type(texto))
for word in texto:
	if word[0] in 'python' or word[-1] in 'python':
		match.append(word)
print(match)

'''

i = 0
a = ['python']
texto = texto.split()
while i <= len(texto)-1:
	print(texto[i])
	if texto[i].startswith(a[0]) or texto[i].endswith(a[-1]):
		listaPython.append(a[i])
	i += 1
print(listaPython)

'''
