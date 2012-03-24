def altin_oran(n):
	a,b=0,1
	i=1
	while n > i:
		a,b=b,a+b
		i+=1
	altin_oran=float(b)/float(a)
	print altin_oran
altin_oran(786)
	
