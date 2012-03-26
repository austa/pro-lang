def basamak_topla(s):
	sayi=str(s)
	toplam=0
	for i in sayi:
		if int(i) > 5:
			toplam=toplam+int(i)
	return toplam
print basamak_topla(5648796)
