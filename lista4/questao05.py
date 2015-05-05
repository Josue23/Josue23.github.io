import string
texto = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'

for bad in string.punctuation:
	texto = texto.replace(bad, '')

match = []
texto = texto.lower()
texto = texto.split()
palavra = 'python'
for word in texto:
	print(word)
	#if word ==
	if word[::] in 'python' and len(word) > 4: 
		match.append(word)
print(match)
