def yuvarla(sayi,n):
	sayi1=sayi*(10**(n+1))
	sayi2=int(sayi1%10)
	sayi3=int(sayi1/10)
	if sayi2>=5:
		sonuc=(sayi3+1)/float(10**n)
	else:
		sonuc=sayi3/float(10**n)
	
