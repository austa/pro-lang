def harf_sayisi_bulma(cumle):
	cumle_listesi=list(cumle)
	sesliler_sayisi=0
	sessizler_sayisi=0
	simgeler_sayisi=0
	sesliler="aeiouAEIOU"
	sessizler="qwrtyplkjhgfdszxcvbnmQWRTYPLKJHGFDSZXCVBNM"
	for i in cumle_listesi:
		if i in sesliler:
			sesliler_sayisi+=1
		elif i in sessizler:
			sessizler_sayisi+=1
		else:
			simgeler_sayisi+=1
	print "sesliler sayisi",sesliler_sayisi,"sessizler_sayisi",sessizler_sayisi,"simgeler sayisi",simgeler_sayisi
harf_sayisi_bulma("alaattin seni kopekler yesin")#boşlukları da bir simge olarak saydık
