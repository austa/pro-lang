def tekse_bir_ciftse_sifir(liste):
	liste2=[]
	for i in liste:
		if i % 2 == 0:
			liste2.append("0")
		else:
			liste2.append("1")
	print liste2
