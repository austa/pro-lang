def kutle_endeksi(boy,kilo):
    if type(19.53) != type(boy):
	print"Boy uzunlugunuzu ondalik olarak giriniz."
    else:
	endeks = float(kilo)/float((boy**2))
	if endeks <= 18.5:
	    print"Zayifsiniz kilo almaniz gerekiyor."
	elif endeks >18.5 and endeks <=25.0:
	    print"Kilonuz normal."
	else:
	    print "Kilonuz normalden fazla."
	
