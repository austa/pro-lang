def onluk_tabana_cevir(sayi,taban):
	n = 1
	j = 0
	for i in sayi:
		j= (int(i) * (taban**(len(sayi)-n))) + j
		n+=1
	print j
