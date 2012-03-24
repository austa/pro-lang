def hop(s, p):
	a=0
	sayi  = len(p)
	for i in range(len(s)):
		if s[i:i+sayi] == p:
			a+=1
	print a
hop("1011010101","101")
