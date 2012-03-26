def en_buyuk_sayi(s):
	liste = list(str(s))
	liste.sort()
	liste.reverse()
	print "".join(liste)
en_buyuk_sayi(69856)
