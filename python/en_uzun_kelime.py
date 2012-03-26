def en_uzun(cumle):
	en_uzun=0
	liste = str.split(cumle)
	for i in liste:
		if len(i) > en_uzun :
			en_uzun = len(i)
	
	for i in liste:
		if len(i) ==en_uzun:
			indis=liste.index(i)
			print liste[indis]
	

en_uzun("usta askin alettin hop")
