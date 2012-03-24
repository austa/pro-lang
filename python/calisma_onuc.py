def kok_bulma(a,b,c):
	delta = b**2-(4*a*c)
	if delta < 0:
		print "denklemin reel koku yoktur."
	elif delta == 0:
		print "denklemin bir koku vardir."
	else:
		kok1 = (-b + (delta**0.5))/(2*a)
		kok2 = (-b - (delta**0.5))/(2*a)
		print"birinci kok",kok1,",ikinci kok",kok2

