def en_buyuk_basamak(s):
	sayi = str(s)
	en_buyuk = 0
	for i in sayi:
		if int(i) > en_buyuk:
			en_buyuk=int(i)
	print en_buyuk
en_buyuk_basamak(54679467)
